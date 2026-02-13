# Image Python officielle
FROM python:3.10

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers
COPY requirements.txt .
COPY api.py .
COPY best_model_xgboost_smote.pkl .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 8000

# Lancer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
