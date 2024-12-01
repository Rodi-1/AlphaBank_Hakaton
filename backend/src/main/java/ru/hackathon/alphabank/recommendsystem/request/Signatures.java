package ru.hackathon.alphabank.recommendsystem.request;

public record Signatures(
        DocumentType common,
        DocumentType special
) {}