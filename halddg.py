from google import google
def gsearch(qry):
    res = google.search(qry)
    return (res[0].link)

print (gsearch("google"))
