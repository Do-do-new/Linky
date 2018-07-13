import requests

from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urlsplit, urlunsplit
import colorama
import re
import queue
import threading
from colorama import Fore
# import mimetypes

proxies = {
    'http': 'http://i00109058:Salerdo100500@proxy.endress.com:8080',
    'https': 'https://i00109058:Salerdo100500@proxy.endress.com:8080',
}


class check_link():
    def __init__(self, address):
        self.address = address

    def check(self, address):
        try:
            resp = requests.get(url=address, proxies=proxies)
            if resp.status_code in [400, 404, 403, 408, 409, 501, 502, 503]:
                print(Fore.RED + resp.status_code + "-" + resp.reason + "-->" +
                      address)
            else:
                print(Fore.GREEN + "no problem in-->" + address)

        except Exception as e:
            print(Fore.YELLOW + "{}-{}".format(e, address))
            pass


def pattern_adjust(a):
    try:
        if re.match('^#', a): return 0
        r = urlsplit(a)
        if r.scheme == '' and (r.netloc != '' or r.path != ''):
            d = urlunsplit(r)
            if re.match('^//', d):
                m = re.search('(?<=//)\S+', d)
                d = m.group(0)
                m = "https://" + d
                return m
        elif r.scheme == '' and r.netloc == '':
            return address + a
        else:
            return a
    except Exception as e:
        pass


def extract_link(address):
    tags = {'a': 'href', 'img': 'src', 'script': 'src', 'link': 'href'}
    for key, value in iter(tags.items()):
        try:

            res = requests.get(url=address, proxies=proxies)
            respText = res.text
            for link in BeautifulSoup(
                    respText, "html.parser", parse_only=SoupStrainer(key)):
                if link.has_attr(value):
                    p = pattern_adjust(link[value])
                    if p != 0 and str(p) != 'None':
                        newcheck = check_link(p)
                        newcheck.check(p)
                        if p not in hyperlinks:
                            hyperlinks.add(p)
                            if website.split('.')[1] in p:  # needs improvement
                                if not website.endswith(
                                    ('.png', '.jpeg', '.js', 'jpg')):
                                    q.put(p)
        except Exception as e:
            print(e, address)


def threader():
    while True:
        value = q.get()
        result = extract_link(value)
        q.task_done()


if __name__ == "__main__":
    colorama.init()
    q = queue.Queue()
    global hyperlinks, website
    hyperlinks = set()
    website = input("Please enter the website address: ")
    for x in range(30):
        t = threading.Thread(target=threader)
        t.deamon = True
        t.start()
    q.put(website.strip())
    q.join()
