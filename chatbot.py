from google import genai
import os
import config
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#verranno mantenuti solo gli ultimi 10 messaggi della conversazione
class ConversationManager:
    #costruttutore che inizializza una lista vuota per la cronologia e imposta un limite di memoria a 10 messaggi di default
    def __init__(io, max_messages=config.MAX_HISTORY_MESSAGES):
        io.history = []
        io.max_messages = max_messages

    #. Inserendo l'undicesimo messaggio in una lista configurata per mantenerne dieci, 
    # l'esecuzione immediata di trim_history() rimuove il nodo più vecchio.
    def add_message(io, role, content):
        io.history.append({"role": role, "content": content})
        io.trim_history()

    #Se la lista ha 12 messaggi e il limite è 10, i primi 2 (i più vecchi) vengono cancellati.       
    def trim_history(io):
        if len(io.history) > io.max_messages:
            io.history = io.history[-io.max_messages:]

    #Cancella la cronologia della conversazione
    def clear_history(io):
        io.history = []

    #Restituisce la cronologia della conversazione
    def get_history(io):
        return io.history        

    # Invia un messaggio al modello Gemini e riceve la risposta man mano che viene generata, 
    # restituendo un generatore che produce i chunk di testo della risposta.
    def stream_gemini_response(prompt, sessione_chat):
        risposta_stream= sessione_chat.send_message_stream(prompt)
        for chunk in risposta_stream:
            yield chunk.text