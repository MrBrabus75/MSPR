Documentation du Pipeline de Traitement des Données
Sommaire

    1. Introduction
    2. Composantes du Pipeline
        2.1. Scripts et Ordre d'Exécution
        2.2. Objectif du Pipeline
    3. Justification du Choix de la Région Géographique et des Critères
    4. Démarche Suivie
    5. Prédiction

1. Introduction

Ce document présente un aperçu du pipeline de traitement de données utilisé dans le projet de prédiction des tendances électorales en Nouvelle-Aquitaine, ainsi que des informations sur les méthodes de prédiction utilisées.
2. Composantes du Pipeline
2.1. Scripts et Ordre d'Exécution

Le pipeline se compose de plusieurs scripts Python qui doivent être exécutés dans un ordre spécifique pour préparer les données à des analyses avancées. Voici les étapes principales :

    Formattage07121722.py : Prépare les données brutes en corrigeant les formats de date, standardisant les noms de colonnes et supprimant les enregistrements superflus.
    Normalisation.py : Normalise les données pour assurer la cohérence et uniformise les formats.
    Formatting-merge2.py : Fusionne les données de différentes sources pour garantir l'intégrité et la cohérence.
    add_age_vote.py : Enrichit les données avec des informations calculées telles que l'âge basé sur la date de naissance et des catégories de vote.
    Normalisation2.py : Applique une couche supplémentaire de normalisation pour peaufiner les données après les enrichissements et les modifications précédentes.
    region.py : Ajoute la région à tous les départements.

2.2. Objectif du Pipeline

Le but de ce pipeline est de transformer des données brutes en un ensemble structuré, normalisé et enrichi, prêt pour des analyses avancées. En automatisant le processus de nettoyage, de normalisation et d'enrichissement des données, le pipeline vise à améliorer l'efficacité et la précision des analyses ultérieures, tout en réduisant le potentiel d'erreur humaine.
3. Justification du Choix de la Région Géographique et des Critères

La Nouvelle-Aquitaine a été choisie comme région géographique pour ce projet en raison de sa diversité territoriale et de son importance économique. Les critères sélectionnés incluent des données électorales détaillées, des indicateurs socio-économiques tels que le taux de chômage et le PIB, ainsi que des données démographiques telles que la répartition par tranches d'âge. Ces critères ont été choisis pour leur pertinence dans l'analyse des tendances électorales et leur disponibilité dans les sources de données sélectionnées.
4. Démarche Suivie

La démarche suivie dans ce projet comprend plusieurs étapes, notamment la collecte de données à partir de sources gouvernementales et statistiques, le nettoyage et le prétraitement des données à l'aide de scripts Python, et l'exploration des données pour identifier les tendances et les corrélations significatives. Des méthodes et des outils tels que l'analyse de séries temporelles, la modélisation prédictive et l'utilisation de modèles d'IA ont été utilisés pour prédire les tendances électorales futures.
5. Prédiction
IA_predict.py

Ce script utilise des techniques avancées d'analyse de données et de modélisation prédictive pour prédire les tendances politiques dans la région Nouvelle-Aquitaine. Il commence par charger un jeu de données depuis un fichier Excel, puis prévoit les caractéristiques démographiques et économiques futures à l'aide du modèle ARIMA. Les données sont préparées pour la modélisation, les modèles de classification sont configurés et évalués, et les prédictions sont finalement générées pour les années à venir.
Predict_by_llm.py

Ce script analyse les sentiments exprimés dans des articles de journaux sur les élections présidentielles françaises et les classe par tendance politique en utilisant l'API de ChatGPT d'OpenAI et Weaviate. Les résultats sont sauvegardés dans un fichier Excel pour une analyse ultérieure.

Ce README fournit une vue d'ensemble complète du pipeline de traitement des données utilisé dans le projet, ainsi que des informations détaillées sur les méthodes de prédiction implémentées.
