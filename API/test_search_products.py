import requests
import pytest


@pytest.mark.apitest
def test_search_products():
    response = requests.get("https://dummyjson.com/products/search", params={"q" : "phone"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"