FROM openjdk:21-jdk
ARG JAR_FILE=build/*.jar
COPY ./build/libs/AlphaBank-recommendSystem-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]