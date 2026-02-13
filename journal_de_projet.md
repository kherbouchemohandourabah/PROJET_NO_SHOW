Journal de Projet – Déploiement d’une Solution IA avec Docker 

1.  Objectif du Projet L’objectif est de déployer une solution
    d’intelligence artificielle permettant de prédire l’absentéisme des
    patients à leurs rendez-vous médicaux (“No-Show”).
    Le projet inclut la préparation des données, l’entraînement du
    modèle, la création d’une API avec FastAPI, la conteneurisation avec
    Docker et les tests locaux.

2.  Préparation et Entraînement du Modèle 2.1 Prétraitement des données

-   Nettoyage du dataset (gestion des valeurs incohérentes comme les
    âges négatifs).
-   Normalisation et transformation des colonnes numériques.
-   Encodage des variables catégorielles.
-   Extraction de nouvelles caractéristiques telles que le nombre de
    jours d’attente.

2.2 Gestion du déséquilibre Le dataset initial est fortement
déséquilibré.
La méthode SMOTE a été intégrée au pipeline pour augmenter la classe
minoritaire.

2.3 Modèle retenu XGBoostClassifier intégré dans un pipeline complet : -
ColumnTransformer (StandardScaler + OneHotEncoder) - SMOTE - XGBoost

2.4 Sauvegarde du modèle joblib.dump(best_model,
“best_model_xgboost_smote.pkl”)

3.  Création de l’API (FastAPI) Endpoints :

-   GET /health
-   POST /predict

4.  Mise en place de l’Environnement requirements.txt contient les
    dépendances : fastapi uvicorn scikit-learn==1.6.1 xgboost imblearn
    numpy pandas joblib

5.  Dockerisation Dockerfile utilisé : FROM python:3.10-slim WORKDIR
    /app COPY requirements.txt . RUN pip install –no-cache-dir -r
    requirements.txt COPY . . EXPOSE 8000 CMD [“uvicorn”, “api:app”,
    “–host”, “0.0.0.0”, “–port”, “8000”]

6.  Construction de l’image Docker docker build -t noshow-api .

7.  Exécution du Conteneur docker run -p 8000:8000 noshow-api

8.  Tests Finaux GET /health → {“status”: “API is running”} POST
    /predict → {“prediction”: 0, “probability”: 0.49}

9.  Problèmes Rencontrés et Solutions

-   Conflit de port → arrêter les conteneurs actifs
-   Incompatibilité scikit-learn → fixer la version
-   Erreurs de validation → corriger le JSON

10. Conclusion Le modèle et l’API fonctionnent correctement et la
    solution est entièrement dockerisée.