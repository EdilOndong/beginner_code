from bs4 import BeautifulSoup
import requests
import os


def get_url(url):
    base_url = requests.get(url)
    return base_url.content


def scarp(url, data, filename):
    try:
        soup = BeautifulSoup(url, "html.parser")
        result = soup.find(id=data)
        with open(filename, "w") as files:
            files.write(result.text)
            current_dir = os.getcwd()
            if filename in current_dir:
                print("The Has Been Write To", current_dir)
            else:
                print("The File Already Exist In", current_dir)
    except requests.exceptions.ConnectionError:
        pass


if __name__ == "__main__":
    scarp(get_url("http://sabahchess.com/v1/index.php/sca-news/792-ardian-syah-muming-menjuarai-kejohanan-catur-oku-lions-sca-2019"), "ja-content", "data.txt")
