from fastapi import FastAPI

from app.api.routes.analysis import router as analysis_router


app = FastAPI(
    title="AI Quality Inspector API",
    description="API para análise inteligente de qualidade de produtos.",
    version="1.0.0",
)


app.include_router(
    analysis_router,
    prefix="/api/v1",
    tags=["Analysis"],
)


@app.get("/")
def root():
    return {
        "message": "AI Quality Inspector API",
        "status": "running",
    }