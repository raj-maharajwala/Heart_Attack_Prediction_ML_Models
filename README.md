# Hearth Attack Prediction using ML Models | Logistic Regression, SVM, Decision Trees, Random Forest, and XGBoost

This is an interactive Machine Learning web application called "ML in Healthcare" developed using Python and Streamlit. The application utilizes various ML algorithms, including XGBoost, Random Forest, SVM, Logistic Regression, and Decision Trees, to create accurate models for predicting the risk of a user having a heart attack based on specific attributes such as age, sex, heart rate, blood sugar, and more.

![StreamLit App](https://static.streamlit.io/badges/streamlit_badge_white.svg)

The application builds five different models using different ML algorithms. The models are:
'''
XGBoost
Random Forest
Support Vector Machines (SVM)
Logistic Regression
Decision Trees
'''

Inside the "Notebook" folder of the ML in Healthcare application, there is a file named "Heart_Attack_Prediction_ML.ipynb". This notebook covers the modeling process for all five models, namely XGBoost, Random Forest, SVM, Logistic Regression, and Decision Trees.

The notebook provides a comprehensive guide on how to train and evaluate these models using a heart attack dataset. Additionally, it includes the use of GridSearchCV and RandomizedSearchCV, which are techniques for hyperparameter tuning. These techniques help to find the best combination of hyperparameters for each model, optimizing their performance.

By leveraging GridSearchCV and RandomizedSearchCV, the notebook demonstrates how to systematically search through different hyperparameter values to identify the optimal configuration that maximizes the models' predictive capabilities.

This comprehensive notebook serves as a valuable resource for understanding the model building process and implementing hyperparameter tuning to enhance the performance of the ML models in predicting the risk of heart attacks.
These models are trained on a dataset containing relevant attributes, and their purpose is to predict the risk of a heart attack for a given user based on their input. 

<hr>
This application aims to provide a user-friendly and informative interface for predicting heart attack risk using machine learning.

The models used in this project are trained using data from the UCI Machine Learning Repository, specifically the Heart Attack Prediction dataset. You can find the dataset here.

The project includes an interactive side-dashboard created using the st.sidebar function from the Streamlit library. This dashboard allows the user to perform the following actions:

Choose an algorithm: The user can select from the following algorithms: Logistic Regression, SVM, Decision Trees, Random Forest, and XGBoost.

Adjust model parameters: The user can modify important parameters for each selected model. These parameters might include learning rate, random state, regularization coefficient, gamma, kernel, and n_estimators, among others.

Once the user has made their selections and adjusted the parameters, the tuned model is built and ready to be tested on the provided testing data. The project displays a classification plot and a confusion matrix for the selected model, along with various model evaluation metrics such as accuracy, precision, recall, F1-score, mean squared error, and execution time. The plots and metrics are updated in real-time as the user modifies the model parameters.

This interactive dashboard provides a great way to explore and understand different machine learning algorithms, as well as observe how they are influenced by tuning their hyperparameters.

> 
![image](https://user-images.githubusercontent.com/72503778/123002403-85b73700-d3cf-11eb-80a1-71262561b9c8.png)

<hr>
