Déploiement d’une API IA – Projet No-Show

1. Description du Projet

Cette application permet de prédire si un patient sera présent ou absent
à son rendez-vous médical (« No-Show »).
Le modèle utilisé est un pipeline complet composé de prétraitement,
SMOTE et XGBoost, sauvegardé dans best_model_xgboost_smote.pkl.

L’API est développée avec FastAPI et conteneurisée avec Docker.

------------------------------------------------------------------------

2. Structure du Projet

    mon_projet_IA/
    │── api.py
    │── best_model_xgboost_smote.pkl
    │── requirements.txt
    │── Dockerfile
    │── .dockerignore
    │── journal_de_projet.md

------------------------------------------------------------------------

3. Installation Locale (Sans Docker)

1) Créer un environnement virtuel

    python -m venv venv
    source venv/bin/activate      # Linux / Mac
    venv\Scripts\activate       # Windows

2) Installer les dépendances

    pip install -r requirements.txt

3) Lancer l’API

    uvicorn api:app --reload

L’API sera disponible :
http://127.0.0.1:8000/docs

------------------------------------------------------------------------

4. Construction et Exécution Docker

Construire l’image

    docker build -t noshow-api .

Lancer le conteneur

    docker run -p 8000:8000 noshow-api

Accéder à la documentation interactive :
http://127.0.0.1:8000/docs

------------------------------------------------------------------------

5. Endpoints Disponibles

1) GET /health

Permet de vérifier si l’API fonctionne correctement.

Réponse attendue :

    {"status": "API is running"}

2) POST /predict

Fournit une prédiction à partir des 11 caractéristiques d’entrée.

Exemple JSON :

    {
      "Age": 25,
      "Scholarship": 0,
      "Hipertension": 1,
      "Diabetes": 0,
      "Alcoholism": 0,
      "Handcap": 1,
      "SMS_received": 0,
      "waiting_days": 3,
      "Gender": "M",
      "Neighbourhood": "JARDIM DA PENHA",
      "scheduled_weekday": "Monday",
      "appointment_weekday": "Tuesday"
    }

------------------------------------------------------------------------

6. Auteur

Projet réalisé par Mohand Kherbouche Ourabah
Dans le cadre du module : Déploiement d’une solution IA

------------------------------------------------------------------------

7. Licence

Ce projet est fourni à titre académique dans le cadre d’un exercice
éducatif.
