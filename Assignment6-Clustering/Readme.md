
# Crime Hotspot Identification Using Clustering Algorithms

## Overview
This project identifies potential crime hotspots in Chicago using crime data from 2022 and unsupervised machine learning clustering algorithms.

## Objectives
- Preprocess crime data and geographical coordinates.
- Apply and compare clustering algorithms.
- Visualize crime clusters and identify areas with higher incident counts.

## Dataset
- **Dataset:** Chicago Crime Prediction Dataset
- **Year:** 2022
- **Features:** Geographical coordinates (X, Y) and crime type.

## Technologies Used
- **Language:** Python
- **Platform:** Google Colab
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SciPy

## Algorithms Used
- K-Means
- Agglomerative Clustering
- Divisive Clustering (Bisecting K-Means)
- DBSCAN

## Methodology
1. Load and preprocess the dataset.
2. Filter records for 2022 and remove invalid coordinates.
3. Sample and standardize geographical coordinates.
4. Apply the four clustering algorithms.
5. Visualize and evaluate the clusters.
6. Analyze and rank K-Means clusters by crime incident count.

## Evaluation Metrics
- **Silhouette Score:** Higher values generally indicate better-defined clusters.
- **Davies-Bouldin Index:** Lower values generally indicate better-separated clusters.

## Results
K-Means achieved the highest Silhouette Score (0.4041) among the evaluated algorithms. Cluster visualizations, evaluation metrics, crime counts, and crime-type summaries are generated in the notebook.

## How to Run
1. Open [Google Colab](https://colab.research.google.com/).
2. Upload `Clustering (1).ipynb`.
3. Upload the dataset `Crime Prediction in Chicago_Dataset.csv`.
4. Ensure the dataset path is correct.
5. Run all notebook cells sequentially.

## Conclusion
The project demonstrates how clustering algorithms can reveal spatial patterns in crime data and help identify potential crime concentration areas.
