# from bs4 import BeautifulSoup
# from urllib.request import urlopen

from utilities.data_fetcher import downloader

math_index_url = "https://jupiter.math.nycu.edu.tw/~smchang/1101/C2.html"
math_url = "https://jupiter.math.nycu.edu.tw/~smchang/1101/C2"

if __name__ == "__main__":
    res = downloader(math_index_url)
    print(res)
