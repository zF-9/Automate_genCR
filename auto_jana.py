# import module
#import re 
import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# browser instance
options = Options()
options.add_argument("--headless=new")
browser = webdriver.Firefox(options=options)

# target URL
browser.get('#')
time.sleep(3)

#for i in range(2, 11, 1):
while(1):
    a_name = browser.find_element("xpath", '/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/div/span/span/a')
    a_name.click()

    time.sleep(3)
    # get URL parameters
    pyautogui.press('f6')
    # for copying the selected url
    pyautogui.hotkey('ctrl', 'c') 
    url = pyperclip.paste()
    print(url)

    # required : strip url to after KL=...
    #seperatist = "&KL="
    #parts = url.split(seperatist, 1)
    #url_params = parts[1].lstrip()

    #clean_string = re.sub(r'[^A-Za-z0-9]', '', url)
    #url_end = clean_string[-10:]

    # xpath_psswd 
    psswd_path = browser.find_element("xpath", '//*[@id="form1"]/table[2]/tbody/tr[2]/td/input')
    psswd = psswd_path.get_attribute('value')
    psswd_len = len(psswd)
    url_end = url[-psswd_len:]

    # check between strip.url == xpath_psswd value //
    if url_end == psswd:
        #jana pemohonan button : xpath = //*[@id="form1"]/p[1]/input
        generate = browser.find_element("xpath", '//*[@id="form1"]/p[1]/input')
        generate.click()

        time.sleep(3)
        # confirm button : xpath = //*[@id="gonext"]/input[1]
        confirm_ = browser.find_element("xpath", '//*[@id="gonext"]/input[1]')
        confirm_.click()

        time.sleep(5)


# Landing Page > list name (10) > check substring_end == password > emulate button click (Jana Permohonan) > click (YA) > wait page reload > repeat