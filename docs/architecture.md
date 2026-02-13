# Documentation technique (Architecture)

## Vue d’ensemble
Le projet est composé de trois blocs :
1. Modèle ML entraîné (XGBoost + SMOTE) sauvegardé au format .pkl
2. API REST FastAPI qui charge le modèle et expose des endpoints
3. Conteneur Docker pour exécuter l’API de façon portable

## Composants
- src/api.py : application FastAPI (routes /health et /predict)
- models/best_model_xgboost_smote.pkl : modèle entraîné
- Dockerfile : build de l’image de l’API
- requirements.txt : dépendances Python

## Flux de fonctionnement
1. L’API démarre et charge le modèle depuis le dossier models/
2. Un client envoie une requête POST /predict avec les caractéristiques patient
3. L’API convertit les données en DataFrame et calcule :
   - prediction (0/1)
   - probability (score de probabilité)

## Endpoints
- GET /health : vérifie que l’API fonctionne
- POST /predict : retourne une prédiction et une probabilité

## Exécution
- Local : uvicorn src.api:app --reload
- Docker : docker build -t noshow-api . puis docker run -p 8000:8000 noshow-api
