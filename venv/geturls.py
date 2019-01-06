from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def geturllist(typeofurl):
    searchlist=input("Search something:")
    results = google_search(searchlist, "AIzaSyDVrcTrFfUahWlwzZb5jv2SxwteduSAt3o", "004241604990378561825:xmcdndj5vti", num=10)
    urllist=[]
    requrls=[]
    for result in results:
        if typeofurl in result['link']:
            requrls.append(result['link'])
        else:
            urllist.append(result['link'])
    return requrls


