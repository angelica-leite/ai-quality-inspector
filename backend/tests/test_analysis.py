from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_analyze_high_risk_product():
    response = client.post(
        "/api/v1/analysis",
        json={
            "categoria": "Medicamento",
            "preco": 89.9,
            "quantidade": 25,
            "fornecedor": "Fornecedor A",
            "dias_para_expiracao": 10,
            "temperatura_de_armazenamento": 32,
            "historico_de_problemas": 4,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nivel_de_risco"] == "alto"
    assert data["pontuacao_de_risco"] == 1.0
    assert data["requer_revisao"] is True