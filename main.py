import os 
import sys
import config
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

import prompts
from chatbot import ConversationManager

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("GEMINI_API_KEY non trovato. Assicurati di aver impostato la variabile d'ambiente correttamente.")
    sys.exit(1)


client = genai.Client(api_key= api_key)

sessione_chat = client.chats.create(
    model = 'gemini-3.6-flash',
    config = {"system_instruction": prompts.get_system_prompt()}
)
conv_manager = ConversationManager(max_messages=config.MAX_HISTORY_MESSAGES)

@retry(
    wait=wait_exponential(multiplier=config.RETRY_MULTIPLIER, min=config.RETRY_MIN_WAIT, max=config.RETRY_MAX_WAIT),
    stop = stop_after_attempt(config.RETRY_MAX_ATTEMPTS),
    retry = retry_if_exception_type(errors.APIError)
)

def invia_messaggio_e_ricevi_risposta(prompt):
    return sessione_chat.send_message_stream(prompt)

def main():
    print("Benvenuto, sono il tutor accademico esperto di Reti di Calcolatori")
    print("Puoi chiedermi di spiegare concetti, generare esercizi o rispondere a domande specifiche.")
    print("Digita '/help' per vedere i comandi disponibili o '/exit' per uscire.\n")

    while True:
        try:
            io_input = input("Tu: ").strip()

            if not io_input:
                print("Input non può essere vuoto. Ritenta.")
                continue

            comando = io_input.lower()
            if comando == "/exit":
                print("Fine sessione di studio. Arrivederci!")
                break
            elif comando == "/help":
                print("\nComandi disponibili:")
                print(" /esercitazione [argomento] - Genera un esercizio pratico sull'argomento specificato.")
                print(" /riassunto                 - Mostra le statistiche di utilizzo")
                print(" /clear                     - Cancella la cronologia della conversazione")
                print(" /exit                      - Esci dal programma\n")
                continue
            elif comando == "/clear":
                conv_manager.clear_history()
                print("Cronologia della conversazione cancellata.")
                continue
            elif comando == "/riassunto":
                storico = conv_manager.get_history()
                print("\n-------Riepilogo della conversazione-------")
                print(f"Messaggi nel buffer: {len(storico)} / {conv_manager.max_messages}")
                print("Nota: Il calcolo esatto dei token per lo streaming locale richiede un tokenizer esterno,")
                print("ma mantenere il buffer sotto i 10 messaggi garantisce un consumo ottimale.\n")
                continue
            elif comando.startswith("/esercitazione"):
                argomento = io_input[9:].strip()
                if not argomento:
                    argomento = "argomento casuale di Reti di Calcolatori"
                io_input = prompts.get_practice_question(argomento)
                print(f"\n[Modalità Esercizio: {argomento}]")

            conv_manager.add_message("user", io_input)
            
            print("Tutor: ", end="", flush=True)
            full_response = ""
            
            response_stream = invia_messaggio_e_ricevi_risposta(io_input)
            for chunk in response_stream:
                print(chunk.text, end="", flush=True)
                full_response += chunk.text
                
            print("\n") 
            conv_manager.add_message("model", full_response)

        except KeyboardInterrupt:
            # Gestione uscita pulita con Ctrl+C
            print("\nChiusura forzata rilevata. Arrivederci!")
            break
        except Exception as e:
            # Gestione errori generali dopo aver esaurito i retry
            print(f"\n[Errore di Sistema]: {e}")
            print("Il servizio potrebbe essere momentaneamente irraggiungibile.")

if __name__ == "__main__":
    main()    

                    
