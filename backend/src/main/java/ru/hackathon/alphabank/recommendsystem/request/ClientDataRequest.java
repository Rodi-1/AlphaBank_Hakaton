package ru.hackathon.alphabank.recommendsystem.request;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

public record ClientDataRequest(
        @JsonProperty("clientId") long clientId,
        @JsonProperty("organizationId") long organizationId,
        @JsonProperty("segment") String segment, // "Малый бизнес", "Средний бизнес", "Крупный бизнес"
        @JsonProperty("role") String role, // "ЕИО", "Сотрудник"
        @JsonProperty("organizations") int organizations,
        @JsonProperty("currentMethod") String currentMethod, // "SMS", "PayControl", "КЭП на токене", "КЭП в приложении"
        @JsonProperty("mobileApp") boolean mobileApp,
        @JsonProperty("signatures") Signatures signatures,
        @JsonProperty("availableMethods") List<String> availableMethods,
        @JsonProperty("claims") int claims, // Наличие обращений
        @JsonProperty("isFirstLogIn") boolean isFirstLogIn, // Первый ли логин
        @JsonProperty("currentDevice") String currentDevice // "Мобильное устройство", "ПК"
) {}

