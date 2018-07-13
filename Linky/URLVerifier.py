import requests
from Settings import Settings


class URLVerifier:

    def isValid(self, url):
        code = self.getCode(url)  # like notorious 404...
        valid = code not in Settings.errorCodes
        return valid

    def getCode(self, url):
        try:
            resp = requests.get(url, proxies=Settings.proxies)
            code = resp.status_code
        except requests.exceptions.SSLError:
            code = 404
        return code
