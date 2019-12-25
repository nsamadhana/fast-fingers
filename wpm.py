from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys 

browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/english")
actions = ActionChains(browser)
inputBox = browser.switch_to_active_element()
debug = open("debug.txt","w") 

def main():
    textContent = browser.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    print(wordList)
    for word in wordList:
        parseWord(word)
 
    
def parseWord(word):  
    assert type(word) is str
    for letter in word: 
        inputBox.send_keys(letter)
    inputBox.send_keys(Keys.SPACE)
     
def cleanUp(arr):
    assert len(arr) > 1 
    temp = ""
    for item in arr:
        temp += item
    return temp.split("|")

if __name__ == "__main__": 
    main()

        






