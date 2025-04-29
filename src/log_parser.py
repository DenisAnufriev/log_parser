import re
from collections import defaultdict
from typing import Dict, Tuple, DefaultDict

log_pattern = re.compile(r"""
    (?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3})  # Дата и время в формате 'YYYY-MM-DD HH:MM:SS,mmm'
    \s+                                                        # Один или несколько пробелов
    (?P<level>\w+)                                             # Уровень логирования (например, INFO, ERROR)
    \s+                                                        # Пробелы
    (?P<logger>django\.\S+):                                    # Имя логгера, начинающееся с 'django.' и до двоеточия
    \s+                                                        # Пробелы
    (?P<message>.*?)                                           # Сообщение (нежадный захват любого символа)
    (?P<handler>/[\w/]+)                                       # Ручка (например, /api/v1/resource)
""", re.VERBOSE)


def parse_log_file(file_path: str) -> Tuple[Dict[str, Dict[str, int]], int]:
    """
    Парсит лог-файл и возвращает:
    - словарь с количеством запросов по ручкам и уровням логирования
    - общее количество распознанных логов
    """
    log_data: DefaultDict[str, DefaultDict[str, int]] = defaultdict(lambda: defaultdict(int))
    total_requests = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = log_pattern.search(line)
                if match:
                    level = match.group('level')
                    handler = match.group('handler')
                    log_data[handler][level] += 1
                    total_requests += 1
    except FileNotFoundError:
        print(f"❌ Файл не найден: {file_path}")

    return log_data, total_requests
