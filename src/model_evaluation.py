from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test):
    """Affiche les performances du modèle."""
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    
    print("\n--- RÉSULTATS DE L'ÉVALUATION ---")
    print(f"Précision globale (Accuracy) : {acc:.4f}")
    print("\nRapport détaillé :")
    print(classification_report(y_test, predictions))
    
    return acc
