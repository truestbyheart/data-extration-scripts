from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


# setting up the browser
root = os.getcwd()
browser = webdriver.Chrome(executable_path=root + "/chromedriver")

# using the browser
list = ["https://www.zoominfo.com/c/Apple-inc/2441797",
        "https://www.zoominfo.com/p/Elon-Musk/3160180912"]
i = 0
for target_list in list:
    browser.get(target_list)
    html = browser.page_source

    # create a txt file to store data
    txt = open(root+"/txt/data"+ str(i) +".txt", "w")
    txt.write(html)
    txt.close()  # 1

    # To the next page
    time.sleep(3)
    browser.implicitly_wait(3)
    i += 1


