# Crops Yield Prediction with Environmental Factors and Land Nutrients

## 🔹 Problem Statement
Large-scale farming is full of uncertainty. Traditional methods of forecasting crop yield often rely on intuition or limited weather predictions, leading to inefficiencies, wasted resources, and financial risks. <br/>
This project leverages machine learning to: <br/>
- Predict crop yields based on environmental factors and soil nutrients.
- Deploying the model into an interactive web application.
- Support the UN Sustainable Development Goals (SDGs) by advancing sustainable agriculture, food security, and climate resilience.

## 🔹 Dataset Overview
- Source: [Crop Yield and Environmental Factors 2014–2023 - Kaggle](https://www.kaggle.com/datasets/madhankumar789/crop-yield-and-environmental-factors-2014-2023)
- Size: 36,520 observations
- Features: 12 (environmental + soil + crop attributes) <br/>
Crops considered: Wheat, Sugarcane, Corn, Rice, Potato

<img width="1366" height="497" alt="Screenshot (199)" src="https://github.com/user-attachments/assets/15e36f0d-e14f-4792-8adf-2bf48f1b6a18" />

## 🔹 Methodology
### 1. Data Preprocessing
- Dropped irrelevant features.
- Encoded categorical variables (Crop_Type, Soil_Type).
- Filtered dataset to focus on key crops.

### 2. Exploratory Data Analysis (EDA)
- #### Analyzed outliers.
![download](https://github.com/user-attachments/assets/16e96c17-cebf-4d89-8c8c-8fb20806b6ce)
![download](https://github.com/user-attachments/assets/52bc7328-4370-4ef1-abce-a862293630e4)

- #### Correlation Heatmap to display correlation between features.
![download](https://github.com/user-attachments/assets/cc92f92d-941d-4119-b76b-6987fa8c3ba8)

### 3. Model Training
- Split data into 80% training and 20% testing.
- Created a baseline model using the average yield (22.8 metric tons/hectare).

### 4. Model Evaluation
- #### Tested six algorithms:
   - Random Forest Regressor (Best performance)
   - Linear Regression
   - KNeighbors Regressor
   - Support Vector Regressor
   - Decision Tree Regressor
   - XGBoost Regressor

- #### Performance Metrics - Mean ABsolute Error (MAE), Mean Squared Error (MSE), Coefficient of Determination (R²) <br/>
| Model             | MAE   | R²    | MSE    |
| ----------------- | ----- | ----- | ------ |
| **Random Forest** | 2.41  | 0.975 | 17.22  |
| XGBoost           | 2.53  | 0.098 | 17.14  |
| Decision Tree     | 3.16  | 0.956 | 30.18  |
| KNeighbors        | 2.70  | 0.413 | 405.83 |
| Linear Regression | 12.77 | 0.615 | 266.41 |
| Support Vector    | 15.96 | 0.413 | 405.83 |
| **Baseline**      | 22.76 | 0.000 | 704.31 |

<img width="1189" height="590" alt="download" src="https://github.com/user-attachments/assets/d96f9436-c3ec-4f03-b822-562c55c4f444" />

- #### Hyperparameter tuning using GridSearchCV further optimized the Random Forest model.

### 5. Best Model Results
- R² : 0.98
- MSE: 4.00
- MAE: 2.33 <br/>
This is ~90% better than the baseline. <br/>

### 6. Feature Importance - Top Predictive Features:
    - Temperature
    - Humidity
    - Crop Type
    - Soil Quality
    
<img width="1366" height="655" alt="Screenshot (200)" src="https://github.com/user-attachments/assets/ac48554e-2ea1-41fe-874a-b2f3e26b0262" />

### 7. Model Deployment
![Screenshot (137)](https://github.com/user-attachments/assets/b1bbab1b-cfe9-47ce-9e5e-826f86a97125)
![Screenshot (138)](https://github.com/user-attachments/assets/b3e8052d-83d4-4a33-8331-bd758c85e09c)

The trained Random Forest model was deployed using Streamlit. The app allows users to input environmental and soil parameters to receive real-time crop yield predictions. <br/>
🔗 [Access the App](https://crops-yield-prediction.streamlit.app/)

## Impact
- Accurate forecasts help optimize storage, logistics, and market planning.
- Smart nutrient management improves soil health and long-term yield.
- Supports data-driven decision-making for sustainable agriculture.

=================================== <br/>
Abdullahi Olalekan Abdulmumeen <br/>
ML Engineer (in training)  || Data Science | Computer Vision | AI Agent <br/>
olalekanabdulmumeen3@gmail.com <br/>
+234 705 305 3024 <br/>
