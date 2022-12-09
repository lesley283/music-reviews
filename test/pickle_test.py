
from app.search_reviews import load_pickle_data

# test that the data that is loaded from the pickle file looks correct
def test_pickle_data():

    data = load_pickle_data()
    assert isinstance(data, list)

    # check if first item in list (first review recorded) has neccessary attributes
    review = data[0]
    assert isinstance(review, dict)
    assert "title" in review.keys()
    assert "album" in review.keys()
    assert "artist" in review.keys()
    assert "review" in review.keys()
    assert "rating" in review.keys()
    assert "user" in review.keys()
