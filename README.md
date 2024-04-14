## Objectif

Ce pipeline de traitement des données a été conçu pour transformer des données brutes en un ensemble structuré, normalisé et enrichi, prêt pour des analyses avancées. Il assure la qualité et la cohérence des données à travers plusieurs étapes de transformation.

## Composantes du Pipeline

Le pipeline se compose de cinq scripts principaux, exécutés dans un ordre spécifique par un script maître (`Formattage.py`). Chaque script a un rôle défini dans le processus de nettoyage et de préparation des données.

### Requirements

Voici le fichier `requirements.txt` contenant les bibliothèques Python utilisées dans les scripts :
- `pandas`
- `openpyxl`
- `logging`
- `re`
- `statsmodels`
- `scikit-learn`
- `joblib`

### Scripts et Ordre d'Exécution

0. Avant tout installez tous les packages python nécessaires : `pip install -r requirements.txt`
1. `Formattage07121722.py` - Prépare les données brutes, corrigeant les formats de date, standardisant les noms de colonnes, et supprimant les enregistrements superflus.
2. `Normalisation.py` - Normalise les données pour assurer une cohérence, corrige les erreurs de saisie, et uniformise les formats.
3. `Formatting-merge2.py` - Fusionne les données de sources multiples, garantissant l'intégrité et la cohérence des données combinées.
4. `add_age_vote.py` - Enrichit les données avec des informations calculées, comme l'âge basé sur la date de naissance et des catégories de vote.
5. `Normalisation2.py` - Applique une couche supplémentaire de normalisation pour peaufiner les données après les enrichissements et les modifications précédentes.
6. `region.py` - Ajoute la région à tous les départements.

#### Formattage.py - Script Maître

Ce script orchestre l'exécution séquentielle des autres scripts. Il utilise la bibliothèque `subprocess` pour appeler chaque script Python dans l'ordre spécifié, garantissant que les données passent par toutes les étapes nécessaires du processus de préparation.
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/diagram.png)
### Instructions d'Exécution

1. Placez tous les scripts et les ensembles de données nécessaires dans un même répertoire.
2. Assurez-vous que Python est correctement installé sur votre système.
3. Ouvrez un terminal ou une invite de commande dans le répertoire contenant les scripts.
4. Exécutez le script maître avec la commande : `python Formattage.py`.
5. Le script maître exécutera automatiquement chaque script dans l'ordre, affichant le statut de chaque étape dans le terminal et enregistrant les détails dans un fichier log (`data_processing.log`).

### But du Pipeline

Le but de ce pipeline est de fournir une méthode structurée et répétable pour préparer les données à des fins d'analyse. En automatisant le processus de nettoyage, de normalisation, et d'enrichissement des données, nous visons à améliorer l'efficacité et la précision des analyses ultérieures, tout en réduisant le potentiel d'erreur humaine.

## Justification du choix de la région géographique et des critères

### Région géographique choisie
Nouvelle-Aquitaine

### Critères sélectionnés

#### 1. Données électorales détaillées
- `libellé_de_la_région` : Nom de la région pour l'identification
- `année` : Année de l'élection
- `tour` : Tour de l'élection (1er, 2nd, etc.)
- `parti` : Parti politique des candidats
- `tendance_politique` : Orientation politique (gauche, droite, etc.)
- `inscrits` : Nombre d'électeurs inscrits
- `abstentions` : Nombre d'abstentions
- `votants` : Nombre de votants
- `exprimés` : Nombre de suffrages exprimés
- `voix` : Nombre de voix par parti
- `%_voix/ins` : Pourcentage des voix par rapport aux inscrits
- `%_voix/exp` : Pourcentage des voix par rapport aux exprimés
- `moyenne_du_parti_XX_ans` : Pourcentage moyen des voix par tranche d'âge pour chaque parti

#### 2. Données socio-économiques
- `taux_de_chômage` : Taux de chômage dans la région
- `incidents_de_délinquance` : Nombre d'incidents liés à la délinquance
- `pib` : Produit intérieur brut de la région

#### 3. Données démographiques
- `18-24_ans`, `25-34_ans`, `35-49_ans`, `50-64_ans`, `65_ans_et_plus` : Répartition de la population par tranches d'âge

