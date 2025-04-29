import argparse
import logging
import os

from src.report_generator import generate_report, print_report

logging.basicConfig(level=logging.ERROR)


def main() -> None:
    parser = argparse.ArgumentParser(description='Анализирует логи Django и генерирует отчеты.')
    parser.add_argument('log_files', nargs='+', help='Пути к лог-файлам.')
    parser.add_argument('--report', required=True, help='Название отчета для генерации.')

    args = parser.parse_args()

    for log_file in args.log_files:
        if not os.path.exists(log_file):
            logging.error(f"Файл не найден: {log_file}")
            return

    try:
        report_data, total_requests = generate_report(args.log_files)
    except Exception as e:
        logging.error(f"Ошибка при генерации отчета: {e}")
        return

    print_report(report_data, total_requests)


if __name__ == '__main__':
    main()
