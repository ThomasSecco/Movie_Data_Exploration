# visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_genre_distribution(df):
    # Compter les genres (chaque film peut avoir plusieurs genres)
    genres = df['genres'].dropna().str.get_dummies(sep='|').sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=genres.values, y=genres.index)
    plt.title('Distribution des genres de films')
    plt.xlabel('Nombre de films')
    plt.ylabel('Genre')
    plt.show()

def plot_ratings_vs_revenue(df):
    # Graphique de la relation entre les notes et les revenus
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='vote_average', y='revenue', data=df, alpha=0.5)
    plt.title('Relation entre la note moyenne et les revenus')
    plt.xlabel('Note moyenne')
    plt.ylabel('Revenus')
    plt.show()

def plot_top_directors(df):
    # Calculer les revenus totaux pour chaque réalisateur
    top_directors = df.groupby('director')['revenue'].sum().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_directors.values, y=top_directors.index)
    plt.title('Top 10 des réalisateurs par revenus générés')
    plt.xlabel('Revenus (en milliards)')
    plt.ylabel('Réalisateur')
    plt.show()
