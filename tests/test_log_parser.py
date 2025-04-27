import pytest
from src.log_parser import parse_log_file


def test_parse_log_file(tmp_path):
    log_content = (
        "2023-10-01 12:00:00,000 INFO django.request: GET /api/v1/resource\n"
        "2023-10-01 12:00:01,000 ERROR django.request: GET /api/v1/resource\n"
        "2023-10-01 12:00:02,000 DEBUG django.request: GET /api/v1/resource\n"
        "2023-10-01 12:00:03,000 WARNING django.request: GET /api/v1/resource\n"
        "2023-10-01 12:00:04,000 CRITICAL django.request: GET /api/v1/resource\n"
    )

    log_file = tmp_path / "test_log.txt"
    log_file.write_text(log_content)

    expected_output = {
        '/api/v1/resource': {
            'DEBUG': 1,
            'INFO': 1,
            'WARNING': 1,
            'ERROR': 1,
            'CRITICAL': 1,
        }
    }

    log_data, total_requests = parse_log_file(log_file)

    log_data_normalized = {k: dict(v) for k, v in log_data.items()}

    assert log_data_normalized == expected_output
    assert total_requests == 5