from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys 

browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/english")
actions = ActionChains(browser)

def main():
    '''
    try: 
        row1 = browser.find_element_by_id("row1") #Grab div parent of span text 
        print("PARENT CONTAINER SUCCESFULLY RETRIEVED")
    except: 
        print("Failed to retrieve parent parent container")
        pass

    children = row1.find_elements_by_tag_name("span")
    '''
    
    textContent = browser.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    print(wordList)
    

    #for item in wordList: #Stopping at last span element seen by the page 
     #   parseWord(item)


    browser.quit() #Quit firefox 
    
def parseWord(word):  
    print("parseWord()")
    for letter in str(word): 
        actions.send_keys(word) #word
        actions.send_keys(Keys.SPACE) #Spacebar 

def cleanUp(arr):
    temp = ""
    for item in arr:
        temp += item
    return temp.split("|")
    

if __name__ == "__main__": 
    main()

        






