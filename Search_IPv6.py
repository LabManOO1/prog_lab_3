import re
import requests


class CheckIPv6:
    """
    CheckIPv6
    Поиск IPv6 адресов в строке, в файле или по сайту

    pattern - регулярное выражение
    """
    def __init__(self):
        self.pattern = r"((?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})"  # Регулярное выражение

    def check_string(self, mystring: str):  # Поиск в строке
        return re.findall(self.pattern, mystring)

    def check_file(self):  # Поиск в файле
        try:
            with open("IPv6.txt", encoding="utf-8") as file:
                mystring = file.read()
                return self.check_string(mystring)
        except Exception as error:
            return print(f"Ошибка при открытия файла: {error}")

    def check_website(self):  # Поиск по веб-странице
        try:
            website = requests.get("https://habr.com/ru/articles/773708/")
            website.raise_for_status()
            return self.check_string(website.text)
        except Exception as error:
            return f"Ошибка чтения страницы: {error}"


if __name__ == "__main__":
    value = 1
    while value != 0:  # Интерфейс
        search = CheckIPv6()
        value = int(input("Выберете действие:\n1 - Поиск по строке\n2 - Поиск по файлу\n3 - Поиск по веб-странице\n0"
                          " - Выход\n"))
        if value == 1:
            line = input("Введите строку:\t")
            result = search.check_string(line)
            if not result:
                print("Нет совпадений!")
            else:
                print(result)
        if value == 2:
            result = search.check_file()
            if not result:
                print("Нет совпадений!")
            else:
                print(result)
        if value == 3:
            result = search.check_website()
            if not result:
                print("Нет совпадений!")
            else:
                print(result)
