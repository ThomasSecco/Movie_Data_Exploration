# Movie Data Exploration

This project performs exploratory data analysis (EDA) and visualization on a public movie dataset to understand various trends and relationships within the data, such as the distribution of movie genres, the relationship between revenue and ratings, and the top directors by revenue.

## Dataset

This project uses a publicly available movie dataset (e.g., from Kaggle), which includes information on movies such as their title, genres, budget, revenue, ratings, and release date.

### Data Source

To run this project, you will need the `movies.csv` dataset. You can obtain the dataset from Kaggle (or use any similar dataset with the same structure).

Link to the dataset on Kaggle: [Movies Dataset on Kaggle](https://www.kaggle.com/datasets/utkarshx27/movies-dataset)

## Installation

1. **Clone the repository** or download the files.

2. **Install dependencies** by running the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download the dataset** from Kaggle and place the `movies.csv` file inside the `data/` directory.

4. **Running the Project:**

   - **To run the Jupyter Notebook** and interactively explore the data, open `Data_Exploration.ipynb` in Jupyter Lab/Notebook.
   
   - **To run the entire analysis as a script**, execute the `main.py` script:

     ```bash
     python main.py
     ```

## Scripts

- **`data_preprocessing.py`**: This script handles loading and cleaning the dataset, including handling missing values and extracting relevant features.
  
- **`visualization.py`**: This script contains functions to generate visualizations, such as:
  - Distribution of movie genres
  - Relationship between movie ratings and revenue
  - Top directors by total revenue
  
- **`main.py`**: The main script that combines the functionality of data cleaning and visualization, running the full analysis.

## Visualizations

The following visualizations are included in the analysis:

- **Distribution of Movie Genres**: A bar plot showing the frequency of different genres in the dataset.
- **Revenue vs Rating**: A scatter plot showing the relationship between average movie ratings and revenue.
- **Top 10 Directors by Revenue**: A bar plot showing the top 10 directors based on total movie revenue.

## Requirements

To run this project, the following libraries are required:

- pandas
- numpy
- matplotlib
- seaborn

These dependencies can be installed by running:

```bash
pip install -r requirements.txt 



