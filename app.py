from flask import Flask, jsonify

# Criar a aplicação Flask
app = Flask(__name__)

# Lista com exatamente 3 livros (id, titulo, autor, ano)
livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"id": 3, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977}
]

# Rota GET /livros - retorna a lista de livros em JSON
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify({"livros": livros})

# Iniciar a aplicação em modo debug
if __name__ == '__main__':
    app.run(debug=True)