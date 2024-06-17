import os
import docker

def main_function(date, hour_start, hour_end, camera_number):
    print(f"дата {date}, начальный час {hour_start}, конечный час {hour_end}, номер камеры {camera_number}")
    date = str(date)
    hour_start = str(hour_start)
    hour_end = str(hour_end)
    camera_number = str(camera_number)

    # Создаем Docker-клиент
    client = docker.from_env()

    # Запускаем контейнер с передачей аргументов
    container = client.containers.run(
        "my-django-anrp-app",  # Имя образа Docker
        detach=True,  # Запускаем контейнер в фоновом режиме
        command=f"python parallel_pipeline.py {date} {hour_start} {hour_end} {camera_number}"
    )
    print('Только имя скрипта')
    # Выводим ID запущенного контейнера (для отладки)
    print(f"Запущен контейнер с ID: {container.id}")

    # Возвращаем контейнер
    return container 

# Запускаем функцию
container = main_function(2, 2, 6, 26 )

# Ожидаем завершения контейнера 
container.wait()

# Вывод логов контейнера 
logs = container.logs().decode()
print(f"Логи контейнера:\n{logs}")

# Удаление контейнера (необязательно)
# container.remove()