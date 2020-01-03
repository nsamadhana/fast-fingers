from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys 
#To do:   
#Bypass anticheat
#0.1s delay ~ 300 wpm (5 keystrokes = 1 word)
 
driver = webdriver.Firefox()
driver.get("https://10fastfingers.com/typing-test/english")
email = "fastfingersbot@gmail.com"
password = "notabot1"
lPath = "/html/body/div[4]/div/div[4]/div/div[1]/div[5]/div[1]/div[1]/a"
ePath = "//*[@id='UserEmail']"
pPath = "//*[@id='UserPassword']"
nPath = "/html/body/div[2]/div/nav/div[2]/ul[4]/li[2]/span[1]/a" #notificatins 
aPath = "/html/body/div[3]/div/div/div[2]/ul/li/a"
acPath = "/html/body/div[4]/div[1]/div[4]/div/div/div[1]/table/tbody/tr[1]/td[1]/a"
startPath = "//*[@id='start-btn']"

def main():
    logIn()
    time.sleep(3) 
    textContent = driver.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    for word in wordList:
        time.sleep(0.1)
        parseWord(word)
    driver.find_element_by_xpath(nPath).click() 
    driver.find_element_by_xpath(aPath).click()
    driver.find_element_by_xpath(acPath).click()
    driver.find_element_by_xpath(startPath) #Failing to find start, find child instead 

    #Parse image to text here

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

        






