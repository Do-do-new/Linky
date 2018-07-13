#
#   Singleton class for storing settings
#


class Settings:
    # class __Settings:
    #     def __init__(self, arg):
    #         self.val = arg

    #     def __str__(self):
    #         return repr(self) + self.val

    # instance = None

    # def __init__(self, arg):
    #     if not Settings.instance:
    #         Settings.instance = Settings.__Settings(arg)
    #     else:
    #         Settings.instance.val = arg

    # def __getattr__(self, name):
    #     return getattr(self.instance, name)

    proxies = {
        'http': 'http://i00109058:Salerdo100500@proxy.endress.com:8080',
        'https': 'https://i00109058:Salerdo100500@proxy.endress.com:8080',
    }

    filePath = "tst.txt"
