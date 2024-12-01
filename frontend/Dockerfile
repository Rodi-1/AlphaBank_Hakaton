# Используем официальный Node.js образ в качестве базового
FROM node:18 AS build

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем package.json и package-lock.json (если есть) в контейнер
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь код проекта в контейнер
COPY . .

# Собираем фронтенд (вызываем build команду)
RUN npm run build

# Используем легкий образ nginx для отдачи статических файлов
FROM nginx:alpine

# Копируем собранные файлы из контейнера build в папку для статики nginx
COPY --from=build /app/build /usr/share/nginx/html

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]
