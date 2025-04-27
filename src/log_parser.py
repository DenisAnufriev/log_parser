import re
from collections import defaultdict


def parse_log_file(file_path):
    """Парсит лог-файл и возвращает словарь с количеством запросов по ручкам и уровням логирования."""
    log_data = defaultdict(lambda: defaultdict(int))
    total_requests = 0

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(
                r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3})\s+(\w+)\s+(django\.\S+):\s+(.*?)(/[\w/]+)', line)
            if match:
                level = match.group(2)
                handler = match.group(5)
                log_data[handler][level] += 1
                total_requests += 1

    return log_data, total_requests
