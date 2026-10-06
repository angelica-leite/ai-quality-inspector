from fastapi import APIRouter

from app.schemas.product import (
    ProductAnalysisRequest,
    ProductAnalysisResponse,
)
from app.services.analysis_service import analyze_product

router = APIRouter()


@router.post(
    "/analysis",
    response_model=ProductAnalysisResponse,
)
def analyze_product_route(
    product: ProductAnalysisRequest,
) -> ProductAnalysisResponse:
    return analyze_product(product)