from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys 

browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/english")
actions = ActionChains(browser)


try: 
    row1 = browser.find_element_by_id("row1") #Grab div parent of span text 
    print("PARENT CONTAINER SUCCESFULLY RETRIEVED")
except: 
    print("Failed to retrieve parent parent container")
    pass

children = row1.find_elements_by_tag_name("span")

print("test1")
for item in children: #Stopping at last span element seen by the page 
    print("test2")
    parseWord(self, item)


browser.close() #Closes firefox 


def parseWord(self, word):
    print("parseWord()")
    for letter in word: 
        actions.send_keys_to_element(, word) #word
        actions.send_keys_to_element(, Keys.SPACE) #Spacebar 
        






