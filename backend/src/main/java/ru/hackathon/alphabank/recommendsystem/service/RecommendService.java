package ru.hackathon.alphabank.recommendsystem.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import ru.hackathon.alphabank.recommendsystem.mapper.ClientDataMapper;
import ru.hackathon.alphabank.recommendsystem.request.ClientDataRequest;
import ru.hackathon.alphabank.recommendsystem.request.MlResponse;

import java.util.Objects;

@Service
@RequiredArgsConstructor
public class RecommendService {

    private final MLRecommendService mlRecommendService;

    public String getRecommendation(ClientDataRequest request) {

        String recommendation = "Нет рекомендаций";
        if (request.availableMethods().size() == 4) return recommendation;

        if(request.isFirstLogIn()){
            if (Objects.equals(request.currentDevice(), "Мобильное устройство")) {
                recommendation = "Удобство на кончиках пальцев: подписывайте документы в любое время и в любом месте с помощью PayControl.";
            } else {
                recommendation = "Надежность и безопасность: используйте КЭП на токене для защищенного подписания документов.";
            }
            return recommendation;
        }

        MlResponse mlRequest = mlRecommendService.recommend(ClientDataMapper.mapToClientDetails(request));
        switch (mlRequest.recommendedMethod()) {
            case 0:   //нет рекомендаций
                recommendation = "Нет рекомендаций";
                break;
            case 1:   //PayControl
                recommendation = "Усиленная защита для вашего бизнеса: выберите PayControl для максимальной безопасности операций.";
                break;
            case 2:   //КЭП на токене
                recommendation = "Простота и надежность в использовании: КЭП на токене для эффективной работы с документами.";
                break;
            case 3:   //КЭП в приложении
                recommendation = "Оцените преимущества цифровой трансформации с КЭП в приложении — меньше бумаги, больше эффективности.";
                break;

        }
        return recommendation;
    }
}