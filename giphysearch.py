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
    print(phrase(qry))
    return res.data[0].url

