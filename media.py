import webbrowser
class Movie():
    """THIS IS DOCUMENTATION """
    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self,movie_title,movie_storyline,trailer_youtube,
                poster_image, noteable_actors_list):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube
        self.poster_image_url = poster_image
        self.noteable_actors = noteable_actors_list

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
