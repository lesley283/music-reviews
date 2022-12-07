from app.music_reviews import fetch_spotify_data

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
