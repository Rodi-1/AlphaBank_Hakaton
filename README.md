
# AlphaBank_Hakaton

Это клиент-серверное приложение, разработанное для рекомендаций клиентам оптимального способа подписания документов на основе их данных и контекста использования. Проект создан в рамках хакатона и включает в себя три ключевых компонента: фронтенд, бэкенд и ML-модель.

- Приложение доступно по IP-адресу:  http://176.108.251.22/
- !Данный репозиторий является слиянием 3х отдельных репозиториев, по этому нет уверенности в том, что всё будет запускаться локально!
- Ссылки на репозитории каждого модуля:
- Backend - https://github.com/Shach1/alpha-bank-recommend-system
- Frontend - https://github.com/Sh1iba/Electronic-signature-in-Alfa-Bank
- ML - https://github.com/yarockM/Alpha-bank-hackaton


## 📋 Описание

Основная задача проекта — предоставить автоматизированную систему рекомендаций для выбора оптимального метода подписания (SMS, PayControl, КЭП на токене, КЭП в приложении). 

**Целевая аудитория:** разработчики онлайн-платформы Alpha-Банка.

---

## 🛠️ Компоненты проекта

### 1. **Frontend**
Фронтенд построен на **React** и предоставляет интерфейс для ввода данных о клиенте и получения рекомендаций.

- **Функционал:**
  - Ввод данных клиента (ID, организация, сегмент, роль и т.д.).
  - Выбор доступных методов подписания.
  - Просмотр рекомендаций на основе данных, полученных от сервера.


### 2. **Backend**
Бэкенд реализован на **Java Spring**. Он обрабатывает данные от фронтенда и взаимодействует с ML-моделью для генерации рекомендаций.

- **Функционал:**
  - REST API для приема данных от фронтенда.
  - Обработка данных и запросы к ML-модели.
  - Возвращение рекомендаций на фронтенд.


### 3. **ML-модель**
ML-модель написана на **Python**. Она анализирует данные клиента и возвращает рекомендации на основе контекста.

- **Функционал:**
  - Обработка входящих данных в формате JSON.
  - Генерация рекомендаций на основе обученной модели.
  


---

## 🚀 Запуск проекта с использованием Docker

### Требования
- Docker
- Docker Compose

### Шаги
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/your-repo/alpha-bank-recommend-system.git
   cd alpha-bank-recommend-system
   ```

2. Соберите и запустите контейнеры:
   ```bash
   docker-compose up --build
   ```


---

## 📂 Структура проекта

```plaintext
alpha-bank-recommend-system/
│
├── frontend/         # React-приложение (фронтенд)
│
├── backend/          # Java Spring-бэкенд
│
├── ml_model/         # ML-модель на Python
│
├── docker-compose.yml # Docker Compose файл для запуска всего проекта
└── README.md          # Документация
```

---

## 🔧 Технические детали

- **Фронтенд:** React, CSS
- **Бэкенд:** Java Spring, Gradle
- **ML-модель:** Python (Flask), Scikit-learn
- **Контейнеризация:** Docker, Docker Compose

---

## 📈 Результаты и планы

### Результаты
- Полностью рабочий прототип, включающий фронтенд, бэкенд и ML-модель.
- Успешная интеграция всех компонентов через REST API.

### Планы на будущее
- Улучшение ML-модели на основе реальных данных.
- Проведение масштабного тестирования.
- Оптимизация архитектуры для поддержки большого количества пользователей.

---

## 🤝 Команда Averagers

- **Frontend-разработчик:** Ибрагимов Зафар А. 
- **Backend-разработчик:** Трухманов Евгений К. 
- **ML-разработчик:** Марцевой Ярослав А.
- **Аналитик/Ведущий разработчик:** Сортов Семён А.

---

## 📬 Контакты

Если у вас есть вопросы или предложения, вы можете связаться с нами:

- Telegram - https://t.me/b0neIess (Ибрагимов Зафар А.)
- Telegram - https://t.me/Shach1 (Трухманов Евгений К.)
- Telegram - https://t.me/TozoHanoline (Марцевой Ярослав А.)
- Telegram - https://t.me/rodi1wastaken (Сортов Семён А.)

---

**Спасибо за внимание!**
