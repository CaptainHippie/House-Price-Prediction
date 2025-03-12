# House Price Prediction
 
🚀 **Live Demo:** [House Price Prediction App](https://house-price-prediction-4im0.onrender.com/)  

## Overview
A machine learning model to predict house prices based on various attributes. Built with **FastAPI**, trained with **GradientBoostingRegressor**, and deployed on **Render**.

## Model Performance
- **R² Score**: *75.88%*  
- **Mean Absolute Error**: *72648*, which is *35.08%* of standard deviation
- **Mean Squared Error**: *10919533397*  

## Run Locally
🔹 **Prerequisites:** Python installed\
🔹 **Install Dependencies:**

```sh
pip install -r requirements.txt
```
🔹 **Set Environment Variable:** (Required for location processing)

```sh
export AZURE_MAPS_API_KEY=your_api_key_here  # For Windows use 'set' instead of 'export'
```

🔹 **Run the API:**
```sh
uvicorn app.main:app --reload
```

## API Usage
- **Endpoint:** `POST /predict`
- **Input (JSON):**

```json
{
  "bedrooms": int,
  "bathrooms": int,
  "sqft_living": float,
  "sqft_lot": float,
  "sqft_above": float,
  "sqft_basement": float,
  "floors": int,
  "waterfront": bool,
  "view": int,
  "condition": int,
  "year_built": int,
  "year_renovated": int,
  "location": string
}
```

- **Output (JSON):**
```json
{
  "predicted_price": float
}
```

## Features
✅ Data preprocessing (scaling, encoding, outlier removal)  
✅ Gradient Boosting Regressor with hyperparameter tuning  
✅ FastAPI backend with Pydantic validation  
✅ Interactive web UI  
✅ Deployed on Render  

## Repository Contents
- `main.py` → FastAPI app
- `notebook.ipynb` → Model training steps
- `models/model.pkl` → Trained model
- `requirements.txt` → Dependencies
- `Final report.pdf` → The Project Report and Documentation
- `datasets/` → Datasets that were used and exported
- `model.py` → The functions used for inference
- `schemas.py` → The pydantic model schemas
- `models/` → Exported models and scalers
- `templates/index.html` → The landing page
- `static/` → Frontend stylesheets and scripts
- `README.md` → This file

## Notes
- Running locally requires an **Azure Maps API key** as an env variable: `AZURE_MAPS_API_KEY`.
- Hosted version **does not require an API key**.
