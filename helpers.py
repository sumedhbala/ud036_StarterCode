"""
Helper functions required to create the movie website.
"""
import httplib
import urlparse


def is_valid_url(url):
    """
    Helper that reads the header of the URL and prints a message
    if the url does not exist for debugging purposes.

    Args:
        url (str): The url to check.
    """
    # Split the url into host and path to the page.
    host, path = urlparse.urlsplit(url)[1:3]
    conn = httplib.HTTPConnection(host)
    # Read the header and not the entire content to save network traffic.
    conn.request("HEAD", path)
    # Check if the response if valid.
    if conn.getresponse().status >= 400:
        print 'link may be invalid'
    conn.close()
