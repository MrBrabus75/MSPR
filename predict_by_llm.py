import os
import pandas as pd
from typing import Dict
from claude_api import ClaudeAPI

# Initialisation de l'API Claude
claude = ClaudeAPI(api_key="your_api_key")

# Répertoire contenant les journaux
news_dir = "/home/gptlab/news"

# Catégories politiques à analyser
political_categories = ["Extrême droite", "Droite", "Centre", "Gauche", "Extrême gauche"]

# Prompt pour l'analyse des journaux
prompt = f"""
Analyse le contenu suivant et détermine s'il exprime un sentiment neutre, en faveur ou contre les différentes catégories politiques suivantes : {', '.join(political_categories)}.

Réponds avec un dictionnaire Python où les clés sont les catégories politiques et les valeurs sont 1 pour un sentiment neutre, 2 pour un sentiment en faveur et 3 pour un sentiment contre.

Par exemple :
{{
    "Extrême droite": 2,
    "Droite": 1,
    "Centre": 3,
    "Gauche": 1,
    "Extrême gauche": 2
}}

Contenu :
"""

# Réglages pour l'API Claude
settings = {
    "temperature": 0.2,  # Contrôle la créativité de la réponse
    "max_tokens": 124000,  # Longueur maximale de la réponse
    "stop_sequences": ["Contenu :"]  # Séquences pour arrêter la réponse
}

# Dictionnaire pour stocker les résultats
results: Dict[str, list] = {category: [] for category in political_categories}

# Parcourir tous les fichiers dans le répertoire
for filename in os.listdir(news_dir):
    filepath = os.path.join(news_dir, filename)
    
    # Ouvrir le fichier et lire son contenu
    with open(filepath, "r") as file:
        content = file.read()
    
    # Construire le prompt complet avec le contenu du fichier
    full_prompt = prompt + content
    
    # Envoyer le prompt à l'API Claude pour l'analyser
    analysis = claude.complete(full_prompt, settings)
    
    try:
        # Convertir la réponse de Claude en dictionnaire
        analysis_dict = eval(analysis.choices[0].text)
    except (ValueError, SyntaxError):
        print(f"Erreur lors de l'analyse du fichier {filename}")
        continue
    
    # Classer l'analyse dans les résultats
    for category, sentiment in analysis_dict.items():
        results[category].append(sentiment)

# Créer un DataFrame Pandas à partir des résultats
df = pd.DataFrame(results)

# Mapper les valeurs numériques aux étiquettes de sentiment
sentiment_labels = {1: "Neutre", 2: "Pour", 3: "Contre"}
df = df.replace(sentiment_labels)

# Enregistrer le DataFrame dans un fichier Excel
df.to_excel("news_analysis.xlsx", index=False)
