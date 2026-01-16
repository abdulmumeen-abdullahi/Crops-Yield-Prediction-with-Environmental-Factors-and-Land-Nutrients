# 🌾 AI-Powered Crop Yield Prediction

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-red.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Hugging Face](https://img.shields.io/badge/Model_Weights-Hugging_Face-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co/VisionaryQuant/Crop_Yield_Prediction/tree/main)

> **Live Demo:** [https://crops-yield-prediction.streamlit.app/](https://crops-yield-prediction.streamlit.app/) </br>
> **Dataset:** [https://www.kaggle.com](https://www.kaggle.com/datasets/madhankumar789/crop-yield-and-environmental-factors-2014-2023)

<div align="center">
  <img width="100%" alt="FarmConsult Dashboard" src="https://github.com/user-attachments/assets/a14b9033-3c50-4e52-befb-0355eae89b3b" />
</div>

## 📋 Project Overview
This project tackles the uncertainty in large-scale farming by developing a machine learning model to predict crop yields based on environmental factors. The final product is a fine-tuned **Random Forest Regressor** with an **MAE of 2.34 tons/ha**, deployed as an interactive Streamlit web application.

This tool empowers farmers to make data-driven decisions, optimizing resource allocation and mitigating financial risks.

## 🚩 Problem Statement
Traditional farming often relies on historical precedent and intuition to forecast crop yields, leaving farmers vulnerable to changing environmental conditions. This uncertainty leads to:
* Inefficient use of fertilizers (Nitrogen).
* Suboptimal planting strategies.
* Financial instability due to unpredictable harvest volumes.

This project solves this by providing reliable yield forecasts for **Corn, Potato, Rice, Sugarcane, and Wheat**.

## 🛠️ Tech Stack & Features

### Core Technologies
* **Language:** `Python 3.9`
* **Machine Learning:** `Scikit-learn` (RandomForestRegressor, RandomizedSearchCV), `XGBoost`
* **Data Processing:** `Pandas`, `NumPy`
* **Visualization:** `Matplotlib`, `Seaborn`

### Deployment & Frontend
* **Web Framework:** `Streamlit`
* **Model Hosting:** `Hugging Face Hub`

### Key Features
* **High-Accuracy Prediction:** A tuned Random Forest model predicts yield in metric tons per hectare (MAE: 2.34).
* **Interactive Web App:** A user-friendly interface for real-time predictions.
* **Multi-Crop Support:** Provides forecasts for five major staple crops.

## ⚙️ Engineering & Data Strategy
*Note: This project emphasizes realistic data constraints over synthetic accuracy.*

### 1. Handling Data Leakage & Multicollinearity
Initial Exploratory Data Analysis (EDA) revealed that the dataset contained synthetic artifacts:
* **The Issue:** Phosphorus (P) and Potassium (K) levels showed a **99% correlation** with Nitrogen (N). Additionally, according to the data description, "Soil Quality" was a derived index that mathematically leaked the yield target.
* **The Solution:** To simulate a real-world production environment—where sensors are costly and noisy, I **dropped P, K, and Soil Quality**.
* **The Result:** The model relies solely on **Nitrogen, Weather Data, and Crop Type**. This reduced the model's complexity and cost of deployment without sacrificing significant accuracy.

### 2. Model Performance
After removing the "cheat" features, the model was trained using **RandomizedSearchCV** for hyperparameter tuning.

| Model | MAE (Tons/Ha) | R² Score | Verdict |
| :--- | :--- | :--- | :--- |
| **Tuned Random Forest** | **2.34** | **0.98** | **Selected** |
| XGBoost | 2.53 | 0.97 | Slightly higher error |
| Linear Regression | 12.77 | 0.62 | Underfitting |
| Baseline Mean | 22.80 | 0.00 | Reference point |

> **Key Metric:** I optimized for **Mean Absolute Error (MAE)** because purely minimizing the average tonnage error (2.34 tons) is more valuable to a farmer's Profit & Loss than maximizing an abstract statistical score like R².

<div align="center">
  <img width="80%" alt="Model Performance Chart" src="https://github.com/user-attachments/assets/32eb22de-637a-4a77-991b-e15185c53617" />
</div>

## 💡 Key Insights from Feature Importance
The new, "clean" model revealed the following drivers of crop yield:
1.  **Temperature:** The single most critical predictor. Accurate, localized weather forecasting is the most valuable data a farmer can have.
2.  **Humidity:** Highlights the critical role of moisture levels in plant transpiration and health.
3.  **Crop Type:** Distinct crops have inherently different yield potentials (e.g., Sugarcane yields are naturally higher in mass than Wheat).
4.  **Nitrogen (N):** The primary soil nutrient driver. By isolating N from P and K, the model confirms that Nitrogen management is the key lever for soil fertility.
5.  
<div align="center">
  <img width="90%" alt="Feature Importance" src="https://github.com/user-attachments/assets/2a76c449-9334-4e2d-82af-6bdfb0091be0" />
</div>

## 🚀 Installation & Usage

### 1. Clone the Repository
- #### Clone the repo
```bash
git clone https://github.com/abdulmumeen-abdullahi/Crops-Yield-Prediction-with-Environmental-Factors-and-Land-Nutrients.git
```
- #### Go to the repo folder
```
cd Crops-Yield-Prediction-with-Environmental-Factors-and-Land-Nutrients
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Download Model Weights
The model file is hosted on Hugging Face to keep the Git repo light. Download crop_yield_best_random_model.pkl and place it in the root directory.
🔗 [Download Weights Here](https://huggingface.co/VisionaryQuant/Crop_Yield_Prediction/tree/main)

### 4. Run the App
```
streamlit run crop_yiled_app.py
```
Navigate to http://localhost:8501 in your web browser.

## ✅ Business Impact
For agribusinesses, this tool translates to:

- Resource Optimization: Reducing fertilizer waste by predicting yield outcomes based on current Nitrogen levels.
- Risk Mitigation: Securing better insurance rates with reliable, data-backed yield forecasts.
- Supply Chain Planning: enhancing storage and distribution logistics with a clearer picture of future supply.
