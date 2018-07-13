from pip._vendor import requests  # absolutely awesome library with "HTTP Requests for Humans"

proxies = {
    'http': 'http://i00109058:Salerdo100500@proxy.endress.com:8080',
    'https': 'https://i00109058:Salerdo100500@proxy.endress.com:8080',
}

if __name__ == "__main__":
    r = requests.get('http://unbolt.me', proxies=proxies)
    print(r.text)
