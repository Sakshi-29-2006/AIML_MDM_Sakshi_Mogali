# Regression Model Performance Evaluation

## Practical Assignment – 03

This project implements regression models to predict **Rented Bike Count** using the Seoul Bike Sharing dataset.

### Models Implemented

- Simple Linear Regression
- Multiple Linear Regression
- Polynomial Regression
- Linear Regression using Gradient Descent

### Dataset

The **Seoul Bike Sharing Dataset** contains hourly bike rental data along with environmental and time-related features such as temperature, humidity, wind speed, rainfall, snowfall, season, holiday, and functioning day.

### Data Preprocessing

- Dataset inspection and cleaning
- Missing value analysis
- Exploratory data analysis
- Feature selection
- One-hot encoding of categorical variables
- Train-test split
- Feature scaling for Gradient Descent

### Performance Metrics

The models are evaluated using:

- MAE – Mean Absolute Error
- MSE – Mean Squared Error
- RMSE – Root Mean Squared Error
- R² Score

### Gradient Descent

Gradient Descent is implemented from scratch for Linear Regression. The loss function, derivatives, parameter updates, and effect of different learning rates are analyzed using convergence graphs.

### Project Structure

```text
Regression-Model-Performance-Evaluation/
│
├── data/
│   └── Seoul Bike Sharing Dataset
├── Results/
├── GradientDescent.ipynb
├── RegressionModel.ipynb
└── README.md

