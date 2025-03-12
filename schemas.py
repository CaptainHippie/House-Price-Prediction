from pydantic import BaseModel, Field, field_validator
from typing import Optional

class HousePredictionInput(BaseModel):
    bedrooms: int = Field(..., ge=0, le=9, description="Number of bedrooms")
    bathrooms: int = Field(..., ge=0, le=8, description="Number of bathrooms")
    sqft_living: float = Field(..., ge=0, description="Square footage of living space")
    sqft_lot: float = Field(..., ge=0, description="Square footage of lot")
    sqft_above: float = Field(..., ge=0, description="Square footage above ground")
    sqft_basement: float = Field(..., ge=0, description="Square footage of basement")
    floors: int = Field(..., ge=0, le=5, description="Number of floors")
    waterfront: bool = Field(False, description="Whether the house has a waterfront view")
    view: int = Field(2, ge=0, le=4, description="Quality of view")
    condition: int = Field(3, ge=0, le=5, description="Overall condition")
    year_built: int = Field(..., ge=1900, le=2024, description="Year built")
    year_renovated: Optional[int] = Field(None, ge=1900, le=2024, description="Year renovated")
    location: str = Field(..., description="Address of the property")

    @field_validator('year_renovated')

    def year_renovated_validator(cls, v, values):
        if v is not None and 'year_built' in values.data and v < values.data['year_built']:
            raise ValueError('Year renovated cannot be earlier than year built')
        return v