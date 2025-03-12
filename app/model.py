import pandas as pd
from sklearn.metrics import euclidean_distances
import numpy as np
import requests
import pickle
import os

with open("models/model.pkl", "rb") as file:
    saved_model = pickle.load(file)

with open("models/coordinate_scaler.pkl", "rb") as file:
    saved_coordinate_scaler = pickle.load(file)

with open("models/inference_scaler.pkl", "rb") as file:
    saved_model_scaler = pickle.load(file)

df_clusters = pd.read_pickle("models/coordinates.pkl")
no_of_areas = df_clusters['area_category'].nunique()

def get_latitude_and_longitude(address):
    try:
        base_url = "https://atlas.microsoft.com/search/address/json"
        params = {
                "api-version": "1.0",
                "subscription-key": os.getenv('AZURE_MAPS_API_KEY'),
                "query": address
            }
        return requests.get(base_url, params=params).json()['results'][0]['position']
    except:
        return 
    
def get_area_category(address):
    coordinates = [list(get_latitude_and_longitude(address).values())]
    scaled_coordinates = saved_coordinate_scaler.transform(coordinates)
    closest_index = euclidean_distances(df_clusters[['lat_scaled', 'lon_scaled']], scaled_coordinates).argmin()
    area_category = int(df_clusters.loc[closest_index, 'area_category'])
    return area_category

def predict_price(house_data):

    is_renovated = True if house_data.year_renovated else False

    arr1 = np.array([house_data.bedrooms, house_data.bathrooms, house_data.sqft_living, 
                     house_data.sqft_lot, house_data.floors, house_data.waterfront, house_data.view, 
                     house_data.condition, house_data.sqft_above, house_data.sqft_basement, 
                     house_data.year_built, house_data.year_renovated, is_renovated])

    arr2 = np.zeros(shape=no_of_areas)
    area_category = get_area_category(house_data.location)
    arr2[area_category] = 1
    X_inference = np.expand_dims(np.hstack([arr1, arr2]), axis=0)
    X_inference_scaled = saved_model_scaler.transform(X_inference)
    predicted_price = float(saved_model.predict(X_inference_scaled)[0].round(2))

    return predicted_price