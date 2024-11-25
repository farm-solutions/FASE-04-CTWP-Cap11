from flask import Flask, request, jsonify
import joblib

# Carregar o modelo
model = joblib.load('./src/pipeline_knn_optimized.pkl')



# Inicializar a aplicação Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Receber dados do POST request
    data = request.get_json(force=True)

    # Converter dados para o formato adequado
    prediction = model.predict([data['features']])

    # Retornar a previsão
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)