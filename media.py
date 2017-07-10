"""
Contains the definition of the Movie Class
"""

from helpers import is_valid_url


class Movie(object):
    """
    Represents the details of the movie.

    Attributes:
        title (str): Name of the movie.
        poster_image_url (str): Link to the movie poster.
        trailer_youtube_url (str): Link to the movie trailer on youtube.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Initializes the movie object.

        Args:
            title (str): Name of the movie.
            poster_image_url (str): Link to the movie poster.
            trailer_youtube_url (str): Link to the movie trailer on youtube.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    @property
    def title(self):
        """
        str: Name of the movie
        """
        return self._title

    @property
    def poster_image_url(self):
        """
        str: Link to the movie poster.
        """
        return self._poster_image_url

    @property
    def trailer_youtube_url(self):
        """
        str: Link to the trailer of the movie on youtube.
        """
        return self._trailer_youtube_url

    # pylint: disable=missing-docstring
    @title.setter
    def title(self, title):
        # pylint: disable=attribute-defined-outside-init
        self._title = title

    @poster_image_url.setter
    def poster_image_url(self, poster_image_url):
        is_valid_url(poster_image_url)
        # pylint: disable=attribute-defined-outside-init
        self._poster_image_url = poster_image_url

    @trailer_youtube_url.setter
    def trailer_youtube_url(self, trailer_youtube_url):
        is_valid_url(trailer_youtube_url)
        # pylint: disable=attribute-defined-outside-init
        self._trailer_youtube_url = trailer_youtube_url
