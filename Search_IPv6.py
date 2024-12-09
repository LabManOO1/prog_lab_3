import re
import requests
#import urllib



class Check_IPv6:
    def __init__(self):
        self.pattern = r"((?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})"

    def check_string(self, string: str):
        return re.findall(self.pattern, string)

    def check_file(self):
        try:
            with open("IPv6.txt", encoding="utf-8") as file:
                string = file.read()
                return self.check_string(string)
        except Exception as error:
            return print(f"Ошибка при открытия файла: {error}")

    def check_url(self):
        try:
            website = requests.get("https://habr.com/ru/articles/773708/")
            website.raise_for_status()
            print(website.text)
            return self.check_string(website.text)
        except Exception as error:
            return f"Ошибка чтения страницы: {error}"



if __name__ == "__main__":
    a = Check_IPv6()
    a.check_url()
