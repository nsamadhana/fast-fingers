from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys 


browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/english")
actions = ActionChains(browser)
minute = 60 
debug = open("debug.txt","w") 

def main():
    textContent = browser.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    for item in wordList:
        print(item)
        parseWord(item)
    

    browser.quit() 
    
def parseWord(word):  
    time.sleep(1.0) 
    assert type(word) is str
    for letter in word: 
        print(letter)
        actions.send_keys(letter) #word
    actions.send_keys(Keys.SPACE).perform() #Spacebar
    
    

def cleanUp(arr):
    assert len(arr) > 1 
    temp = ""
    for item in arr:
        temp += item
    return temp.split("|")
    

if __name__ == "__main__": 
    main()

        






