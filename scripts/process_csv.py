```python
import pandas as pd
import os

# Chemin vers le fichier CSV
DATA_PATH = "../data/sample.csv"
REPORT_PATH = "../reports/summary_report.csv"

def main():
    # Lire le fichier CSV
    df = pd.read_csv(DATA_PATH)
    print("Données initiales :")
    print(df.head())

    # Nettoyage : supprimer doublons et lignes avec valeurs manquantes
    df_clean = df.drop_duplicates().dropna()
    print("\nDonnées nettoyées :")
    print(df_clean.head())

    # Générer un rapport simple : statistiques descriptives
    summary = df_clean.describe(include='all')
    print("\nRésumé statistique :")
    print(summary)

    # Sauvegarder le rapport
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    summary.to_csv(REPORT_PATH)
    print(f"\nRapport généré : {REPORT_PATH}")

if __name__ == "__main__":
    main()