# Intro to ML - Tic-Tac-Toe Analysis

This repository contains the code for a machine learning project focused on building and evaluating various models on a tic-tac-toe dataset. The project involves implementing classifiers and regressors using libraries such as `pandas`, `numpy`, and `scikit-learn`, and demonstrates how these models can be used to predict optimal moves in a tic-tac-toe game.

## Table of Contents
- [Overview](#overview)
- [Implementation Details](#implementation-details)
- [Evaluation Results](#evaluation-results)
- [How to Run the Code](#how-to-run-the-code)
- [Known Issues](#known-issues)
- [License](#license)

## Overview

This project implements several machine learning models to classify and predict outcomes in a tic-tac-toe game. The dataset includes final board states, optimal single moves, and optimal multiple moves. The models are evaluated based on their accuracy and root mean square error (RMSE).

## Implementation Details

The code is implemented in a Jupyter notebook and includes the following steps:
1. **Data Import and Processing**: Using `pandas` and `numpy` to handle the tic-tac-toe data.
2. **Model Building**: Implementing and training the following models:
   - Classifiers: Linear SVM, K-Nearest Neighbors (KNN), and Multilayer Perceptron (MLP).
   - Regressors: KNN, MLP, and Linear Regression.
3. **Model Evaluation**: Evaluating the models using metrics such as accuracy and RMSE.
4. **Saving Models**: Using the `joblib` library to save the trained regression models for use in a command line tic-tac-toe game.

## Evaluation Results

### Classifiers
- **MLP**: 
  - Accuracy: 98% (final board state data), 92% (single move data)
- **KNN**: 
  - Accuracy: ~100% (final board state data), 85% (single move data)
- **SVM**: 
  - Accuracy: 99% (final board state data), 82% (single move data)

### Regressors
- **MLP**: 
  - Accuracy: 83%, RMSE: 0.1654
- **KNN**: 
  - Accuracy: 71%, RMSE: 0.2699
- **Linear Regression**: 
  - Accuracy: 0%, RMSE: 0.4587

Due to computational limitations, the MLP model was limited to 1000 iterations, which might impact its performance.

## How to Run the Code

To run the code, ensure you have Python installed along with the necessary libraries. Follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/intro-to-ml-tictactoe.git
    cd intro-to-ml-tictactoe
    ```

2. Install the required libraries:
    ```bash
    pip install pandas numpy scikit-learn matplotlib jupyter
    ```

3. Open the Jupyter notebook:
    ```bash
    jupyter notebook
    ```

4. Run the cells in the notebook to train and evaluate the models.

## Known Issues

- The multi-output linear regression model currently has an accuracy of zero. Despite various attempts to resolve this, the issue persists.
- Due to computational limitations, the number of iterations for the MLP model is restricted, potentially affecting its performance.
