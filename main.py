# from bs4 import BeautifulSoup
# from urllib.request import urlopen

from utilities.data_fetcher import downloader
from utilities.soup import C2,C2_index
from utilities.tools import get_root_path

math_index_url = "https://jupiter.math.nycu.edu.tw/~smchang/1101/C2.html"
math_url = "https://jupiter.math.nycu.edu.tw/~smchang/1101/C2"

if __name__ == "__main__":
    res = downloader(math_index_url)
    data = C2_index(text=res,root=get_root_path(math_index_url))
    # write json file
    res = downloader(math_url)
    data = C2(res)
