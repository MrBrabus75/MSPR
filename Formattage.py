import subprocess

def run_script(script_path):
    """Fonction pour exécuter un script Python donné."""
    try:
        subprocess.run(['python', script_path], check=True)
        print(f"Le script {script_path} a été exécuté avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script {script_path}: {e}")

if __name__ == "__main__":
    # Liste des chemins des scripts à exécuter
    scripts = [
        'Formattage07121722.py',
        'Normalisation.py',
        'Formatting-merge2.py',
        'add_age_vote.py',
        'Normalisation2.py'
    ]

    # Exécuter chaque script dans l'ordre
    for script in scripts:
        run_script(script)
