"""
    This python file a supporting file for fresh_tomatoes.py.
    It define multiple instances of the movie then store them in a list.
    ''fresh_tomatoes.open_movies_page'' function uses the list to generate a
    movie website.

    example:
    movie = media.Movie(
        "Title", "Duration_of_the_movie","Main_actors", "Youtube_URL",
        "Storyline", "Poster_image_URL
    )
"""

import media
import fresh_tomatoes


toy_story = media.Movie(
    "Toy Story", 81, "Joss Whedon, Andrew Stanton",
    "https://www.youtube.com/watch?v=4KPTXpQehio",
    "A story of toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
)

avatar = media.Movie(
    "Avatar", 161,
    "Sam Worthington, Zoe Saldana, Stephen Lang",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "Aliean movie",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg"
)

school_of_rock = media.Movie(
    "School of Rock", 105, "Jack Black, Joan Cusack",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg"
)

ratatouille = media.Movie(
    "Ratatouille", 111, "Patton Oswalt, Ian Holm, Lou Romano",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk",
    "Arat is a chef in Paris",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg"
)

midnight_in_paris = media.Movie(
    "Midnight in Paris", 94, "Kathy Bates, Adrien Brody, Carla Bruni",
    "https://www.youtube.com/watch?v=FAfR8omt-CY", "Goint back in time",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg"  # noqa
)


hunger_games = media.Movie(
    "Hunger Games", 142, "Jennifer Lawrence, Josh Hutcherson",
    "https://www.youtube.com/watch?v=SMGRhAEn6K0", "A Good movie",
    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg"
)

#store all the movies in a list
movies = [
    toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
    hunger_games
]

#Create movie website by using this function
fresh_tomatoes.open_movies_page(movies)

