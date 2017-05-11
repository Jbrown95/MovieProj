import webbrowser
#I followed along with the course, so it should look very similar if not word
#for word in some parts.
class Movie():
    """THIS IS DOCUMENTATION """
    VALID_RATINGS = ["G","PG","PG-13","R"]
#creating constructor that will be used to create intances of the class. 
    def __init__(self,movie_title,movie_storyline,trailer_youtube,
                poster_image, noteable_actors_list):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube
        self.poster_image_url = poster_image
        self.noteable_actors = noteable_actors_list

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
