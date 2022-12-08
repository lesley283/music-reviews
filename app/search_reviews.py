# this is the "music_reviews.py" file...

# Allows user to search reviews and view average ratings

import pickle
from itertools import islice

def reverse_list(original_list):
    """Return newest 5 reviews by reversing list"""
    new_list = list(islice(reversed(original_list), 0, 5))
    return new_list

if __name__ == "__main__":

    while True:
        avg_input = input("Please input at what level you would like to view reviews for: 'song', 'artist', or 'album': ").lower()
        avg_input = avg_input.lower()
        if avg_input == "song" or avg_input == "artist" or avg_input == "album":
            break
        else:
            print("Please make sure your input is one of the following, 'song', 'artist', or 'album'.")

    avg_rating = []
    match_reviews = []
    match_user = []

    # load data from pickle file back to memory
    with open('reviews.pk', 'rb') as rfp:
        all_reviews = pickle.load(rfp)

    search_input = input("What " + avg_input + " would you like to view the average rating for? ").lower()
    for review in all_reviews:
        if search_input == review["title"].lower() or search_input == review["artist"].lower() or search_input == review["album"].lower():
            avg_rating.append(review["rating"])
            match_reviews.append(review["review"])
            match_user.append(review["user"])
        if not avg_rating:
            print("There seems to be no reviews for that particular " + avg_input + ". Please make sure you have entered the name correctly or leave a review yourself!")
            quit()

    avg_rating = [int(x) for x in avg_rating]

    rating_output = sum(avg_rating) / len(avg_rating)
    print("Here is the average rating for " + search_input.upper() + " based on all user reviews: " + str(rating_output))
    print("Here are a list of recent reviews...")
    print("-------------------")

    # reverse list (since most recent reviews are at the back of the list)
    reviews = reverse_list(match_reviews)
    ratings = reverse_list(avg_rating)
    users = reverse_list(match_user)

    count = 0
    while count <= 5 and count <= (len(match_reviews) - 1):
        print("Reviews: " + reviews[count])
        print("Rating: " + str(ratings[count]))
        print("User: " + users[count])
        print("-------------------")
        count = count + 1
