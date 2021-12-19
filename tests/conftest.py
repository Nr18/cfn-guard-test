import pytest
import os.path


@pytest.fixture(scope="module")
def payload_path() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "payloads"))
