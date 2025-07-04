# Django Log Parser

Программа для анализа логов Django и генерации отчетов о состоянии ручек API по каждому уровню логирования.

Этот инструмент анализирует логи Django и генерирует отчет по запросам к API. Программа поддерживает генерацию отчета о количестве запросов по ручкам и уровням логирования. Отчет группируется по ручкам и сортируется по алфавиту. Программа также позволяет обрабатывать несколько лог-файлов.

## Установка

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/DenisAnufriev/log_parser.git
cd django-log-parser
```

2. Установите зависимости:
Рекомендуется использовать виртуальное окружение.

```bash
python -m venv venv
source venv/bin/activate  # для Windows используйте venv\Scripts\activate
pip install -r requirements.txt
```

## Использование
#### Чтобы запустить программу и сгенерировать отчет, используйте следующую команду:

```bash
python main.py <путь_к_лог_файлу_1> <путь_к_лог_файлу_2> ... --report handlers
```
#### Пример:
```bash
python main.py logs/app1.log logs/app2.log --report handlers
```


### Требования
Python 3.6+

Установленные зависимости (см. requirements.txt)

### Структура проекта
```perl
django-log-parser/
├── main.py              # Главный скрипт для запуска
├── src/
│   ├── report_generator.py  # Генерация отчета
│   ├── log_parser.py       # Парсинг логов
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация
```