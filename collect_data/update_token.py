from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def get_token(url):

    first = ''
    second = ''
    length = len(url)
    
    for index, character in enumerate(url):
        if character == '=':
            first = index + 1
            break
            
    
    for index, character in enumerate(reversed(url)):
        if character == '&':
            second = (length - 1) - index
            break
        

    return url[first:second]
    

# create the browser and navigate to starting page
browser = webdriver.Firefox() # Get local session of firefox
browser.get("https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token") 
try:
    email = browser.find_element_by_id("email")
except NoSuchElementException:
    assert 0, "can't find email box"
    
email.send_keys("s-seperez@lwsd.org")

try:
    password = browser.find_element_by_id("pass")
except NoSuchElementException:
    assert 0, "can't find password box"

password.send_keys("AnnaCamp7!")
try: 
    submit = browser.find_element_by_id("loginbutton")
except NoSuchElementException:
    assert 0, "can't find submit button"
    
submit.send_keys(Keys.RETURN)


# creating the actual token
url = browser.current_url
token = get_token(url)
print token

browser.close()
