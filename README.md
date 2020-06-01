# API для YaTube

**API начинается с /api/v1/**

# POSTS
Посты

## Получить список всех публикаций:
---------------------------------------
    GET /api/v1/posts/
    
    QUERY PARAMETERS 
    group - number (ID группы)


## Создать новую публикацию
---------------------------------------
    POST /api/v1/posts/    

    REQUEST BODY SCHEMA: application/json
    text - string (Текст поста)

## Получить публикацию по id    
---------------------------------------
    GET /api/v1/posts/{id}/

    PATH PARAMETERS
    id - number (ID публикации)

## Обновить публикацию по id
---------------------------------------
    PATCH /api/v1/posts/{id}/

    PATH PARAMETERS
    id required number (ID публикации)
    
    REQUEST BODY SCHEMA: application/json
    text required string (Текст поста)

## Частично обновить публикацию по id
---------------------------------------
    PUT /api/v1/posts/{id}/

    PATH PARAMETERS    
    id required number (ID публикации)
    
    REQUEST BODY SCHEMA: application/json
    text required string (Текст поста)

## Удалить публикацию по id
---------------------------------------
    DELETE /api/v1/posts/{id}/

    PATH PARAMETERS
    id required number (ID публикации)