from Settings import Settings
from Parsers.ParserASCII import ParserASCII
from URLVerifier import URLVerifier

if __name__ == "__main__":

    parser = ParserASCII()
    urls = parser.parseFile(Settings.testFilePath)

    verifier = URLVerifier()
    for url in urls:
        valid = verifier.isValid(url)
        print(url, valid)


    # soup = BeautifulSoup(data)
    # for link in soup.find_all('a'):
    #     print(link)

