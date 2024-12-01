package ru.hackathon.alphabank.recommendsystem.request;

public record MlResponse(
        String clientId,
        String organizationId,
        Integer recommendedMethod
) {
}
