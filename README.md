# 🌾 AI-Powered Crop Yield Prediction

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green.svg)](https://pandas.pydata.org/)

This project tackles the uncertainty in large-scale farming by developing a machine learning model to predict crop yields. The final product is a fine-tuned **Random Forest Regressor** with an **R² of 0.98**, deployed as an interactive **Streamlit web application**.

This tool empowers farmers and agricultural stakeholders to make data-driven decisions, optimizing resource allocation and mitigating financial risks.

**🔗 Live Demo:** [**https://crops-yield-prediction.streamlit.app/**](https://crops-yield-prediction.streamlit.app/)

<img width="1366" height="739" alt="445298146-b3e8052d-83d4-4a33-8331-bd758c85e09c" src="https://github.com/user-attachments/assets/a14b9033-3c50-4e52-befb-0355eae89b3b" />
<img width="1366" height="739" alt="445298146-b3e8052d-83d4-4a33-8331-bd758c85e09c" src="https://github.com/user-attachments/assets/f91fb6a4-c3fb-4e35-9fd7-e5c3950fdfcd" />

## 🚩 Problem Statement
Traditional farming often relies on historical precedent and intuition to forecast crop yields, leaving farmers vulnerable to changing environmental conditions. This uncertainty can lead to inefficient use of fertilizers, suboptimal planting strategies, and significant financial losses. This project aims to solve this by providing a reliable, data-driven tool to predict yields for key crops (**Corn, Potato, Rice, Sugarcane, Wheat**) based on environmental and soil data.

## 🛠️ Tech Stack & Features

### Core Technologies:
* `Python`
* `Scikit-learn` for machine learning (RandomForestRegressor, GridSearchCV).
* `Pandas` & `NumPy` for data manipulation.
* `Matplotlib` & `Seaborn` for data visualization.

### Deployment & Frontend:
* `Streamlit` for creating and deploying the interactive web application.

### Key Features:
* **High-Accuracy Prediction:** A tuned Random Forest model predicts yield in metric tons per hectare.
* **Interactive Web App:** A user-friendly interface for real-time predictions.
* **Multi-Crop Support:** Provides forecasts for five major staple crops.

## 🚀 Installation & Usage
To run the Streamlit application locally, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/abdulmumeen-abdullahi/Crops-Yield-Prediction-with-Environmental-Factors-and-Land-Nutrients.git
    cd Crops-Yield-Prediction-with-Environmental-Factors-and-Land-Nutrients
    ```
2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit app:**
    ```bash
    streamlit run crop_yiled_app.py
    ```
    Navigate to `http://localhost:8501` in your web browser.

---

## ⚙️ Methodology & Model Performance
The project followed a structured machine learning workflow:

1.  **Data Preprocessing:** The dataset was cleaned, and categorical features like `Crop_Type` and `Soil_Type` were numerically encoded.
2.  **Model Training & Selection:** Six different regression models were trained and evaluated against a baseline. The **Random Forest Regressor** demonstrated the lowest Mean Absolute Error (MAE) and was selected for further tuning.
3.  **Hyperparameter Tuning:** `GridSearchCV` was used to find the optimal parameters for the Random Forest model, resulting in `max_depth=20` and `n_estimators=1400`.

The final tuned model achieved an **R² of 0.98**, explaining 98% of the variance in crop yield, and an **MAE of 2.40**, representing a **~90% improvement** over the baseline model.

<img width="1189" height="590" alt="484682968-d96f9436-c3ec-4f03-b822-562c55c4f444" src="https://github.com/user-attachments/assets/32eb22de-637a-4a77-991b-e15185c53617" />

| Model                     | Mean Absolute Error (MAE) | R² Score |
| :------------------------ | :------------------------ | :------- |
| Baseline                  | 22.80                     | 0.00     |
| **Tuned Random Forest** | **2.40** | **0.98** |
| XGBoost Regressor         | 2.53                      | 0.97     |
| K-Neighbors Regressor     | 2.70                      | 0.97     |
| Decision Tree Regressor   | 3.16                      | 0.96     |
| Linear Regression         | 12.77                     | 0.62     |
| Support Vector Regressor  | 15.96                     | 0.41     |

## 💡 Key Insights from Feature Importance
The feature importance analysis revealed the most influential factors in predicting crop yield:

1.  **Temperature:** This was the single most critical predictor. It underscores that accurate, localized weather forecasting is the most valuable data a farmer can have for yield estimation.
2.  **Humidity:** As the second most important feature, it highlights the critical role of moisture levels in plant growth and health.
3.  **Crop Type:** Different crops have inherently different yield potentials and sensitivities to environmental conditions, making this a key distinguishing feature.
4.  **Soil Quality:** A direct measure of the soil's health and fertility, this feature is a fundamental driver of a successful harvest.

<img width="1366" height="655" alt="484700945-ac48554e-2ea1-41fe-874a-b2f3e26b0262" src="https://github.com/user-attachments/assets/2a76c449-9334-4e2d-82af-6bdfb0091be0" />

## ✅ Conclusion & Business Impact
This project successfully demonstrates the power of machine learning to bring precision and predictability to agriculture.

For farmers and agribusinesses, this tool can:
* **Optimize Resource Planning:** Make informed decisions about fertilizer, water, and labor allocation.
* **Mitigate Financial Risk:** Secure better financing and insurance with reliable yield forecasts.
* **Enhance Market Strategy:** Plan for storage and distribution with a clearer picture of future supply.
* **Promote Sustainable Farming:** Reduce waste and environmental impact by aligning inputs with predicted needs.
