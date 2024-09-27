import os
from datetime import datetime

def analyze_heartbeat(log_file, output_file, key='TSTFEED0300|7E3E|0400'):
    timestamps = []  # Список для хранения временных меток и значений heartbeat

    # Открываем файл логов и отбираем строки с нужным ключом
    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if key in line:
                # Находим позицию "Timestamp" и извлекаем 8 символов
                timestamp_position = line.find("Timestamp ")
                if timestamp_position != -1:
                    timestamp_str = line[timestamp_position + len("Timestamp "):timestamp_position + len("Timestamp ") + 8].strip()

                    # Преобразуем строку времени в объект datetime
                    try:
                        current_timestamp = datetime.strptime(timestamp_str, '%H:%M:%S')
                        timestamps.append(current_timestamp)  # Добавляем в список
                    except ValueError:
                        print(f"Ошибка при преобразовании времени: {timestamp_str}")
                        continue  # Пропускаем строки, которые не соответствуют формату

    # Проверяем, нашли ли мы временные метки
    if not timestamps:
        print("Нет временных меток с указанным ключом.")
        return

    # Сортируем временные метки
    timestamps.sort()
    print(f"Найдено {len(timestamps)} временных меток. Запускаем анализ...")

    previous_timestamp = None

    # Открываем файл для записи результатов
    with open(output_file, 'w') as log:
        for current_timestamp in timestamps:
            if previous_timestamp:
                # Рассчитываем разницу по времени (heartbeat)
                heartbeat = (current_timestamp - previous_timestamp).total_seconds()

                # Логируем в зависимости от разницы во времени
                if 31 < heartbeat < 33:
                    log.write(f"WARNING: Heartbeat {heartbeat:.1f} seconds at {current_timestamp.strftime('%H:%M:%S')}\n")
                elif heartbeat >= 33:
                    log.write(f"ERROR: Heartbeat {heartbeat:.1f} seconds at {current_timestamp.strftime('%H:%M:%S')}\n")
                else:
                    print(f"Heartbeat {heartbeat:.1f} seconds (no log) at {current_timestamp.strftime('%H:%M:%S')}")

            # Обновляем предыдущий timestamp для следующего сравнения
            previous_timestamp = current_timestamp

# Получаем текущую директорию, где находится этот скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))

# Указываем правильные пути к файлам
log_file = os.path.join(current_dir, 'hblog.txt')  # Исходный файл с логами
output_file = os.path.join(current_dir, 'hb_test.log')  # Файл для записи результатов

# Запускаем анализ
analyze_heartbeat(log_file, output_file)

# Проверка на успешное создание файла
if os.path.exists(output_file):
    print(f"Результаты успешно записаны в {output_file}.")
else:
    print("Файл не был создан.")








