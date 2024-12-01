package ru.hackathon.alphabank.recommendsystem.model;

import ru.hackathon.alphabank.recommendsystem.request.Signatures;

import java.util.List;

public record ClientDetails(
        long clientId,
        long organizationId,
        String segment,
        String role,
        int organizations,
        String currentMethod,
        boolean mobileApp,
        Signatures signatures,
        List<String> availableMethods,
        int claims
) { }
