from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/invert_text', methods=['POST'])
def invert_text():
    
    data = request.get_json()
    
    if 'texto' not in data:
        return jsonify({'error': 'O atributo "texto" é obrigatório.'}), 400
    
    texto = data['texto']
    texto_invertido = texto[::-1]
    
    return jsonify({'texto_invertido': texto_invertido})
