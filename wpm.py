from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver import ActionChains
import time
import sys
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\nevan\AppData\Local\Tesseract-OCR\tesseract.exe'
 
#To do:   
#Bypass anticheat
#0.1s delay ~ 300 wpm (5 keystrokes = 1 word)
 
driver = webdriver.Firefox()
email = "fastfingersbot@gmail.com"
password = "notabot1"
lPath = "/html/body/div[4]/div/div[4]/div/div[1]/div[5]/div[1]/div[1]/a"
ePath = "//*[@id='UserEmail']"
pPath = "//*[@id='UserPassword']"
nPath = "/html/body/div[2]/div/nav/div[2]/ul[4]/li[2]/span[1]/a" #notifications 
aPath = "/html/body/div[3]/div/div/div[2]/ul/li/a"
acPath = "/html/body/div[4]/div[1]/div[4]/div/div/div[1]/table/tbody/tr[1]/td[1]/a"
startPath = "//*[@id='start-btn']"
imgPath = "/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]/img"

def main():
    driver.get("https://10fastfingers.com/typing-test/english")
    time.sleep(1)
    logIn() 
    time.sleep(3)
    '''
    textContent = driver.find_element_by_id('wordlist').get_attribute('textContent')
    wordList = cleanUp(textContent)
    for word in wordList:
        time.sleep(0.1)
        parseWord(word)
       ''' 
    driver.find_element_by_xpath(nPath).click() 
    driver.find_element_by_xpath(aPath).click()
    driver.find_element_by_xpath(acPath).click()
    driver.find_element_by_id("start-btn").click()
    #Parse image to text here
    imgUrl = driver.find_element_by_xpath(imgPath).get_attribute("src")
    text = imgParser(imgUrl)
    text.split()
    print(text)
    #Switch back to first tab 
    driver.switch_to.window(driver.window_handles[0])

    
def logIn():
    driver.find_element_by_xpath(lPath).click()
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

def imgParser(url):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    driver.get_screenshot_as_file('image.png')
    im = Image.open('image.png')
    return(tess.pytesseract.image_to_string(im))
    
if __name__ == "__main__": 
    main()

        






