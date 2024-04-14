import weaviate
import openai
import pandas as pd

# Configuration de l'API OpenAI
openai.api_key = 'votre_clé_API'

# Connexion à la base de données Weaviate locale
client = weaviate.Client("http://localhost:8080")

# Fonction pour utiliser ChatGPT
def ask_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Fonction pour déterminer la position par rapport au candidat
def determine_position(text):
    sentiment_prompt = f"Déterminez si ce texte est pour, contre ou neutre par rapport au candidat: {text}"
    position = ask_chatgpt(sentiment_prompt)
    return position.strip()

# Extraction des données depuis Weaviate
def extract_data():
    query = """
    {
      Get {
        Article (limit: 1000000) {
          title
          subtitle
          source {
            name
          }
          content
        }
      }
    }
    """
    result = client.query.raw(query)
    return result['data']['Get']['Article']

def analyze_articles(articles):
    data = []
    for article in articles:
        title = article['title']
        subtitle = article['subtitle'] if 'subtitle' in article else ""
        journal_name = article['source']['name']
        
        # Extraire les noms des candidats et déterminer la position
        extract_names_prompt = f"Listez tous les noms de candidats mentionnés dans ce texte: {title} {subtitle}"
        candidates = ask_chatgpt(extract_names_prompt).split(',')
        candidates = [name.strip() for name in candidates if name.strip()]
        
        # Déterminer la position pour chaque candidat
        for candidate in candidates:
            position = determine_position(f"{title} {subtitle}")
            data.append({
                "Candidat": candidate,
                "Nom du Journal": journal_name,
                "Titre du journal": title,
                "Sous-titre du journal": subtitle,
                "Pour / Contre / Neutre": position
            })

    return pd.DataFrame(data)

def save_to_excel(df):
    # Calculer la récurrence
    df['Réccurence'] = df.groupby(['Candidat', 'Nom du Journal', 'Pour / Contre / Neutre'])['Titre du journal'].transform('count')
    # Suppression des doublons
    df = df.drop_duplicates()
    # Écriture dans un fichier Excel
    df.to_excel("analyse_journal_elections.xlsx", index=False)

# Exécution des fonctions
articles = extract_data()
df = analyze_articles(articles)
save_to_excel(df)
