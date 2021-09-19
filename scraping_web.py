from progress.bar import Bar
import requests
from bs4 import BeautifulSoup


def get_url(url):
    url_requests = requests.get(url)
    return url_requests.content


def scrap_url(url, data_want_scrap):
    info = BeautifulSoup(url, "html.parser")
    info.find(data=data_want_scrap)
    print(info.text)
    return info


if __name__ == '__main__':
    target_url = input("Please Enter Target URL : ")
    # Enter Your Target URL Here
    target_element = input("Please Target HTML Elements : ")
    # Enter Your Target HTML Elements for Target URL @ Inspect Element
    with Bar("Crawling :", max=10) as bars:
        for i in range(10):
            bars.next()
            result = scrap_url(get_url(target_url), target_element)
            print(result.text)
        bars.finish()

