# required module
import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# browser instance
options = Options()
#options.add_argument("--headless=new")
browser = webdriver.Firefox(options=options)

# target URL
browser.get('#')
time.sleep(10)

while(1):

    pyautogui.moveTo(500, 777, duration=1)
    pyautogui.leftClick()

    time.sleep(3)
    a_name = browser.find_element("xpath", '/html/body/table/tbody/tr[3]/td/table/tbody/tr[6]/td[1]/div/span/span/a')
    a_name.click()
    
    # for copying the selected url
    time.sleep(5)
    url = ''
     
    pyautogui.press('f5')
    time.sleep(3)
    pyautogui.moveTo(588, 70, duration=1)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'c')
    url = pyperclip.paste()
    print(url)

    '''
    def re_jana():
        #jana pemohonan button : xpath = //*[@id="form1"]/p[1]/input
        generate = browser.find_element("xpath", '//*[@id="form1"]/p[1]/input')
        generate.click()

        time.sleep(3)
        # confirm button : xpath = //*[@id="gonext"]/input[1]
        confirm_ = browser.find_element("xpath", '//*[@id="gonext"]/input[1]')
        confirm_.click()

        time.sleep(5)
    '''

    # idlling for copy + paste
    pyautogui.moveTo(500, 777, duration=1)
    pyautogui.leftClick()

    # xpath_psswd 
    psswd_path = browser.find_element("xpath", '//*[@id="form1"]/table[2]/tbody/tr[2]/td/input')
    psswd = psswd_path.get_attribute('value')
    psswd_len = len(psswd)
    _substring = '&KL='
    res = url.split(_substring, 1)
    result = res[1] if len(res) > 1 else ""
    url_end = url[-psswd_len:]
    print("input_password: "+ psswd + " url_end: " + result)

    psswd_path.clear()
    time.sleep(5)
    psswd_path.send_keys(result)

    time.sleep(3)
    #jana pemohonan button
    generate = browser.find_element("xpath", '//*[@id="form1"]/p[1]/input')
    generate.click()

    time.sleep(7)
    # confirm button
    confirm_ = browser.find_element("xpath", '//*[@id="gonext"]/input[1]')
    confirm_.click()

    time.sleep(7)
    pyautogui.press('f5')


# Landing Page > list name (10) > check params > params to text field > emulate button click (Jana Permohonan) > click (YA) > wait page reload > repeat
