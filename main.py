# main.py
from data_preprocessing import load_and_clean_data
from visualization import plot_genre_distribution, plot_ratings_vs_revenue, plot_top_directors

# Charger et nettoyer les données
file_path = "data/movies.csv"
df = load_and_clean_data(file_path)

# Afficher les graphiques
plot_genre_distribution(df)
plot_ratings_vs_revenue(df)
plot_top_directors(df)
