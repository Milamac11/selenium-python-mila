import requests
import pytest


@pytest.mark.apitest
def test_get_all_products():
    response = requests.get("https://dummyjson.com/products/1")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    json_data = response.json()
    assert json_data ['id'] == 1
    assert json_data ['category'] == 'beauty'