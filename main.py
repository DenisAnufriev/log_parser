import argparse

from src.report_generator import generate_report, print_report


def main():
    parser = argparse.ArgumentParser(description='Анализирует логи Django и генерирует отчеты.')
    parser.add_argument('log_files', nargs='+', help='Пути к лог-файлам.')
    parser.add_argument('--report', required=True, help='Название отчета для генерации.')

    args = parser.parse_args()

    if args.report != 'handlers':
        print("Ошибка: поддерживается только отчет 'handlers'.")
        return

    report_data, total_requests = generate_report(args.log_files)

    print_report(report_data, total_requests)


if __name__ == '__main__':
    main()
