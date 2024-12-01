from flask import Flask, request, jsonify
import joblib  # Для загрузки модели
import pandas as pd
from custom_transformers import MultiLabelBinarizerTransformer

# Инициализация Flask
app = Flask(__name__)

# Загрузка модели и LabelEncoder
MODEL_PATH = "python-docker/model_pipeline.joblib"
LABEL_ENCODER_PATH = "python-docker/label_encoder.joblib"
pipeline = joblib.load(MODEL_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)

# Функция для извлечения признаков из 'signatures'
def extract_signatures(row):
    row['signatures_common_mobile'] = row['signatures']['common']['mobile']
    row['signatures_common_web'] = row['signatures']['common']['web']
    row['signatures_special_mobile'] = row['signatures']['special']['mobile']
    row['signatures_special_web'] = row['signatures']['special']['web']
    return row

# Ручка для получения предсказаний
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получение данных из запроса
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Преобразование данных в DataFrame
        new_data = pd.DataFrame([data])

        # Предварительная обработка данных
        new_data = new_data.apply(extract_signatures, axis=1)

        # Преобразуем булевое значение 'mobileApp' в числовое
        new_data['mobileApp'] = new_data['mobileApp'].astype(int)

        # Создаем признак с количеством доступных методов
        new_data['availableMethods_count'] = new_data['availableMethods'].apply(len)

        # Удаляем ненужные столбцы
        features = new_data.drop(columns=['clientId', 'organizationId', 'signatures', 'recommendedMethod'], errors='ignore')

        # Предсказание
        predicted_class_encoded = pipeline.predict(features)[0]
        predicted_class = label_encoder.inverse_transform([predicted_class_encoded])[0]
        

        results = {'None': 0,
            'PayControl':1,
        'КЭП на токене':2,
        'КЭП в приложении':3}
        
        # Возврат результата
        return jsonify({
            "clientId": data.get("clientId"),
            "organizationId" : data.get('organizationId'),
            "recommendedMethod": results[predicted_class]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Ручка для проверки работоспособности сервера
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# Запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
