# this is the "music_reviews.py" file...

# Allows user to search reviews and view average ratings

from app.music_reviews import all_reviews

# Finding average user rating

while True:
    avg_input = input(
        "Please input at what level you would like to view reviews for: 'song', 'artist', or 'album': ")
    if avg_input.lower() == "song":
        break
    elif avg_input.lower() == "artist":
        break
    elif avg_input.lower() == "album":
        break
    else:
        print("Please make sure your input is one of the following, 'song', 'artist', or 'album'.")

##### NEED TO REFACTOR CODE #####
avg_rating = []
match_reviews = []
match_user = []
if avg_input.lower() == "song":
    avg_song = input(
        "What song would you like to view the average rating for? ")
    for review in all_reviews:
        if review["title"].lower() == avg_song.lower():
            avg_rating.append(review["rating"])
            match_reviews.append(review["review"])
            match_user.append(review["user"])
    if not avg_rating:
        print("There seems to be no reviews for that particular song. Please make sure you have entered the title correctly, or leave a review for that song!")
    else:
        rating_output = sum(avg_rating) / len(avg_rating)
        print("Here is the average rating for " + avg_song.upper() +
              " based on all user reviews: " + str(rating_output))
        print("-------------------")
        print("Here are a list of recent reviews...")
        count = 0
        while count <= 5 and count <= (len(match_reviews) - 1):
            print("Reviews: " + match_reviews[count])
            print("Rating: " + str(avg_rating[count]))
            print("User: " + match_user[count])
            count = count + 1
elif avg_input.lower() == "artist":
    avg_artist = input(
        "What artist would you like to view the average rating for? ")
    for review in all_reviews:
        if review["artist"].lower() == avg_artist.lower():
            avg_rating.append(review["rating"])
            match_reviews.append(review["review"])
            match_user.append(review["user"])
    if not avg_rating:
        print("There seems to be no reviews for that particular artist. Please make sure you have entered the name correctly, or leave a review for that artist!")
    else:
        rating_output = sum(avg_rating) / len(avg_rating)
        print("Here is the average rating for the song " + avg_artist.upper() +
              " based on all user reviews: " + str(rating_output))
        print("-------------------")
        print("Here are a list of recent reviews...")
        count = 0
        while count <= 5 and count <= (len(match_reviews) - 1):
            print("Reviews: " + match_reviews[count])
            print("Rating: " + str(avg_rating[count]))
            print("User: " + match_user[count])
            count = count + 1
elif avg_input.lower() == "album":
    avg_album = input(
        "What album would you like to view the average rating for? ")
    for review in all_reviews:
        if review["album"].lower() == avg_album.lower():
            avg_rating.append(review["rating"])
            match_reviews.append(review["review"])
            match_user.append(review["user"])
    if not avg_rating:
        print("There seems to be no reviews for that particular album. Please make sure you have entered the name correctly, or leave a review for that album!")
    else:
        rating_output = sum(avg_rating) / len(avg_rating)
        print("Here is the average rating for the album " + avg_album.upper() +
              " based on all user reviews: " + str(rating_output))
        print("-------------------")
        print("Here are a list of recent reviews...")
        count = 0
        while count <= 5 and count <= (len(match_reviews) - 1):
            print("Reviews: " + match_reviews[count])
            print("Rating: " + str(avg_rating[count]))
            print("User: " + match_user[count])
            count = count + 1
