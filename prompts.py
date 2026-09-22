def get_system_prompt():
    return(
        "Sei un tutor universitario esperto in Reti di Calcolatori e Architettura dei Sistemi. "
        "Devi basare rigorosamente tutte le tue spiegazioni e modelli sui testi di Fred Halsall. "
        "Mantieni un tono analitico, rigoroso e orientato al problem-solving. "
        "Non fornire subito la soluzione finale; guida l'utente attraverso il ragionamento."
    )

def get_concept_explanation(concept, detail):
    return(
        f"Spiega dettagliatamente il funzionamento di {concept} concentrandoti sul meccanismo di {detail}."
        "Devi basare le tue spiegazioni esclusivamente sulle definizioni e i concetti forniti nel testo di Fred Halsall."
        "Non semplificare eccessivamente ma guida l'utente attraverso il ragionamento passo dopo passo."
        "Includi esempi pratici e casi d'uso e chiedi all'utente se ha compreso il concetto prima di procedere con ulteriori dettagli."
    )

def get_practice_question(topic):
    return(
        f"Genera un esercizio o uno scenario pratico riguardo a {topic}."
        "Fornisci i requisiti, attendi la mia soluzione e correggi eventuali errori riproponendo successivamente un esercizio per capire meglio il concetto."
    )