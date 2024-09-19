import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("item",
                         [
                             "Nikola Tesla",
                             "Dodge Viper"
                         ])
def test_wiki_items(browser, item):
    browser.get("https://www.wikipedia.org/")
    search = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(browser.find_element(By.ID, "searchInput")))
    search.send_keys(item + Keys.ENTER)
    assert browser.title == item + ' - Wikipedia'
    time.sleep(2)




