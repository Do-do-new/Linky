from pip._vendor import requests  # absolutely awesome library with "HTTP Requests for Humans"
from Settings import Settings

if __name__ == "__main__":
    r = requests.get('http://unbolt.me', proxies=Settings.proxies)
    print(r.text)
