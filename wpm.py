from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox() #type is of webdriver 
browser.get("https://10fastfingers.com/typing-test/english")

print("retreiving parent")
try: 
    row1 = browser.find_element_by_id("row1") #Grab div parent of span text 
    print("PARENT CONTAINER SUCCESFULLY RETRIEVED")
except: 
    print("Failed to retrieve parent parent container")
    pass


children = row1.find_elements_by_tag_name("span")
print("Post child retrieval")

for item in children: #Stopping at last span element seen by the page 
    print(item.text) #type of item: str 




