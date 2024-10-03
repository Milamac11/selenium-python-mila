import requests
import pytest


@pytest.mark.apitest
def test_search_products():
    test_data = {
    "title": "Automation QA Job",
    "description": "I know Automation API Testing Now! wow",
    "category": "beauty",
    "price": 50.99
    }
    response = requests.post("https://dummyjson.com/products/add", data=test_data)
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    json_data = response.json()
    assert json_data["title"] == "Automation QA Job"
    assert json_data["description"] == "I know Automation API Testing Now! wow"
    assert json_data["category"] == "beauty"
    assert json_data["price"] == '50.99'