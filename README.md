# API de Agregação de Dados Climáticos e Geográficos

## 📌 Descrição do Projeto

Esta API REST foi desenvolvida em Python utilizando FastAPI.

O objetivo do projeto é integrar dados de APIs públicas para fornecer informações climáticas e geográficas de cidades brasileiras.

A API permite:

- Consultar clima atual de uma cidade
- Listar cidades por estado (UF)
- Validar erros de entrada
- Retornar respostas padronizadas
- Disponibilizar documentação automática com Swagger

---

# 🚀 Como Rodar o Projeto

## 1. Instalar Dependências

Execute no terminal:

```bash
pip install fastapi uvicorn requests pytest httpx
```

---

## 2. Executar a API

No terminal, execute:

```bash
uvicorn src.main:app --reload --port 3000
```

---

## 3. Acessar a Documentação

Swagger:

```text
http://localhost:3000/docs
```

Redoc:

```text
http://localhost:3000/redoc
```

---

# 📡 Endpoints da API

---

## ✅ Health Check

### Endpoint

```http
GET /api/v1/health
```

### Exemplo

```text
http://localhost:3000/api/v1/health
```

### Resposta

```json
{
  "status": "online",
  "timestamp": "2026-05-07T12:00:00Z"
}
```

---

## 🌤 Clima por Cidade

### Endpoint

```http
GET /api/v1/clima/{cidade}
```

### Exemplo

```text
http://localhost:3000/api/v1/clima/Fortaleza
```

### Resposta

```json
{
  "nome": "Fortaleza",
  "estado": "CE",
  "clima": {
    "temperatura": 28,
    "vento": 10
  },
  "consultado_em": "2026-05-07T12:00:00Z"
}
```

---

## 🏙 Listar Cidades por Estado

### Endpoint

```http
GET /api/v1/cidades/{uf}
```

### Exemplo

```text
http://localhost:3000/api/v1/cidades/CE
```

### Resposta

```json
{
  "uf": "CE",
  "quantidade": 3,
  "cidades": [
    "Fortaleza",
    "Sobral",
    "Juazeiro do Norte"
  ]
}
```

---

# ⚠️ Tratamento de Erros

| Código | Descrição |
|--------|------------|
| 400 | Parâmetro inválido |
| 404 | Cidade ou UF não encontrada |
| 503 | Serviço externo indisponível |

---

# 🧪 Executando os Testes

Execute:

```bash
pytest
```

Resultado esperado:

```text
4 passed
```

---

# 📬 Coleção Postman

O arquivo da coleção Postman está disponível em:

```text
docs/postman_collection.json
```

---

# 🛠 Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn
- Requests
- Pytest
- HTTPX

---

# 👥 Integrantes

Consultar arquivo:

```text
INTEGRANTES.md
```