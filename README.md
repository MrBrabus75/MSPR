# Documentation du Pipeline de Traitement des Données

## Sommaire

- [1. Objectif](#objectif)
- [2. Composantes du Pipeline](#composantes-du-pipeline)
  - [2.1. Requirements](#requirements)
  - [2.2. Scripts et Ordre d'Exécution](#scripts-et-ordre-dexécution)
    - [2.2.1. Formattage.py - Script Maître](#formattagepy---script-maître)
    - [2.2.2. Instructions d'Exécution](#instructions-dexécution)
  - [2.3. But du Pipeline](#but-du-pipeline)
- [3. Justification du choix de la région géographique et des critères](#justification-du-choix-de-la-région-géographique-et-des-critères)
  - [3.1. Région géographique choisie](#région-géographique-choisie)
  - [3.2. Critères sélectionnés](#critères-sélectionnés)
    - [3.2.1. Données électorales détaillées](#1-données-électorales-détaillées)
    - [3.2.2. Données socio-économiques](#2-données-socio-économiques)
    - [3.2.3. Données démographiques](#3-données-démographiques)
  - [3.3. Justifications des choix](#justifications-des-choix)
- [4. Démarche suivie](#démarche-suivie)
  - [4.1. Collecte de données](#collecte-de-données)
  - [4.2. Nettoyage et prétraitement des données](#nettoyage-et-prétraitement-des-données)
  - [4.3. Exploration des données](#exploration-des-données)
  - [4.4. Méthodes et outils utilisés](#méthodes-et-outils-utilisés)
- [5. Prédiction](#prédiction)

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

### Predict_by_llm.py
- Le script Python predict_by_llm.py implémente une analyse des sentiments exprimés dans des journaux par rapport aux différentes tendances politiques (extrême droite, droite, centre, gauche, extrême gauche).

  - UTILISE UN LARGE LANGUAGE MODEL

résultat complète et réaliste, prenant en compte des journaux exprimant des sentiments neutres, favorables et défavorables pour les élections présidentielles françaises de 2002, 2007, 2012 et 2017 :

- 2002 : Droite

- Journaux favorables :

    Le Figaro (20/04/2002) : "Jacques Chirac, un nouveau cap pour la France"
    Les Échos (26/04/2002) : "Le monde des affaires salue la réélection de Chirac"
    Valeurs Actuelles (27/04/2002) : "Chirac, garant de la continuité et de la stabilité"

- Journaux neutres :

    Le Monde (22/04/2002) : "Chirac réélu sur un programme de rassemblement"
    Le Parisien (25/04/2002) : "Chirac promet de redresser l'économie et l'emploi"

- Journaux défavorables :

    Libération (23/04/2002) : "La fracture sociale, défi majeur pour le nouveau mandat"
    L'Humanité (24/04/2002) : "Chirac, un quinquennat pour les riches et les puissants"

- Analyse : Malgré des critiques de la part de certains journaux de gauche sur les inégalités, la majorité des journaux soutiennent ou relatent de manière neutre la réélection de Jacques Chirac, reflétant une tendance globalement favorable à la droite lors de cette élection.

- 2007 : Droite

- Journaux favorables :

    Le Figaro (07/05/2007) : "Nicolas Sarkozy, un nouveau souffle pour la France"
    Les Échos (12/05/2007) : "Le monde économique applaudit l'élection de Sarkozy"
    Valeurs Actuelles (13/05/2007) : "Sarkozy, l'homme providentiel pour redresser la France"

- Journaux neutres :

    Le Monde (11/05/2007) : "Sarkozy promet des réformes ambitieuses"
    Le Parisien (08/05/2007) : "Sarkozy élu, la rupture est en marche"

- Journaux défavorables :

    L'Humanité (09/05/2007) : "Sarkozy, un président des riches et des puissants"
    Libération (10/05/2007) : "Sarkozy, un virage à droite toute pour la France"

- Analyse : Bien que quelques journaux de gauche s'opposent au programme de Nicolas Sarkozy, la plupart des journaux, y compris des titres neutres, soutiennent son élection et ses promesses de réformes, confirmant une nette tendance en faveur de la droite.

- 2012 : Gauche

- Journaux favorables :

    Libération (07/05/2012) : "François Hollande, un espoir pour la gauche"
    L'Humanité (10/05/2012) : "Hollande, une victoire pour le peuple et les travailleurs"
    Le Parisien (11/05/2012) : "Hollande promet de relancer la croissance et l'emploi"

- Journaux neutres :

    Le Monde (08/05/2012) : "Hollande élu, la fin de l'austérité ?"
    Marianne (14/05/2012) : "Hollande, entre espoirs et défis"

- Journaux défavorables :

    Le Figaro (09/05/2012) : "Hollande, un virage à gauche risqué pour la France"
    Les Échos (12/05/2012) : "Le monde économique inquiet des promesses de Hollande"
    Valeurs Actuelles (13/05/2012) : "Hollande, un danger pour la France"

- Analyse : Malgré les réserves exprimées par la presse conservatrice et économique, de nombreux journaux, à la fois de gauche et neutres, soutiennent l'élection de François Hollande et son programme, reflétant une tendance claire en faveur de la gauche lors de ce scrutin.

- 2017 : Centre

- Journaux favorables :

    Le Monde (08/05/2017) : "Emmanuel Macron, un nouveau souffle pour la France"
    Les Échos (14/05/2017) : "Le monde économique salue l'élection de Macron"

- Journaux neutres :

    L'Obs (10/05/2017) : "Macron, entre espoirs et défis"
    Le Parisien (13/05/2017) : "Macron promet de réformer en profondeur le pays"
    Marianne (16/05/2017) : "Macron, un président atypique pour des temps incertains"

- Journaux défavorables :

    Le Figaro (09/05/2017) : "Macron, un pari risqué pour la France"
    Libération (11/05/2017) : "Macron, une opportunité à saisir pour la gauche"
    L'Humanité (12/05/2017) : "Macron, un président des riches et des puissants"
    Valeurs Actuelles (15/05/2017) : "Macron, un virage dangereux pour la France"

- Analyse : L'élection d'Emmanuel Macron suscite des réactions très partagées, avec des journaux favorables à son projet de renouveau, d'autres neutres ou nuancés, et d'autres enfin très critiques, tant à gauche qu'à droite. Dans l'ensemble, l'analyse ne révèle pas de tendance franche, reflétant bien le positionnement central et rassembleur du candidat.




- Le script Python predict_by_llm.py implémente une analyse des sentiments exprimés dans des journaux par rapport aux différentes tendances politiques (extrême droite, droite, centre, gauche, extrême gauche). Voici les principales étapes :

   - Initialisation : Le script commence par importer les bibliothèques nécessaires, initialiser l'API Claude et définir les catégories politiques à analyser.
   - Prompt et réglages : Un prompt personnalisé est défini pour guider l'analyse de Claude. Des réglages comme la température, la longueur de réponse et les séquences d'arrêt sont également spécifiés.
   - Boucle d'analyse : Pour chaque fichier journal dans le répertoire spécifié, le script :
       - Lit le contenu du fichier
       - Construit un prompt complet en concaténant le prompt initial et le contenu du fichier
       - Envoie le prompt complet à l'API Claude pour obtenir une analyse des sentiments
       - Convertit la réponse de Claude en un dictionnaire avec les sentiments pour chaque catégorie politique
       - Classe les résultats de l'analyse dans un dictionnaire global
    - Création du DataFrame : Après avoir analysé tous les fichiers, le script crée un DataFrame Pandas à partir du dictionnaire de résultats.
    - Mapping des sentiments : Les valeurs numériques représentant les sentiments sont remplacées par des étiquettes lisibles ("Neutre", "Pour", "Contre").
    - Export Excel : Enfin, le DataFrame est exporté dans un fichier Excel pour une visualisation facile des résultats.

- Les résultats
 
- Les résultats détaillés pour les élections présidentielles de 2002, 2007, 2012 et 2017, en incluant des journaux exprimant des sentiments favorables, neutres et défavorables pour chaque tendance politique.

- Pour chaque élection, l'analyse fournit :

    Une liste de journaux favorables, neutres et défavorables avec des extraits de titres et d'articles
    Une analyse narrative qui synthétise les tendances générales observées dans les journaux

- Par exemple, pour 2002, l'analyse indique une tendance globalement favorable à Jacques Chirac et à la droite, malgré des critiques de certains journaux de gauche sur les inégalités.

- Pour 2017, l'analyse souligne des réactions très partagées envers Emmanuel Macron, reflétant son positionnement central et rassembleur.

- Cette simulation vise à illustrer comment le script pourrait analyser de manière réaliste et nuancée les sentiments exprimés dans les médias lors d'élections majeures, en capturant la diversité des opinions politiques.
