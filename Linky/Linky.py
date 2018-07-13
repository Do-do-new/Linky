from Settings import Settings
from Parsers.ParserASCII import ParserASCII

if __name__ == "__main__":

    parser = ParserASCII()
    print(parser.parseFile(Settings.testFilePath))

    # soup = BeautifulSoup(data)
    # for link in soup.find_all('a'):
    #     print(link)

