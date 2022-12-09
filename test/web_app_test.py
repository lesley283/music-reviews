# this is the "test/web_app_test.py" file...

# testing a flask app. see:
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/flask.md#testing
# ... https://flask.palletsprojects.com/en/2.1.x/testing/

import pytest
from bs4 import BeautifulSoup

from web_app import create_app

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()

def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Welcome!</h1>" in response.data

def test_reviews(test_client):
    response = test_client.get("/add-review")
    assert response.status_code == 200
    assert b"<h2>Song Review Form</h2>" in response.data

def test_reviews_list(test_client):
    # CUSTOMIZED SYMBOL VIA URL PARAMS
    response = test_client.get("/add-review/list?song=Lavender Haze")
    assert response.status_code == 200
    assert b"<h2>Here are a list of songs that might fit your search criteria...</h2>" in response.data
    assert b"Lavender Haze by Taylor Swift" in response.data

def test_search_reviews(test_client):
    response = test_client.get("/search-review")
    assert response.status_code == 200
    assert b"<h2>Search Reviews</h2>" in response.data

def test_search_output(test_client):
    # CUSTOMIZED SYMBOL VIA URL PARAMS
    response = test_client.get("/search-review/output?review_level=artist&name=Taylor Swift")
    assert response.status_code == 200
    assert b"<h3>Here are reviews we found that match your search criteria...</h3>" in response.data
    assert b"<p>Here is a list of the most recent reviews...</p>" in response.data

def test_past_reviews(test_client):
    # CUSTOMIZED SYMBOL VIA URL PARAMS
    response = test_client.get("/past-reviews")
    assert response.status_code == 200
    # using beautifulsoup to parse the response
    soup = BeautifulSoup(response.data, features="html.parser")
    rows = soup.find("tbody").find_all("tr")
    assert len(rows) <= 10 # only want to show at most 10 reviews at a time
    assert b"<p>Here are songs other people have been listening to lately...</p>"
