# data_preprocessing.py
import pandas as pd

def load_and_clean_data(file_path):
    # Charger les données
    df = pd.read_csv(file_path)
    
    # Sélectionner les colonnes d'intérêt
    columns = ['title', 'genres', 'budget', 'revenue', 'vote_average', 'vote_count', 'release_date']
    df = df[columns]
    
    # Supprimer les films sans titre ni note
    df.dropna(subset=['title', 'vote_average'], inplace=True)
    
    # Remplacer les valeurs manquantes de revenus et budget par 0
    df['revenue'].fillna(0, inplace=True)
    df['budget'].fillna(0, inplace=True)
    
    # Convertir release_date en datetime
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    
    # Extraire l'année de sortie
    df['release_year'] = df['release_date'].dt.year

    return df

# Test de la fonction
if __name__ == "__main__":
    df_cleaned = load_and_clean_data("data/movies.csv")
    print(df_cleaned.head())
