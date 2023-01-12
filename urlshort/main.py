import os, sys
import requests

try:
    api = open("api.txt", "r")
    api = api.readlines()
    api = api[0]
except:
    print("No api.txt in your folder")
    os._exit(0)

try:
    url = sys.argv[1]
    alias = sys.argv[2]
except:
    print("Usage : shortx URL ALIAS")
    os._exit(0)

short_url = f"https://urlshortx.com/api?api={api}&url={url}&alias={alias}"
Send_url = f"https://xpshort.com/{alias}"

req = requests.get(short_url, allow_redirects=True)
print(short_url + "   Created [+]")
print()
print()
print(f"\n Url : '{Send_url}'")