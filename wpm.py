from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys 

#Implement timer to break after 60 seconds 

browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/english")
inputBox = browser.switch_to_active_element()
minute = 60

def main():
    wpm = sys.argv[1]
    textContent = browser.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    t = time.time() + minute
    #Stop sending keys after one minute 
    while time.time() < t: 
        for word in wordList:
            time.sleep(0.250)
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

        






