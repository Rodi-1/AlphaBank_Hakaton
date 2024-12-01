package ru.hackathon.alphabank.recommendsystem.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import ru.hackathon.alphabank.recommendsystem.model.ClientDetails;
import ru.hackathon.alphabank.recommendsystem.request.ClientDataRequest;
import ru.hackathon.alphabank.recommendsystem.request.MlResponse;

@Service
public class MLRecommendService {

    private static final Logger logger = LoggerFactory.getLogger(MLRecommendService.class);

    private final RestTemplate restTemplate;

    public MLRecommendService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public MlResponse recommend(ClientDetails data) {
        logger.info("Received client data: {}", data);

        // Create headers
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        // Create request
        HttpEntity<ClientDetails> request = new HttpEntity<>(data, headers);

        // Send request and get response
        String url = "http://ml_app:5000/predict";
        MlResponse mlResponse = restTemplate.postForObject(url, request, MlResponse.class);

        logger.info("Received recommendation from Python server: {}", mlResponse);
        return mlResponse;
    }
}

