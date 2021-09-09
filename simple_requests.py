# simple python script to download website to content to txt file
import requests


def get_data(url, filename, extension):
    try:
        url = requests.get(url)
        content = url.content
        with open(filename, extension) as files:
            files.write(str(content))
            if files:
                print("The file has been download")
            else:
                print("The data cannot download")
    except requests.exceptions.ConnectionError as msg:
        print(msg)


website = "https://www.bbc.com/news/technology-58437753"
file_name = "data.txt"
method = "w"
get_data(website, file_name, method)