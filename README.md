# API de Livros - Flask

API simples em Python com Flask para servir uma lista de 3 livros clássicos da literatura brasileira.

## Objetivo

Fornecer uma API REST básica que retorna uma lista fixa de 3 livros em formato JSON, para ser consumida por um frontend React.

## Livros disponíveis

| ID | Título | Autor | Ano |
|----|--------|-------|-----|
| 1 | Dom Casmurro | Machado de Assis | 1899 |
| 2 | O Cortiço | Aluísio Azevedo | 1890 |
| 3 | A Hora da Estrela | Clarice Lispector | 1977 |

## Como instalar as dependências

1. Entre na pasta do projeto:
```bash
cd api-livros-flask
```

2. Crie o ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- **Windows (PowerShell/CMD):**
```bash
venv\Scripts\activate
```
- **Linux/Mac (bash/zsh):**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como executar

Com o ambiente virtual ativado:
```bash
python app.py
```

A API estará disponível em: **http://127.0.0.1:5000**

## Endpoint

- **GET** `http://127.0.0.1:5000/livros`

Retorna:
```json
{
  "livros": [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"id": 3, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977}
  ]
}
```

## Observações

- Não usa banco de dados (dados em memória)
- Não tem autenticação
- Apenas a biblioteca Flask como dependência
- Modo debug ativado para desenvolvimento