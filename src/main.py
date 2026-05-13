from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from src.services.cidade_service import buscar_cidade
from src.services.clima_service import buscar_clima

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HEALTH CHECK
@app.get("/api/v1/health")
def health():
    return {
        "status": "healthy",
        "versao": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }

# CLIMA
from datetime import datetime
import traceback

# CLIMA
@app.get("/api/v1/clima/{cidade}")
def clima(cidade: str):

    if len(cidade) < 2:
        raise HTTPException(
            status_code=400,
            detail={
                "erro": True,
                "codigo": "NOME_INVALIDO",
                "mensagem": "O nome da cidade deve conter pelo menos 2 caracteres",
                "nome_informado": cidade
            }
        )

    dados = buscar_cidade(cidade)

    if not dados:
        raise HTTPException(
            status_code=404,
            detail={
                "erro": True,
                "codigo": "CIDADE_NAO_ENCONTRADA",
                "mensagem": "Nenhuma cidade encontrada",
                "nome_informado": cidade
            }
        )

    # 🔥 validação importante (evita erro escondido)
    if not dados.get("latitude") or not dados.get("longitude"):
        raise HTTPException(
            status_code=404,
            detail="Cidade sem coordenadas"
        )

    try:
        clima = buscar_clima(dados["latitude"], dados["longitude"])
    except Exception as e:
        print("ERRO REAL:")
        traceback.print_exc()

        raise HTTPException(
            status_code=503,
            detail=str(e)
        )

    return {
        "nome": dados["nome"],
        "estado": dados["uf"],
        "clima": clima,
        "consultado_em": datetime.utcnow().isoformat()
    }

# CIDADES POR UF
@app.get("/api/v1/cidades/{uf}")
def cidades(uf: str, limite: int = 10):

    if len(uf) != 2:
        raise HTTPException(
            status_code=400,
            detail={
                "erro": True,
                "codigo": "SIGLA_UF_INVALIDA",
                "mensagem": "A sigla deve ter 2 letras",
                "sigla_uf_informada": uf
            }
        )

    import requests

    url = f"https://brasilapi.com.br/api/ibge/municipios/v1/{uf.upper()}"

    try:
        res = requests.get(url)
        data = res.json()
    except:
        raise HTTPException(
            status_code=503,
            detail={"erro": True, "codigo": "SERVICO_EXTERNO_INDISPONIVEL"}
        )

    if not data:
        raise HTTPException(
            status_code=404,
            detail={
                "erro": True,
                "codigo": "UF_NAO_ENCONTRADA"
            }
        )

    return {
        "uf": uf.upper(),
        "quantidade_retornada": min(limite, len(data)),
        "cidades": data[:limite],
        "consultado_em": datetime.utcnow().isoformat()
    }