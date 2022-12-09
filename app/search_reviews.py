# this is the "music_reviews.py" file...

# Allows user to search reviews and view average ratings

import pickle
from itertools import islice

def reverse_list(original_list, num):
    """Return newest 5 reviews by reversing list"""
    new_list = list(islice(reversed(original_list), 0, num))
    return new_list

def load_pickle_data():
    """Load data stored in a pickle file."""
    # load data from pickle file back to memory

    try:
        with open('reviews.pk', 'rb') as rfp:
            all_reviews = pickle.load(rfp)
    except EOFError:
        all_reviews = [] # if the file is empty, the list of all reviews should just be empty

    return all_reviews

def load_matching_reviews(search_input, review_level, all_reviews):
    """Return review information that matches search criteria"""
    avg_rating = []
    match_reviews = []
    match_user = []
    match_song = []

    for review in all_reviews:
        if (review_level == "artist" and search_input == review["artist"].upper()) or (review_level == "song" and search_input == review["title"].upper()) or (review_level == "album" and search_input == review["album"].upper()):
            avg_rating.append(review["rating"])
            match_reviews.append(review["review"])
            match_user.append(review["user"])
            match_song.append(review["title"])

    return avg_rating, match_reviews, match_user, match_song

def reviews_output(avg_rating, match_reviews, match_user, match_song):
    """Return review output, including 5 most recent reviews and average rating"""

    avg_rating = [int(x) for x in avg_rating]
    rating_output = sum(avg_rating) / len(avg_rating)
    rating_output = round(rating_output, 2)

    # reverse list (since most recent reviews are at the back of the list)
    reviews = reverse_list(match_reviews, 5)
    ratings = reverse_list(avg_rating, 5)
    users = reverse_list(match_user, 5)
    song = reverse_list(match_song, 5)

    return rating_output, reviews, ratings, users, song

if __name__ == "__main__":

    while True:
        review_level = input("Please input at what level you would like to view reviews for: 'song', 'artist', or 'album': ").lower()
        review_level = review_level.lower() #convert to lowercase to compare to list of options without case sensitivity
        valid_choice = ["song", "artist", "album"]
        if review_level in valid_choice:
            break
        else:
            print("Please make sure your input is one of the following, 'song', 'artist', or 'album'.")

    all_reviews = load_pickle_data()

    search_input = input("What " + review_level + " would you like to view the average rating for? ")
    search_input = search_input.upper() # convert to uppercase to compare to list of reviews without case sensitivity

    avg_rating, match_reviews, match_user, match_song = load_matching_reviews(search_input, review_level, all_reviews)

    if len(avg_rating) == 0: # list is empty
        print("There seems to be no reviews for that particular " + review_level + ". Please make sure you have entered the name correctly or leave a review yourself!")
        quit()

    rating_output, reviews, ratings, users, song = reviews_output(avg_rating, match_reviews, match_user, match_song)

    print("Here is the average rating for " + search_input.upper() + " based on all user reviews: " + str(rating_output))
    print("Here are a list of recent reviews...")
    print("-------------------")

    count = 0
    for x in song:
        print("Song: " + x)
        print("Reviews: " + reviews[count])
        print("Rating: " + str(ratings[count]))
        print("User: " + users[count])
        print("-------------------")
        count = count + 1
