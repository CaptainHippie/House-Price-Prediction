from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Optional

from schemas import HousePredictionInput
from model import predict_price

app = FastAPI(title="House Price Prediction")

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page with the prediction form."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict(
    bedrooms: int = Form(...),
    bathrooms: int = Form(...),
    sqft_living: float = Form(...),
    sqft_lot: float = Form(...),
    sqft_above: float = Form(...),
    sqft_basement: float = Form(...),
    floors: int = Form(...),
    waterfront: bool = Form(False),
    view: int = Form(...),
    condition: int = Form(...),
    year_built: int = Form(...),
    year_renovated: Optional[int] = Form(None),
    location: str = Form(...)
):
    """
    Predict house price based on input parameters.
    """

    try:
        # Validate input data
        house_data = HousePredictionInput(
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            sqft_living=sqft_living,
            sqft_lot=sqft_lot,
            sqft_above=sqft_above,
            sqft_basement=sqft_basement,
            floors=floors,
            waterfront=waterfront,
            view=view,
            condition=condition,
            year_built=year_built,
            year_renovated=year_renovated,
            location=location
        )
        # Make prediction
        predicted_price = predict_price(house_data)
        return {"prediction": predicted_price, "currency": "USD"}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