### Justifications des choix

- La région Nouvelle-Aquitaine est représentative d'une grande diversité territoriale, offrant un bon équilibre entre zones urbaines, semi-urbaines, et rurales. Elle offre une quantité substantielle de données pour une analyse robuste.

- Les données électorales détaillées par parti, tendance politique, nombre de voix, pourcentages et tranches d'âge sont cruciales pour entraîner des modèles prédictifs fiables des comportements électoraux. Elles permettent d'analyser finement les préférences selon les caractéristiques des électeurs.

- Le taux de chômage et le PIB sont des indicateurs économiques majeurs qui influencent souvent les choix électoraux. Ils reflètent le contexte socio-économique de la région.

- Les incidents de délinquance apportent une dimension sécuritaire, un critère déterminant pour beaucoup d'électeurs.

- La répartition par tranches d'âge permet d'étudier les tendances de vote selon les générations et d'adapter les analyses en conséquence.

## Démarche suivie

### Collecte de données
- Les données ont été récupérées à partir des sites data.gouv.fr et insee.fr, incluant des informations sur le chômage, la délinquance, le PIB, la population, et les résultats des élections présidentielles de 2007 à 2022.

### Nettoyage et prétraitement des données
- Plusieurs scripts Python ont été utilisés pour effectuer diverses tâches de nettoyage et de prétraitement :
  - `Formattage07121722.py`, `Normalisation.py`, `Formatting-merge2.py`, `add_age_vote.py`, `Normalisation2.py`.

### Exploration des données
- Une exploration approfondie des données a été réalisée pour comprendre leur structure, identifier les anomalies, et préparer les étapes de modélisation.

### Méthodes et outils utilisés
- Python et ses bibliothèques (Pandas, Logging, Re), ainsi que Excel pour le stockage initial des données.

## Prédiction

### IA_predict.py
- Ce script d'intelligence artificielle est conçu pour la prédiction des tendances politiques dans la région Nouvelle-Aquitaine en utilisant des techniques avancées d'analyse de données et de modélisation prédictive
   - Le script commence par charger un jeu de données depuis un fichier Excel spécifique.
   - Les données sont filtrées pour cette région (Nouvelle Aquitaine) et seul les colonnes numériques sont utilisées pour calculer une matrice de corrélation.

-Prévision des Caractéristiques Futures:
  - Il utilise le modèle ARIMA pour prédire les valeurs futures de plusieurs caractéristiques démographiques et économiques sur 4 années à venir.

Préparation des Données pour la Modélisation:
  - Les données historiques et prévues sont combinées et préparées pour la modélisation. Les classes sont rééquilibrées à l'aide de la technique SMOTE pour améliorer la performance des modèles sur des données déséquilibrées.

Configuration et Évaluation des Modèles de Classification:
  -  Trois modèles de classification sont configurés dans des pipelines qui intègrent des étapes de normalisation, d'imputation, et de réduction de dimensionnalité (PCA).
  -  Les modèles sont évalués avec une recherche en grille (GridSearchCV) pour optimiser leurs hyperparamètres sur des plis stratifiés.
  -  Le modèle avec la meilleure performance est sélectionné et utilisé pour faire des prédictions sur les données de test.

Sauvegarde et Prédiction Finale:
  - Le meilleur modèle est sauvegardé sur le disque.
  - Ce modèle est ensuite utilisé pour prédire les tendances politiques des années futures en utilisant les caractéristiques démographiques et économiques prévues.

Utilisation
  - Pour exécuter ce script, assurez-vous que le chemin d'accès au fichier de données Excel est correct et que toutes les bibliothèques nécessaires sont installées. Le script peut être exécuté pour générer des prévisions de tendances politiques, qui sont sauvegardées et affichées à la fin de l'exécution.

Résultats
 - Le script affiche la matrice de corrélation des caractéristiques, les meilleurs paramètres pour chaque modèle de classification testé, et les performances de ces modèles en termes de précision sur l'ensemble de test. Finalement, il prédit les tendances politiques pour les prochaines années et les affiche, offrant une vision prospective basée sur les données historiques et les prévisions démographiques et économiques. La précision globale obtenue sur l'ensemble de test est de 33.9%, reflétant les défis liés à la prédiction précise des tendances politiques à partir des données disponibles.

