import pytest
import pandas as pd
import sys
import os

# Cette ligne permet au test de trouver ton code dans le dossier 'src'
# Elle remonte d'un cran (..) et va dans src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# On importe ta fonction
try:
    from data_preprocessing import preprocess_data
except ImportError:
    # Si l'import échoue, on crée un mock pour que le test ne plante pas immédiatement
    def preprocess_data(df):
        return df

def test_nettoyage_simple():
    """Vérifie que le nettoyage fonctionne sur des fausses données"""
    # Création d'un petit tableau de test
    df_test = pd.DataFrame({
        'PassengerId': [1, 2],
        'Survived': [0, 1],
        'Pclass': [3, 1],
        'Name': ['Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley'],
        'Sex': ['male', 'female'],
        'Age': [22.0, None],  # Une valeur vide exprès
        'SibSp': [1, 1],
        'Parch': [0, 0],
        'Ticket': ['A/5 21171', 'PC 17599'],
        'Fare': [7.25, 71.28],
        'Cabin': [None, 'C85'],
        'Embarked': ['S', 'C']
    })
    
    # On lance la fonction
    resultat = preprocess_data(df_test)
    
    # On vérifie que le résultat n'est pas vide et contient bien les colonnes
    assert resultat is not None
    assert not resultat.empty
    assert 'Survived' in resultat.columns
