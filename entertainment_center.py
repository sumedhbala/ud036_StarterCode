"""
Contains details of the Favorite movies.
"""
from media import Movie

# String representation for the different properties of the movie.
TITLE = "title"
POSTER_IMAGE_URL = "poster_image_url"
TRAILER_YOUTUBE_URL = "trailer_youtube_url"

# pylint: disable=line-too-long
# Favorite movies and its properties
FAV_MOVIES = [{TITLE: "The Shawshank Redemption",
               POSTER_IMAGE_URL: "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
               TRAILER_YOUTUBE_URL: "https://www.youtube.com/watch?v=RLw6hBFJ8bk"  # noqa
              },
              {TITLE: "Life Is Beautiful",
               POSTER_IMAGE_URL: "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",  # noqa
               TRAILER_YOUTUBE_URL: "https://www.youtube.com/watch?v=Q1qggoumYi0"  # noqa
              },
              {TITLE: "The Dark Knight",
               POSTER_IMAGE_URL: "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # noqa
               TRAILER_YOUTUBE_URL: "https://www.youtube.com/watch?v=qY3UkAHufLY"  # noqa
              }
             ]
# pylint: enable=line-too-long

# List of the favorite movie objects
MOVIES = [Movie(fav_movie[TITLE], fav_movie[POSTER_IMAGE_URL],
                fav_movie[TRAILER_YOUTUBE_URL])
          for fav_movie in FAV_MOVIES]
