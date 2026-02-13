Déploiement d’une API IA – Projet No-Show
1. Contexte du projet

Ce projet vise à prédire si un patient sera absent (« No-Show ») à un rendez-vous médical.
Les rendez-vous manqués représentent un enjeu important pour les établissements de santé, entraînant des pertes financières, une mauvaise gestion des ressources et une désorganisation des plannings.

Le dataset utilisé provient d’une clinique au Brésil et est disponible publiquement sur Kaggle.

Ce projet a été réalisé dans le cadre du module :
Déploiement d’une solution IA.

2. Objectifs

Développer un modèle de classification robuste pour prédire les absences.

Gérer le déséquilibre des classes à l’aide de SMOTE.

Mettre en place un suivi expérimental avec MLflow.

Déployer une API REST professionnelle avec FastAPI.

Conteneuriser l’application avec Docker.

Structurer le dépôt GitHub selon des standards professionnels.

3. Méthodologie
3.1 Préparation des données

Nettoyage des données

Création de nouvelles variables (waiting_days, weekdays)

Encodage des variables catégorielles

Gestion du déséquilibre des classes avec SMOTE

3.2 Modélisation

Algorithme utilisé : XGBoost Classifier

Optimisation des performances

Évaluation via F1-score, matrice de confusion et probabilités de prédiction

Le modèle final est sauvegardé dans :

models/best_model_xgboost_smote.pkl

3.3 Déploiement

Développement d’une API REST avec FastAPI

Documentation automatique via Swagger

Conteneurisation avec Docker pour un déploiement portable

4. Structure du projet
PROJET_NO_SHOW/
│
├── src/                      # Code source de l’API
│   └── api.py
├── models/                   # Modèle entraîné
│   └── best_model_xgboost_smote.pkl
├── docs/                     # Documentation et captures
├── portfolio/                # Intégration portfolio
├── Dockerfile
├── requirements.txt
├── journal_de_projet.md
└── README.md

5. Installation locale (sans Docker)

Créer un environnement virtuel

python -m venv venv
venv\Scripts\activate       # Windows


Installer les dépendances

pip install -r requirements.txt


Lancer l’API

uvicorn src.api:app --reload


L’API sera disponible à l’adresse suivante :
http://127.0.0.1:8000/docs

6. Construction et exécution avec Docker

Construire l’image :

docker build -t noshow-api .


Lancer le conteneur :

docker run -p 8000:8000 noshow-api


Accéder à la documentation interactive :
http://127.0.0.1:8000/docs

7. Endpoints disponibles
GET /health

Permet de vérifier si l’API fonctionne correctement.

Réponse attendue :

{"status": "API is running"}

POST /predict

Retourne une prédiction ainsi qu’une probabilité à partir des caractéristiques d’entrée du patient.

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

8. Rôle et responsabilités

Projet réalisé individuellement.

Rôles assumés :

Chef de projet

Data Scientist

Machine Learning Engineer

MLOps Engineer

Responsable documentation et gestion des versions

9. Compétences démontrées

Pipeline Machine Learning complet

Gestion du déséquilibre des classes

Expérimentation et suivi avec MLflow

Déploiement d’API REST

Conteneurisation Docker

Structuration professionnelle d’un dépôt Git

Gestion rigoureuse des versions

10. Licence

Ce projet est fourni à titre académique dans le cadre d’un exercice éducatif.