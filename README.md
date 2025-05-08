# Crops Yield Prediction with Environmental Factors and Land Nutrients

## 🔹 Problem Statement
Large-scale farming involves significant risk—especially when relying on traditional weather forecasting to estimate yields. Inaccuracy in these forecasts often leads to stress, loss, and reduced efficiency. <br/>
This project aims to empower farmers, agropreneurs, and agro-investors by: <br/>
- Training a machine learning model to predict crop yields based on farmer inputs.
- Deploying the model into an interactive web application.
- Integrating a smart recommendation system that provides actionable insights. <br/>
This contributes to achieving the UN Sustainable Development Goals (SDGs) by supporting sustainable agriculture, food security, and climate resilience.

## 🔹 Dataset Overview
- Source: [Crop Yield and Environmental Factors 2014–2023 - Kaggle](https://www.kaggle.com/datasets/madhankumar789/crop-yield-and-environmental-factors-2014-2023)
- Size: 36,520 observations
- Features: 12

## 🔹 Methodology
### 1. Data Preprocessing
- Loaded data into Pandas, dropped country_code.

Filtered for specific crops: Wheat, Sugarcane, Corn, Rice, Potato.

Dropped Date (for non-time-series models).

Encoded categorical variables like Crop_Type and Soil_Type.

2. Exploratory Data Analysis (EDA)
📌 [Insert Visualizations Here: Boxplots, Heatmaps, Bar/Line Charts, Scatter Plots]

Analyzed distribution, trends, and outliers.

Heatmaps revealed strong correlation between Temperature, Soil_pH, and Crop_Yield.

Bar/line plots showed seasonal and soil type trends.

3. Model Training
Split data into 80% training and 20% testing.

Created a baseline model using the average yield (22.8 metric tons/hectare).

4. Model Evaluation
Tested six algorithms:

✅ Random Forest Regressor (Best performance)

Linear Regression

KNeighbors Regressor

Support Vector Regressor

Decision Tree Regressor

XGBoost Regressor

Performance Metrics (MAE):

Model	MAE (Metric Tons/Ha)
Random Forest Regressor	2.4 ✅
XGBoost Regressor	2.5
Decision Tree Regressor	3.2
KNeighbors Regressor	2.7
Linear Regression	12.8
SVR	16.0

🔍 Hyperparameter tuning using GridSearchCV further optimized the Random Forest model.

5. Model Results
R² Score: 98%

RMSE: 4.13

MAE: 2.4
✅ This is ~90% better than the baseline.

6. Feature Importance
📌 [Insert Feature Importance Bar Chart Here]
Top Predictive Features:

Temperature 🌡️

Soil pH

Humidity 💧

N (Nitrogen)

P (Phosphorus)

Soil Quality

K (Potassium)

🧠 How the Model Can Help
Accurate crop yield forecasts to plan storage, transportation, and sales.

Smart recommendations for nutrient management.

Informed decision-making for investment in land and resources.

👨‍💻 Author
Abdullahi Olalekan Abdulmumeen
Data Scientist
📧 olalekanabdulmumeen3@gmail.com
📱 +234 705 305 3024
