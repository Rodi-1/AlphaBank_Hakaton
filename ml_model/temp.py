#Генережка

import json
import random

segments = ["Малый бизнес", "Средний бизнес", "Крупный бизнес"]
roles = ["ЕИО", "Сотрудник"]
methods = ["PayControl", "КЭП на токене", "КЭП в приложении"]
available_methods = ["SMS", "PayControl", "КЭП на токене", "КЭП в приложении"]

dataset = []

for i in range(100000):
    client_id = f"client_{i}"
    organization_id = f"organization_{i}"
    segment = random.choice(segments)
    role = random.choice(roles)
    organizations = random.randint(1, 300)
    current_method = random.choice(methods + ["SMS"])
    mobile_app = random.choice([True, False])
    signatures = {
        "common": {
            "mobile": random.randint(0, 100),
            "web": random.randint(0, 100)
        },
        "special": {
            "mobile": random.randint(0, 100),
            "web": random.randint(0, 100)
        }
    }
    available = random.sample(available_methods, random.randint(1, len(available_methods)))
    claims = random.randint(0, 10)

    data = {
        "clientId": client_id,
        "organizationId": organization_id,
        "segment": segment,
        "role": role,
        "organizations": organizations,
        "currentMethod": current_method,
        "mobileApp": mobile_app,
        "signatures": signatures,
        "availableMethods": available,
        "claims": claims,
    }

    dataset.append(data)

# Save to a JSON file
with open('dataset.json', 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)


import json

# Функция для определения рекомендации
def recommend_method(data):
    # Добавляем currentMethod в availableMethods, если его там нет
    if data["currentMethod"] not in data["availableMethods"]:
        data["availableMethods"].append(data["currentMethod"])

    segment = data["segment"]
    role = data["role"]
    organizations = data["organizations"]
    mobile_app = data["mobileApp"]
    signatures = data["signatures"]
    available_methods = data["availableMethods"]
    claims = data["claims"]

    # Все возможные методы
    all_methods = {"SMS", "PayControl", "КЭП на токене", "КЭП в приложении"}

    # Исключаем уже подключенные методы
    unconnected_methods = all_methods - set(available_methods)

    # Если все методы подключены, возвращаем "None"
    if not unconnected_methods:
        return "None"

    # Функция для выбора подходящего метода из неподключенных
    def choose_best_method(preferred_methods):
        for method in preferred_methods:
            if method in unconnected_methods:
                return method
        return "None"

    # Определяем рекомендацию
    if segment == "Малый бизнес":
        if mobile_app:
            return choose_best_method(["PayControl", "КЭП в приложении", "КЭП на токене"])
        else:
            return choose_best_method(["КЭП на токене"])

    if segment in ["Средний бизнес", "Крупный бизнес"]:
        if role == "ЕИО":
            return choose_best_method(["КЭП в приложении", "КЭП на токене"])
        if role == "Сотрудник":
            return choose_best_method(["КЭП на токене", "PayControl", "КЭП в приложении"])

    if organizations <= 10:
        return choose_best_method(["КЭП в приложении", "PayControl"])
    else:
        return choose_best_method(["КЭП на токене", "КЭП в приложении"])

    if claims > 0:
        return choose_best_method(["PayControl", "КЭП в приложении"])

    # Дефолтная рекомендация
    return choose_best_method(["КЭП на токене"])

# Загружаем данные
with open("ds/dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

# Добавляем рекомендации в каждый элемент
for client in dataset:
    client["recommendedMethod"] = recommend_method(client)

# Сохраняем разметку
with open("ds/labeled_dataset.json", "w", encoding="utf-8") as file:
    json.dump(dataset, file, ensure_ascii=False, indent=4)


    

#Обучение модельки
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report
from custom_transformers import MultiLabelBinarizerTransformer
import xgboost as xgb
import joblib


# Загрузка данных из файла data.json
with open('ds/labeled_dataset.json', 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# Преобразование JSON в DataFrame
data = pd.DataFrame(data_json)

# Разворачиваем данные из 'signatures'
def extract_signatures(row):
    row['signatures_common_mobile'] = row['signatures']['common']['mobile']
    row['signatures_common_web'] = row['signatures']['common']['web']
    row['signatures_special_mobile'] = row['signatures']['special']['mobile']
    row['signatures_special_web'] = row['signatures']['special']['web']
    return row

data = data.apply(extract_signatures, axis=1)

data['mobileApp'] = data['mobileApp'].astype(int)

# Создаем признак с количеством доступных методов
data['availableMethods_count'] = data['availableMethods'].apply(len)

# Удаляем ненужные столбцы
data = data.drop(columns=['clientId', 'organizationId', 'signatures'])
# Обработка списка 'availableMethods' через MultiLabelBinarizer не потребуется, так как мы включим это в ColumnTransformer
# Целевая переменная
y = data['recommendedMethod']

# Признаки
X = data.drop(columns=['recommendedMethod'])

# Кодирование целевой переменной
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


X_train, X_test, y_train_encoded, y_test_encoded = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)


# Параметры модели
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer

class MultiLabelBinarizerTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.mlb = MultiLabelBinarizer()
    
    def fit(self, X, y=None):
        self.mlb.fit(X['availableMethods'])
        return self
    
    def transform(self, X):
        available_methods_encoded = self.mlb.transform(X['availableMethods'])
        available_methods_df = pd.DataFrame(
            available_methods_encoded,
            columns=['available_' + method for method in self.mlb.classes_],
            index=X.index
        )
        X = X.reset_index(drop=True).join(available_methods_df.reset_index(drop=True))
        X = X.drop(columns=['availableMethods'])
        return X

# Список числовых признаков
numeric_features = [
    'organizations',
    'mobileApp',
    'signatures_common_mobile',
    'signatures_common_web',
    'signatures_special_mobile',
    'signatures_special_web',
    'claims',
    'availableMethods_count'
]

# Список категориальных признаков
categorical_features = ['segment', 'role', 'currentMethod']

# Создаем колонковый трансформер
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(), categorical_features),
        ('avail_methods', MultiLabelBinarizerTransformer(), ['availableMethods'])
    ],
    remainder='drop'
)


# Создаем конвейер
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', xgb.XGBClassifier(
        objective='multi:softmax',
        eval_metric='mlogloss',
        use_label_encoder=False,
        seed=42
    ))
])



# Обучение модели
# Обучение модели
pipeline.fit(X_train, y_train_encoded)


# Предсказания на тестовой выборке
y_pred_encoded = pipeline.predict(X_test)

# Преобразуем предсказания обратно в исходные метки
y_pred = label_encoder.inverse_transform(y_pred_encoded)
y_test = label_encoder.inverse_transform(y_test_encoded)

# Вычисление точности
accuracy = accuracy_score(y_test_encoded, y_pred_encoded)
print(f'Точность модели: {accuracy:.4f}')

# Отчет о классификации
print(classification_report(y_test, y_pred))


# Сохранение конвейера
joblib.dump(pipeline, 'model_pipeline.joblib')

# Сохранение LabelEncoder для целевой переменной
joblib.dump(label_encoder, 'label_encoder.joblib')































