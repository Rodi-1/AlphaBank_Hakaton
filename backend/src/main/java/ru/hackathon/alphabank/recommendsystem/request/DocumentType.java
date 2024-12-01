package ru.hackathon.alphabank.recommendsystem.request;

public record DocumentType(
        int mobile, // Количество подписаний в мобильном приложении
        int web // Количество подписаний в вебе
) {}