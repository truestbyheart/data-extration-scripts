from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import os
from random import choice

# proxy server


def get_proxy():
    url = "https://sslproxies.org/"
    r = requests.get(url)
    static_page = BeautifulSoup(r.content, "html5lib")
    return {"https": choice(list(map(lambda x: x[0]+':'+x[1], list(
        zip(map(lambda x: x.text, static_page.findAll('td')[::8]),
            map(lambda x: x.text, static_page.findAll('td')[1::8]))))))}

def proxy_integrity(request_type, url, **kwargs): 
    while 1:
        try:
            proxy = get_proxy()
            r = requests.request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            print(r.content)
            break
        except:
            pass
    return proxy


# setting up the browser
root = os.getcwd()
PROXY = proxy_integrity("get", "https://youtube.com")
print(PROXY)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome(executable_path=root + "/chromedriver", options=chrome_options)

# using the browser
list = ["https://www.zoominfo.com/c/Apple-inc/2441797",
        "https://www.zoominfo.com/p/Elon-Musk/3160180912"]
i = 0
for target_list in list:
    browser.get(target_list)
    html = browser.page_source

    # create a txt file to store data
    txt = open(root+"/txt/data" + str(i) + ".txt", "w")
    txt.write(html)
    txt.close()  # 1

    # To the next page
    time.sleep(3)
    browser.implicitly_wait(3)
    i += 1
