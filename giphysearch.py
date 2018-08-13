import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import haltoken

g = giphy_client.DefaultApi()
api_key = haltoken.giphy()

def phrase(qry):
    return qry.replace(" ","+")

def search(qry):
    res = g.gifs_search_get(api_key, phrase(qry), limit=2)
    try:
        link = res.data[0].url
    except:
        link = "I could not find any results, so I found a random gif. " + g.gifs_random_get(api_key).data.url
    return link

if __name__ == "__main__":
    search("mew and boo")
