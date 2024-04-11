import os
import weaviate
import pandas as pd
from openai import OpenAI
from datetime import datetime

# Configuration de l'API OpenAI
api_key = 'votre_clé_api_openai'
openai_client = OpenAI(api_key=api_key)

# Configuration de la base de données Weaviate
weaviate_client = weaviate.Client("http://localhost:8080")

# Dossier contenant les articles de journaux
news_directory = "/home/weaviate/db_news"

# Spectres politiques analysés
political_spectrums = ["Extrême droite", "Droite", "Centre", "Gauche", "Extrême gauche"]

# Initialiser DataFrame pour les résultats
columns = ["Filename", "Excerpt", "Extrême droite", "Droite", "Centre", "Gauche", "Extrême gauche"]
results_df = pd.DataFrame(columns=columns)

# Fonction pour demander à ChatGPT de classifier un texte
def classify_text(text, spectrum):
    prompt = f"Concernant les élections françaises, est-ce que cet article est pour, contre, ou neutre envers {spectrum}? Réponse: 1 = Neutre, 2 = Pour, 3 = Contre.\n\n{text}"
    response = openai_client.Completion.create(
        model="text-davinci-003",  # Assurez-vous d'utiliser le dernier modèle disponible
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Lire tous les fichiers de journal dans le dossier spécifié
for filename in os.listdir(news_directory):
    if filename.endswith(".txt"):  # Assurer que seuls les fichiers .txt sont traités
        with open(os.path.join(news_directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # Obtenir les embeddings du texte (optionnel, pour améliorer la gestion des données)
        try:
            weaviate_client.data_object.create(
                data_object={"text": content},
                class_name="Article"
            )
        except Exception as e:
            print(f"Erreur lors de l'insertion dans Weaviate: {e}")

        # Classifier le texte pour chaque spectre politique
        results = [filename, content[:100] + "..."]  # Sauvegarder l'extrait du contenu
        for spectrum in political_spectrums:
            sentiment = classify_text(content, spectrum)
            results.append(sentiment)
        
        # Ajouter les résultats dans le DataFrame
        results_df.loc[len(results_df)] = results

# Sauvegarde des résultats dans un fichier Excel
output_filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
results_df.to_excel(output_filename, index=False)

print(f"Les résultats ont été sauvegardés dans {output_filename}")