- France entière :
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2007%20t1.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2007%20t2.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2012%20t1.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2012%20t2.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2017%20t1.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2017%20t2.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2022%20t1.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/2022%20t2.png)

- Nouvelle Aquitaine :
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/NA%202007.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/NA%202012.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/NA%202017.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/NA%202022.png)

- Prédiction :
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/NA.png)
![alt text](https://github.com/MrBrabus75/MSPR/blob/master/NA2.png)

| Années | Région             | Élu           |
|--------|--------------------|---------------|
| 2007   | Nouvelle-Aquitaine | Gauche        |
| 2012   | Nouvelle-Aquitaine | Gauche        |
| 2017   | Nouvelle-Aquitaine | Centre        |
| 2022   | Nouvelle-Aquitaine | Centre        |
| 2023   | Nouvelle-Aquitaine | Centre        |
| 2024   | Nouvelle-Aquitaine | Droite        |
| 2025   | Nouvelle-Aquitaine | Droite        |
| 2026   | Nouvelle-Aquitaine | Extrême Droite|
| 2027   | Nouvelle-Aquitaine | Extrême Droite|


### Predict_by_llm.py
- Un script Python détaillé et réaliste nommé predict_by_llm.py, qui analyse les sentiments exprimés dans des articles de journaux sur les élections présidentielles françaises et les classe par tendance politique, nous allons utiliser l'API de ChatGPT d'OpenAI, un modèle d'embedding pour le traitement de texte, et Weaviate, une base de données vectorielle pour stocker et rechercher les données. Le script classera les sentiments comme neutres, pour, ou contre, pour cinq spectres politiques (extrême droite, droite, centre, gauche, extrême gauche) et sauvegardera les résultats dans un fichier Excel.

- Explications et Détails :

    - Imports et Configurations:
        - Les bibliothèques nécessaires sont importées.
        - La connexion à l'API OpenAI et à Weaviate est configurée.

    - Spectres Politiques:
        - Une liste des spectres politiques pour lesquels les sentiments des articles seront classés.

    - Traitement des Fichiers:
        - Le script parcourt tous les fichiers texte dans le répertoire spécifié, lit leur contenu, et les insère dans Weaviate (pour utilisation ultérieure ou pour bénéficier de fonctionnalités avancées comme la recherche vectorielle).

    - Classification par ChatGPT:
        - Pour chaque article et pour chaque spectre politique, un prompt est envoyé à ChatGPT qui retourne une classification (Neutre, Pour, Contre).

    - Sauvegarde Excel:
        - Les résultats sont sauvegardés dans un DataFrame puis exportés dans un fichier Excel avec un timestamp pour éviter l'écrasement des fichiers précédents.
     
| Candidat          | Nom du Journal | Titre du journal                                           | Sous-titre du journal                                                                          | Pour / Contre / Neutre | Réccurence |
|-------------------|----------------|------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------|------------|
| Marine Le Pen     | Le Monde       | Sur l’international, la délicate présidentialisation de Marine Le Pen | Si la leader d’extrême droite revendique d’incarner la future cheffe de l’État, elle se montre discrète sur l’Ukraine. | Neutre                 | 2          |
| Emmanuel Macron   | Le Figaro      | Macron et les défis de la diplomatie française             | En pleine crise ukrainienne, le président cherche à renforcer la stature internationale de la France. | Pour                   | 1          |
| Jean-Luc Mélenchon| Libération     | Mélenchon, le tribun qui veut renverser Macron             | Le leader de la France insoumise propose un programme radicalement opposé à celui du président sortant. | Contre                 | 3          |
| Éric Zemmour      | France Soir    | Éric Zemmour face aux médias                               | Le candidat de la droite extrême s’attaque à la presse, qu’il juge trop bienveillante envers Macron.   | Contre                 | 2          |
| Yannick Jadot     | L'Écho         | Jadot et l'urgence climatique                              | Le candidat écologiste met le climat au cœur de sa campagne présidentielle.                       | Pour                   | 1          |
