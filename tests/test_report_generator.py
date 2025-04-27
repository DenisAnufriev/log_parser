import pytest
from src.report_generator import generate_report


def test_generate_report(tmp_path):
    log_data = {
        '/api/v1/resource': {
            'DEBUG': 1,
            'INFO': 2,
            'WARNING': 0,
            'ERROR': 1,
            'CRITICAL': 0,
        }
    }

    log_content = (
        "2023-10-01 12:00:00,000 INFO django.request: GET /api/v1/resource\n"
        "2023-10-01 12:00:01,000 INFO django.request: GET /api/v1/resource\n"
        "2023-10-01 12:00:02,000 ERROR django.request: GET /api/v1/resource\n"
        "2023-10-01 12:00:03,000 DEBUG django.request: GET /api/v1/resource\n"
    )

    log_file = tmp_path / "test_log.txt"
    log_file.write_text(log_content)

    report_data, total_requests = generate_report([str(log_file)])

    expected_output = (
        {'/api/v1/resource': {'DEBUG': 1, 'INFO': 2, 'WARNING': 0, 'ERROR': 1, 'CRITICAL': 0}},
        4
    )

    assert report_data == expected_output[0]
    assert total_requests == expected_output[1]