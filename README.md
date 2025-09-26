# Prompt Framework v0.0.1

Запуск проекта через Docker Desktop (Windows / Mac / Linux).

1. Перейти в папку проекта:
cd prompt_framework_v0.0.1_docker

2. Собрать и запустить контейнер:
docker-compose up --build -d

3.Проверить работу:
docker logs -f prompt_framework

Остановка
docker-compose down

PostgreSQL (опционально)

Контейнер db с PostgreSQL:
Пользователь: user
Пароль: password
База: mydb

Строка подключения для приложения:
postgresql://user:password@db:5432/mydb

Если локальный PostgreSQL использует порт 5432 — остановите его или пробросьте другой порт для контейнера.