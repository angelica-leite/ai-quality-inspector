from typing import Literal

from pydantic import BaseModel, Field


class ProductAnalysisRequest(BaseModel):
    categoria: str = Field(min_length=2, max_length=50)
    preco: float = Field(gt=0)
    quantidade: int = Field(ge=0)
    fornecedor: str = Field(min_length=2, max_length=100)
    dias_para_expiracao: int
    temperatura_de_armazenamento: float = Field(allow_inf_nan=False)
    historico_de_problemas: int = Field(ge=0)


class ProductAnalysisResponse(BaseModel):
    nivel_de_risco: Literal["baixo", "médio", "alto"]
    pontuacao_de_risco: float = Field(ge=0, le=1)
    requer_revisao: bool
