from collections import defaultdict

from src.log_parser import parse_log_file


def generate_report(log_files):
    """Генерирует отчет о состоянии ручек API."""
    overall_data = defaultdict(lambda: {level: 0 for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]})
    total_requests = 0

    for log_file in log_files:
        log_data, requests_count = parse_log_file(log_file)
        total_requests += requests_count

        for handler, levels in log_data.items():
            for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
                overall_data[handler][level] += levels.get(level, 0)

    return overall_data, total_requests


def print_report(report_data, total_requests):
    """Выводит отчет в консоль."""
    print(f"Всего запросов: {total_requests}\n")

    headers = ["HANDLER", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    column_widths = [30, 10, 10, 10, 10, 10]

    header_row = "".join(f"{header:<{width}}" for header, width in zip(headers, column_widths))
    print(header_row)

    overall_counts = {level: 0 for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]}

    for handler in sorted(report_data.keys()):
        counts = [report_data[handler].get(level, 0) for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]]

        for i, level in enumerate(overall_counts.keys()):
            overall_counts[level] += counts[i]

        row = f"{handler:<30}" + "".join(f"{count:<10}" for count in counts)
        print(row)

    total_row = f"{'Total':<30}" + "".join(
        f"{overall_counts[level]:<10}" for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    print(total_row)