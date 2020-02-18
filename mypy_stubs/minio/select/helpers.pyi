from typing import Any

SQL: str
EVENT_RECORDS: str
EVENT_PROGRESS: str
EVENT_STATS: str
EVENT_CONT: str
EVENT_END: str
EVENT_CONTENT_TYPE: str
EVENT: str
ERROR: str

def calculate_crc(value: Any): ...
def validate_crc(current_value: Any, expected_value: Any): ...
def byte_int(data_bytes: Any): ...
