from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_clima_sucesso():
    response = client.get("/api/v1/clima/Fortaleza")
    assert response.status_code == 200
    data = response.json()
    assert "nome" in data
    assert "clima" in data

def test_clima_nome_invalido():
    response = client.get("/api/v1/clima/X")
    assert response.status_code == 400

def test_clima_cidade_inexistente():
    response = client.get("/api/v1/clima/CidadeInexistenteXYZ")
    assert response.status_code == 404

def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200