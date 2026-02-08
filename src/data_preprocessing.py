import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(filepath):
    """Charge un fichier CSV de manière sécurisée."""
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"ERREUR CRITIQUE: Le fichier '{filepath}' est introuvable.")

def preprocess_data(df):
    """
    Nettoie les données pour qu'elles soient digérables par le modèle.
    Gère les valeurs manquantes et transforme le texte en nombres.
    """
    df = df.copy()
    
    # 1. Gestion des valeurs manquantes (Stratégie simple et robuste)
    # Pour l'âge, on met la médiane pour ne pas fausser la distribution
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())
    
    # Pour le port d'embarquement, on met le plus fréquent
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
        
    # Pour le prix, la médiane
    if 'Fare' in df.columns:
        df['Fare'] = df['Fare'].fillna(df['Fare'].median())

    # 2. Suppression des colonnes trop compliquées ou inutiles
    colonnes_inutiles = ['Cabin', 'Name', 'Ticket', 'PassengerId']
    df = df.drop(columns=[c for c in colonnes_inutiles if c in df.columns])

    # 3. Encodage (Texte -> Nombres)
    le = LabelEncoder()
    cols_texte = ['Sex', 'Embarked']
    for col in cols_texte:
        if col in df.columns:
            df[col] = le.fit_transform(df[col].astype(str))
            
    return df
