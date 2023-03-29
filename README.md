![GitHub](https://img.shields.io/github/license/JonysArcanjo/Predict-house-price)
# Predict House Price

![Design sem nome (3)](https://user-images.githubusercontent.com/48812740/228647953-7479dbc2-c903-4d6c-ba39-5029fd56248a.png)




### Welcome to this Data Science project!

The objective of this project is to predict house prices using machine learning techniques. To achieve this, I performed a brief exploratory data analysis and directed the study to evaluate the Boruta feature selection technique, comparing its performance with the neural network both with and without the use of this technique.

## About Dataset

The dataset used contains house sale prices for King County, which includes Seattle, and it includes homes sold between May 2014 and May 2015.

Dataset source: [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)

## Libraries Used

- Tensorflow
- Pandas
- Numpy
- Matplotlib
- Boruta (for feature selection)
- Gradio - user interface (ux)

## Metrics Used

The following metrics were used to assess the performance of the models:

- RMSE: Root Mean Squared Error
- MSE: Mean Squared Error
- MAE: Mean Absolute Error
- R2: The determination coefficient
- Adjusted R2

## Application in PRD

![APP_predicit_house_price-min (1)](https://user-images.githubusercontent.com/48812740/228641695-e94dc66e-eea1-4aa7-bb3b-d97d57fe0dfa.gif)

## Conclusion

The results of this project indicate that the model that uses all resources performed better than the model that used the Boruta feature selection technique. However, when choosing the best model for a specific application, it is important to consider not only the performance but also the computational cost and the efficiency in the selection of resources. For future versions of this model, it would be interesting to explore other feature selection and feature engineering techniques.

## License

This project is licensed under the MIT License.
