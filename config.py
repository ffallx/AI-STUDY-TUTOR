# config.py

# Impostazioni del Modello
MODEL_NAME = "gemini-3.6-flash"

# Impostazioni della Cronologia
MAX_HISTORY_MESSAGES = 10

# Impostazioni di Riconnessione (Gestione Errori)
RETRY_MULTIPLIER = 1
RETRY_MIN_WAIT = 2
RETRY_MAX_WAIT = 10
RETRY_MAX_ATTEMPTS = 4