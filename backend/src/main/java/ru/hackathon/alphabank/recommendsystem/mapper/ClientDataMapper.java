package ru.hackathon.alphabank.recommendsystem.mapper;

import ru.hackathon.alphabank.recommendsystem.model.ClientDetails;
import ru.hackathon.alphabank.recommendsystem.request.ClientDataRequest;


public class ClientDataMapper {

    public static ClientDetails mapToClientDetails(ClientDataRequest request) {
        return new ClientDetails(
                request.clientId(), // clientId
                request.organizationId(), // organizationId
                request.segment(), // segment
                request.role(), // role
                request.organizations(), // organizations
                request.currentMethod(), // currentMethod
                request.mobileApp(), // mobileApp
                request.signatures(), // signatures
                request.availableMethods(), // availableMethods
                request.claims() // claims
        );
    }
}

