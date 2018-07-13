import re


class ParserASCII:

    def parseFile(self, filePath):
        file = open(filePath, 'r')
        data = file.read()
        file.close()
        return self.parseString(data)

    def parseString(self, data):
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data)
        urls = list(set(urls))  # remove duplicates from the list
        return urls
