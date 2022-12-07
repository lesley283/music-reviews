from app.music_reviews import fetch_spotify_data
from app.search_reviews import reverse_list

def test_data_fetching():

    data = fetch_spotify_data("Lavender Haze")
    assert isinstance(data, dict)

    # check if first song in list has all of the required keys
    items = data["tracks"]["items"][0]
    assert isinstance(items, dict)
    assert "name" in items.keys()
    assert "id" in items.keys()
    assert "artists" in items.keys()
    assert "album" in items.keys()


def test_reverse_list():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    reversed_list = [7, 6, 5, 4, 3]
    assert reverse_list(test_list) == reversed_list

    test_list = [1, 2, 3]
    reversed_list = [3, 2, 1]
    assert reverse_list(test_list) == reversed_list
