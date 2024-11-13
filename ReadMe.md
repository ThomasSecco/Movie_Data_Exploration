# 🎬 Movie Data Exploration

Explore the world of movies through data! This project performs **Exploratory Data Analysis (EDA)** and visualization on a public movie dataset to uncover trends, relationships, and insights within the data, such as genre distribution, revenue vs. ratings, and top directors by revenue. 🎥📊

## 📂 Dataset

We use a publicly available movie dataset (e.g., from Kaggle), which includes details like title, genres, budget, revenue, ratings, and release date. Perfect for data enthusiasts looking to dive into the movie industry! 🍿

### 📥 Data Source

To get started, download the `movies.csv` dataset from Kaggle (or any similar dataset with the same structure).

👉 [Movies Dataset on Kaggle](https://www.kaggle.com/datasets/utkarshx27/movies-dataset)

## 🚀 Getting Started

### Installation

1. **Clone the repository** or download the project files.

2. **Install dependencies** by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download the dataset** from Kaggle and place `movies.csv` inside the `data/` folder.

4. **Running the Project:**

   - **Jupyter Notebook**: Open `Data_Exploration.ipynb` in Jupyter Lab/Notebook to interactively explore the data.
   - **Script Mode**: To run the entire analysis as a script, execute:

     ```bash
     python main.py
     ```

## 🛠️ Project Structure

Here are the key scripts in the project:

- **`data_preprocessing.py`**: Handles data loading, cleaning, and feature extraction.
  
- **`visualization.py`**: Contains functions for visualizing:
  - 🎭 Distribution of movie genres
  - 💵 Relationship between movie ratings and revenue
  - 🎬 Top directors by total revenue
  
- **`main.py`**: The main script that brings everything together, running data cleaning and visualization for a full analysis.

## 📊 Visualizations

Dive into insightful visualizations included in this project:

- **📈 Distribution of Movie Genres**: See which genres dominate the dataset.
- **💸 Revenue vs Rating**: Explore the connection between revenue and ratings.
- **🏆 Top 10 Directors by Revenue**: Discover the directors with the highest total revenue.

## 📋 Requirements

Make sure you have these libraries installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

Install everything you need with:

```bash
pip install -r requirements.txt
