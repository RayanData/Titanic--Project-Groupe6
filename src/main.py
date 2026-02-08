import os
import sys
from sklearn.model_selection import train_test_split

# Import des modules locaux
# On ajoute le dossier courant au path pour être sûr de trouver les modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_preprocessing import load_data, preprocess_data
from model_training import train_model, save_model
from model_evaluation import evaluate_model

def main():
    # --- GESTION DES CHEMINS (PORTABILITÉ MAXIMALE) ---
    # On récupère le dossier où se trouve ce fichier main.py (c'est src/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # On remonte d'un cran pour trouver la racine du projet
    root_dir = os.path.dirname(current_dir)
    
    # On construit les chemins vers data de manière dynamique
    TRAIN_PATH = os.path.join(root_dir, 'data', 'train.csv')
    MODEL_PATH = os.path.join(root_dir, 'data', 'model.pkl')

    print(f"📂 Répertoire de travail détecté : {root_dir}")
    
    # --- ÉTAPE 1 : CHARGEMENT ---
    print("1️⃣  Chargement des données...")
    if not os.path.exists(TRAIN_PATH):
        print(f"\n❌ ERREUR : Fichier introuvable : {TRAIN_PATH}")
        print("👉 SOLUTION : Glissez le fichier 'train.csv' dans le dossier 'data'.")
        sys.exit(1)
        
    df = load_data(TRAIN_PATH)

    # --- ÉTAPE 2 : NETTOYAGE ---
    print("2️⃣  Nettoyage des données...")
    df_clean = preprocess_data(df)
    
    # Séparation Features (X) / Cible (y)
    X = df_clean.drop('Survived', axis=1)
    y = df_clean['Survived']

    # Séparation Entraînement / Test (80% / 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- ÉTAPE 3 : ENTRAÎNEMENT ---
    print("3️⃣  Entraînement du modèle Random Forest...")
    model = train_model(X_train, y_train)
    save_model(model, MODEL_PATH)

    # --- ÉTAPE 4 : ÉVALUATION ---
    print("4️⃣  Évaluation des performances...")
    evaluate_model(model, X_test, y_test)
    
    print("\n✅ PROCESSUS TERMINÉ AVEC SUCCÈS.")

if __name__ == "__main__":
    main()
