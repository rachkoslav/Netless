import requests

# API - http://www.icndb.com/api/
def getRandomJoke:
    resp = requests.get("http://api.icndb.com/jokes/random")
    # Split the repose just before the start of the joke
    jokeWrap = resp.content.split("\"joke\"")
    # Get the joke and the text after it
    jokeAndCategory = jokeWrap[1].split(", \"")

    # Split the joke only and return
    joke = jokeAndCategory[0]
    return joke
