#! /usr/bin/python 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from serialcoms import TeamsSerial

ser = TeamsSerial("", 115200)

# Microsoft Teams login credentials
username = ""
password = ""

# Path to the saved Firefox profile
firefox_profile_path = "/home/pk/.mozilla/firefox"


# Set individual preferences from the saved Firefox profile

driver = webdriver.Firefox()

# Open Microsoft Teams login page
driver.get("https://teams.microsoft.com/")

# Wait for the page to load
sleep(5)

# Enter username and password
username_input = driver.find_element(By.XPATH, "//input[@name='loginfmt']")
username_input.send_keys(username)
username_input.send_keys(Keys.RETURN)

# Wait for the page to load
sleep(5)

# Enter username and password
username_input = driver.find_element(By.XPATH, "//input[@id='okta-signin-username']")
username_input.send_keys(username)

password_input = driver.find_element(By.XPATH, "//input[@id='okta-signin-password']")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete
sleep(30)


# Wait for the calendar page to load
xpath = "//div[@class='user-information-button']//span[@class='ts-skype-status visible']//span[@aria-hidden='true']//span[@class]"
while True:
    element =  driver.find_element(By.XPATH,xpath)     
    status = element.get_attribute("class")
    
    status = (list(status.split(" ")))[-1]

    print(status)

    ser.senddata(status+"\r\n")

    
    
    
    sleep(2)

driver.quit()
