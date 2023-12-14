import urllib

url_file = lambda urlpath, fileid : urllib.requests.urlretrieve(urlpath, fileid)