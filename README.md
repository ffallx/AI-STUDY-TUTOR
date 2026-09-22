# AI Study Assistant - Tutor Reti di Calcolatori

Questo progetto implementa un chatbot CLI basato sull'API di Google Gemini, configurato per fungere da tutor universitario specializzato in Reti di Calcolatori. Le risposte e le spiegazioni sono modellate per seguire rigorosamente l'approccio didattico dei testi di Fred Halsall.

## Setup
1. Clona il repository e crea un ambiente virtuale:
   `python3 -m venv venv`
   `source venv/bin/activate`
2. Installa le dipendenze richieste:
   `pip install google-genai python-dotenv tenacity`
3. Crea un file `.env` nella root del progetto e inserisci la tua chiave API:
   `GEMINI_API_KEY="tua_chiave_qui"`
4. Avvia l'assistente:
   `python3 main.py`

## Comandi Supportati
* `/help` - Mostra la lista dei comandi.
* `/practice [argomento]` - Genera uno scenario pratico o un esercizio (es. `/practice protocollo IP`).
* `/summary` - Mostra lo stato del buffer di conversazione.
* `/clear` - Azzera la cronologia dei messaggi.
* `/quit` - Chiude il programma in modo sicuro.

## Esempio di Utilizzo
```text
Tu: Spiegami l'incapsulamento
Tutor: [Spiegazione in streaming basata sul testo di Halsall...]
Tu: /practice subnetting
Tutor: [Generazione esercizio pratico...]