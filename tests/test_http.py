import pytest
from lib.http_utils import get_response_code

class TestHttpUtils:
    def test_get_request_success(self):
        response_code = get_response_code("https://httpbin.org/get")
        assert response_code == 200
