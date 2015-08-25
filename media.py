import webbrowser


class Movie():
    """This is a Movie class contains title, duration, actor, trailer_url,
    movie_storyline, poster_image.
    """

    def __init__(self, movie_title, duration, actor, trailer_youtube,
                 movie_storyline, poster_image):
        # Constructor of Movie class
        self.title = movie_title
        self.duration = duration
        self.actor = actor
        self.trailer_youtube_url = trailer_youtube
        self.storyline = movie_storyline
        self.poster_image_url = poster_image

    def show_trailer(self):
        # open trailer in webbrowser
        webbrowser.open(self.trailer_youtube_url)

    def show_actor(self):
        # print main actors name
        print self.actor
