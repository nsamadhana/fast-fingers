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
    textContent = browser.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    print(wordList)
    
    for item in wordList: #Stopping at last span element seen by the page 
        parseWord(item)


    browser.quit() 
    
def parseWord(word):  
    assert type(word) is str
    for letter in str(word): 
        actions.send_keys(letter).perform() #word
        actions.send_keys(Keys.SPACE).perform() #Spacebar 

def cleanUp(arr):
    assert len(arr) > 1 
    temp = ""
    for item in arr:
        temp += item
    return temp.split("|")
    

if __name__ == "__main__": 
    main()

        






