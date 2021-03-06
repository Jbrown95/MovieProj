"""This file is what fresh_tomatoes uses for its movie list."""
import media
import fresh_tomatoes
# I followed along with the course, so the first 2 movies should be very close
# to what was done there.
# defining instances of class "Movie" to be added to list "Movies"
ToyStory = media.Movie("Toy Story", "A Story about toys that live",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                       "https://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",  # noqa
                       "Tom Hanks")
Avatar = media.Movie("Avatar",
                     "marine in space",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",  # noqa
                     "None")
ShawshankRedemption = media.Movie("Shawshank Redemption",
                                  "Triumph of a man wrongly accused of murder",
                                  "https://www.youtube.com/watch?v=6hB3S9bIaco",  # noqa
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                                  "Morgan Freeman")
Movies = [ToyStory, Avatar, ShawshankRedemption]  # Used by fresh_tomatoes
fresh_tomatoes.open_movies_page(Movies)  # running fresh_tomatoes
