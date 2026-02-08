# Projet d'Ingénierie Logicielle - Prédiction Titanic

## 1. Objectifs du Projet
Ce projet vise à appliquer les bonnes pratiques d'ingénierie logicielle au défi Kaggle "Titanic - Machine Learning from Disaster".
L'objectif principal est de **refactoriser** un notebook d'exploration de données monolithique pour en faire une application Python modulaire, robuste et industrialisée.

Les objectifs spécifiques incluent :
* **Modularité :** Découpage du code en scripts réutilisables (`src/`).
* **Qualité du code :** Respect des normes PEP 8 (via `flake8`) et formatage automatique (`black`).
* **Fiabilité :** Mise en place de tests unitaires automatisés (`pytest`) pour valider le nettoyage des données.
* **Automatisation :** Intégration Continue (CI/CD) via GitHub Actions pour tester le code à chaque modification.
* **Reproductibilité :** Gestion des dépendances via `requirements.txt` et conteneurisation optionnelle via Docker.

## 2. Équipe et Contributions (Groupe 6)
Ce projet a été réalisé en collaboration par les membres suivants :

* **Rayan RAMI** : Architecture du projet, refactoring du code source et pipeline CI/CD.
* **Asaad SAADI** : Développement des scripts d'entraînement du modèle et gestion des données.
* **Aziz DJERBI** : Implémentation des tests unitaires et validation de la qualité du code.
* **Ismael GAHLOUZI** : Documentation, rédaction du rapport et conteneurisation (Docker).

*(Note : La répartition des tâches est indicative d'un travail collaboratif sur l'ensemble du cycle de développement).*

## 3. Structure du Projet
L'architecture respecte les standards de l'industrie :
* `src/` : Code source (Nettoyage, Entraînement, Évaluation, Main).
* `tests/` : Tests unitaires.
* `data/` : Données d'entrée (train.csv, test.csv) et modèles sauvegardés.
* `docs/` : Documentation du projet.
* `.github/workflows/` : Configuration de l'intégration continue.

## 4. Instructions d'Installation
Prérequis : Python 3.8 ou supérieur.

1. **Cloner le dépôt :**
   ```bash
   git clone <URL_DU_DEPOT>
   cd TitanicEngineering
