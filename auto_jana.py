# import module
#import re 
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


#for i in range(2, 11, 1):
while(1):
    #force refresh
    #pyautogui.keyDown('ctrl')
    #pyautogui.keyDown('shift')
    #pyautogui.press('f5')
    #pyautogui.keyUp('shift')
    #pyautogui.keyUp('ctrl')


    pyautogui.moveTo(500, 777, duration=1)
    pyautogui.leftClick()
    #url = ''

    time.sleep(3)
    a_name = browser.find_element("xpath", '/html/body/table/tbody/tr[3]/td/table/tbody/tr[6]/td[1]/div/span/span/a')
    a_name.click()

    #force refresh
    #pyautogui.keyDown('ctrl')
    #pyautogui.keyDown('shift')
    #pyautogui.press('f5')
    #pyautogui.keyUp('shift')
    #pyautogui.keyUp('ctrl')



    #time.sleep(3)
    # get URL parameters
    
    # for copying the selected url
    time.sleep(5)
    url = ''
    #print("this old url " + url)
     
    pyautogui.press('f5')
    time.sleep(3)
    #pyautogui.press('f6')
    pyautogui.moveTo(588, 70, duration=1)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'c')
    url = pyperclip.paste()
    print(url)

    # required : strip url to after KL=...
    #seperatist = "&KL="
    #parts = url.split(seperatist, 1)
    #url_params = parts[1].lstrip()

    #clean_string = re.sub(r'[^A-Za-z0-9]', '', url)
    #url_end = clean_string[-10:]
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

    pyautogui.moveTo(500, 777, duration=1)
    pyautogui.leftClick()

    # xpath_psswd 
    psswd_path = browser.find_element("xpath", '//*[@id="form1"]/table[2]/tbody/tr[2]/td/input')
    psswd = psswd_path.get_attribute('value')
    psswd_len = len(psswd)
    _substring = '&KL='
    res = url.split(_substring, 1)
    result = res[1] if len(res) > 1 else ""
    #print(result)
    url_end = url[-psswd_len:]
    print("input_password: "+ psswd + " url_end: " + result)

    # check between strip.url == xpath_psswd value //
    #if result == psswd:  

    psswd_path.clear()
    time.sleep(5)
    psswd_path.send_keys(result)

    time.sleep(3)
    #jana pemohonan button : xpath = //*[@id="form1"]/p[1]/input
    generate = browser.find_element("xpath", '//*[@id="form1"]/p[1]/input')
    generate.click()

    time.sleep(7)
    # confirm button : xpath = //*[@id="gonext"]/input[1]
    confirm_ = browser.find_element("xpath", '//*[@id="gonext"]/input[1]')
    confirm_.click()

    time.sleep(7)
    pyautogui.press('f5')

    #time.sleep(3)
    #a_name = browser.find_element("xpath", '/html/body/table/tbody/tr[3]/td/table/tbody/tr[6]/td[1]/div/span/span/a')
    #a_name.click()
    #time.sleep(3)
    #browser.back()

'''
    time.sleep(3)
    a_name = browser.find_element("xpath", '/html/body/table/tbody/tr[3]/td/table/tbody/tr[6]/td[1]/div/span/span/a')
    a_name.click()

    pyautogui.press('f5')
    time.sleep(3)
    #jana pemohonan button : xpath = //*[@id="form1"]/p[1]/input
    generate = browser.find_element("xpath", '//*[@id="form1"]/p[1]/input')
    generate.click()

    time.sleep(3)
    # confirm button : xpath = //*[@id="gonext"]/input[1]
    confirm_ = browser.find_element("xpath", '//*[@id="gonext"]/input[1]')
    confirm_.click()

    time.sleep(5)
    pyautogui.press('f5')
'''

'''
    # Auto filled input field 
    else:
        #print("err")

        #force refresh
        #pyautogui.keyDown('ctrl')
        #pyautogui.press('f5')
        #pyautogui.keyUp('ctrl')

        # get URL parameters
        #pyautogui.press('f6')
        # for copying the selected url
        #time.sleep(3)
        #pyautogui.hotkey('ctrl', 'c') 
        #xurl = pyperclip.paste()
        #print(xurl)

        #xurl_end = xurl[-psswd_len:]
        #print("input_password: "+ psswd + " url_end: " + xurl_end)

        psswd_path.clear()
        time.sleep(3)
        psswd_path.send_keys(result)
        #jana pemohonan button : xpath = //*[@id="form1"]/p[1]/input
        generate = browser.find_element("xpath", '//*[@id="form1"]/p[1]/input')
        generate.click()

        time.sleep(3)
        # confirm button : xpath = //*[@id="gonext"]/input[1]
        confirm_ = browser.find_element("xpath", '//*[@id="gonext"]/input[1]')
        confirm_.click()

        time.sleep(5)
        pyautogui.press('f5')
'''



# Landing Page > list name (10) > check substring_end == password > emulate button click (Jana Permohonan) > click (YA) > wait page reload > repeat
