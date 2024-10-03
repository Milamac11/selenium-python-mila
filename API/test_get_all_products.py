import requests
import pytest


@pytest.mark.apitest
def test_get_all_products():
    response = requests.get("https://dummyjson.com/products")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"