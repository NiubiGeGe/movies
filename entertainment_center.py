import media
import fresh_tomatoes


#toy_story = media.Movie("Toy Story", "A story of toys", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio")


#avatar = media.Movie("Avatar", "Aliean movie", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")


school_of_rock = media.Movie("School of Rock", 105, "Jack Black, Joan Cusack", "https://www.youtube.com/watch?v=XCwy6lW5Ixc", "Using rock music to learn", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg")


#ratatouille = media.Movie("Ratatouille", "Arat is a chef in Paris", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")


#midnight_in_paris = media.Movie("Midnight in Paris", "Goint back in time", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")


#hunger_games = media.Movie("Hunger Games", "A Good movie", "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=SMGRhAEn6K0")


#movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

movies = [school_of_rock]

fresh_tomatoes.open_movies_page(movies)

school_of_rock.show_actor()

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__module__)
