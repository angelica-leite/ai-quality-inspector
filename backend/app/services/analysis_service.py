from app.schemas.product import (
    ProductAnalysisRequest,
    ProductAnalysisResponse,
)


def analyze_product(product: ProductAnalysisRequest) -> ProductAnalysisResponse:
    risk_score = 0.0

    if product.dias_para_expiracao <= 30:
        risk_score += 0.4

    if product.historico_de_problemas >= 3:
        risk_score += 0.4

    if product.temperatura_de_armazenamento > 30:
        risk_score += 0.2

    risk_score = min(risk_score, 1.0)

    if risk_score >= 0.7:
        risk_level = "alto"
    elif risk_score >= 0.4:
        risk_level = "médio"
    else:
        risk_level = "baixo"

    return ProductAnalysisResponse(
        nivel_de_risco=risk_level,
        pontuacao_de_risco=risk_score,
        requer_revisao=risk_score >= 0.4,
    )