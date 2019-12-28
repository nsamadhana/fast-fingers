from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys 
#To do:
#Navigate through logging in etc    
#Implement Recaptcha bypass 
#un:fastfingersbot@gmail.com   pw:Squat5buckets! 
#un:definitleynotabot pw:notabot1

#0.1s delay ~ 327 wpm 
browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/english")
inputBox = browser.switch_to_active_element()
email = "fastfingersbot@gmail.com"
pw = "notabot1"
logInXP = "/html/body/div[4]/div/div[4]/div/div[1]/div[5]/div[1]/div[1]/a"
unXP = 
pwXP = 


def main():
    textContent = browser.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    t = time.time() + minute
    #logging in 
    logIn = browser.find_element_by_xpath()
    logIn.click()
    print("after log in ")
    
    '''
    while time.time() < 60: 
        for word in wordList:
            time.sleep(0.1)
            parseWord(word)
    '''
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

        






