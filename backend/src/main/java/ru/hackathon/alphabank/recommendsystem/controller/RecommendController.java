package ru.hackathon.alphabank.recommendsystem.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.hackathon.alphabank.recommendsystem.request.ClientDataRequest;
import ru.hackathon.alphabank.recommendsystem.response.RecommendResponse;
import ru.hackathon.alphabank.recommendsystem.service.RecommendService;

@CrossOrigin(origins = "http://176.108.251.22")
@RestController
@RequestMapping("/api/v1/recommend")
@RequiredArgsConstructor
public class RecommendController {

    private final RecommendService recommendService;

    @PostMapping("/get")
    public ResponseEntity<?> getRecommendation(@RequestBody ClientDataRequest clientDataRequest) {
        RecommendResponse recommendation = new RecommendResponse(recommendService.getRecommendation(clientDataRequest)) ;
        return ResponseEntity.ok(recommendation);
    }
}
