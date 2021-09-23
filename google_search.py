from progress.bar import Bar
from googlesearch import search
import webbrowser
import time


def progress_bar():
    bar = Bar("Processing" + " : ", max=10)
    for i in range(10):
        time.sleep(1)
        bar.next()
    bar.finish()


def google_search(url, tld):
    url_data = []
    for data in search(url, tld=tld, num=10, stop=10, lang="en", pause=1.0):
        url_data.append(data)
        for result in url_data:
            print(result)


def open_page(url):
    if url == "":
        print("Please Provide A Link To Open")
    else:
        return webbrowser.open(url)


if __name__ == '__main__':
    target_url = input("Please Enter Keyword To Search : ")  # Enter Keyword To Search Here
    tld_name = input("Please Enter The TLD Name (eg : com) : ")  # Enter The TLD Name
    progress_bar()
    google_search(target_url, tld_name)
    url_to_open = input("Please Enter Put A Link To Open : ") # Open The Link You Want To Open
    open_page(url_to_open)