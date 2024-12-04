from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/seu-endpoint', methods=['POST'])
def seu_endpoint():
    
    data = request.get_json()

    if '1' not in data or '2' not in data:
        return jsonify({'error': 'Os atributos "1" e "2" são obrigatórios.'}), 400

   
    try:
        atributo_1 = float(data['1']) 
        atributo_2 = float(data['2'])
    except ValueError:
        return jsonify({'error': 'Os atributos "1" e "2" devem ser números.'}), 400
    
    resultado = atributo_1 + atributo_2

    response = {
        '1': atributo_1,
        '2': atributo_2,
        'resultado': resultado
    }

