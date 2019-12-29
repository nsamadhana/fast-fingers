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
driver = webdriver.Firefox()
driver.get("https://10fastfingers.com/typing-test/english")
email = "fastfingersbot@gmail.com"
password = "notabot1"
lPath = "/html/body/div[4]/div/div[4]/div/div[1]/div[5]/div[1]/div[1]/a"
ePath = "//*[@id='UserEmail']"
pPath = "//*[@id='UserPassword']"


def main():
    logIn()
    time.sleep(5)
    textContent = driver.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    limit = time.time() + 60

    while time.time() < limit: 
        for word in wordList:
            time.sleep(0.15)
            parseWord(word)
    

def logIn():
    temp = driver.find_element_by_xpath(lPath)
    temp.click()
    em = driver.find_element_by_xpath(ePath)
    em.click()
    em.send_keys(email)
    pw = driver.find_element_by_xpath(pPath)
    pw.click()
    pw.send_keys(password)
    pw.send_keys(Keys.ENTER)

def parseWord(word):  
    assert type(word) is str
    for letter in word: 
        driver.switch_to.active_element.send_keys(letter)
    driver.switch_to.active_element.send_keys(Keys.SPACE)
     
def cleanUp(arr):
    assert len(arr) > 1 
    temp = ""
    for item in arr:
        temp += item
    return temp.split("|")

if __name__ == "__main__": 
    main()

        






