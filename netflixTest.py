from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import datetime
from UserInfo import netflixUsername, netflixPassword
from PIL import Image
#from Screenshot import Screenshot_clipping

import sys


original_stdout = sys.stdout # Save a reference to the original standard output

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
'''
with open('TestReport.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('This message will be written to a file.')
    print('this is the second.')
    print('testing for three')
    sys.stdout = original_stdout # Reset the standard output to its original value
'''

sourceFile = open('demo.txt', 'w')

driver = webdriver.Chrome(chrome_options=option) 
driver.get("https://www.netflix.com/")
x = datetime.datetime.now()
driver.save_screenshot("00_netflixAnaMenu.png")
screenshot = Image.open("00_netflixAnaMenu.png")
#screenshot.show()

#STEP1: Netflix login butonuna tıkla 
try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()
    time.sleep(2)
    driver.save_screenshot("01_netflixLogin.png")
    #screenshot = Image.open("netflixLogin.png")
    
    print("Login screen opened --> SUCCESS", file = sourceFile)
except:
    print("Login screen can't opened --> FAIL", file = sourceFile)

#STEP2: Username doldur
try:
    
    driver.find_element_by_xpath('//*[@id="id_userLoginId"]').send_keys(netflixUsername)
    time.sleep(1)
    driver.save_screenshot("02_usernameEntered.png")
    #screenshot = Image.open("usernameEntered.png")
    print("Username entered --> SUCCESS", file = sourceFile)

except:
    print("Username can't entered --> FAIL", file = sourceFile)

#STEP3: Password doldur.
try:
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(netflixPassword)
    time.sleep(1)
    driver.save_screenshot("03_passwordEntered.png")
    screenshot = Image.open("03_passwordEntered.png")
    print("Password entered --> SUCCESS", file = sourceFile)
except:
    print("Password can't entered --> FAIL", file = sourceFile)
#STEP3: Login
try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
    time.sleep(1)
    driver.save_screenshot("04_loginedSuccesfully.png")
    screenshot = Image.open("04_loginedSuccesfully.png")
    print("Logined --> SUCCESS", file = sourceFile)
except:
    print("Can't Logined --> FAIL", file = sourceFile)
#STEP4: User selection
try:    
    time.sleep(5)
    driver.find_element_by_xpath("//*[text()='ilhan mert']").click()
    time.sleep(1)
    driver.save_screenshot("05_userSelected.png")
    screenshot = Image.open("05_userSelected.png")
    print("User selected --> SUCCESS", file = sourceFile)
except:
    print("User can't selected--> FAIL", file = sourceFile)


time.sleep(5)
#STEP5: Select Movie
try:
    driver.find_element_by_xpath('//*[@id="main-view"]/div/span/div/div/div/div/div/div[2]/div/div/div[3]/a/button').click()
    time.sleep(1)
    driver.save_screenshot("06_movieSelected.png")
    screenshot = Image.open("06_movieSelected.png")
    print("Movie selected --> SUCCESS", file = sourceFile)
except:
    print("Movie can't selected--> FAIL", file = sourceFile)
time.sleep(5)

#
try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[2]/button[3]').click()
    driver.save_screenshot("07_tensecforward0.png")
    screenshot = Image.open("07_tensecforward0.png")
    print("10sec forwarding --> SUCCESS", file = sourceFile)
except:
    print("Cant forwarding--> FAIL", file = sourceFile)
    
time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[2]/button[3]').click()
    driver.save_screenshot("08_tensecforward.png")
    screenshot = Image.open("08_tensecforward.png")
    print("10sec forwarding --> SUCCESS", file = sourceFile)
except:
    print("Cant forwarded--> FAIL", file = sourceFile)

time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[2]/button[3]').click()
    driver.save_screenshot("09_tensecforward2.png")
    screenshot = Image.open("09_tensecforward2.png")
    print("10sec forwarding --> SUCCESS", file = sourceFile)
except:
    print("Cant forwarded--> FAIL", file = sourceFile)

time.sleep(2)

try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[2]/button[2]').click()
    driver.save_screenshot("10_10secback.png")
    screenshot = Image.open("10_10secback.png")
    print("10sec rewind --> SUCCESS", file = sourceFile)
except:
    print("Cant rewind--> FAIL", file = sourceFile)

time.sleep(5)

time.sleep(5)
try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[2]/button[1]').click()
    driver.save_screenshot("11_stopMovie.png")
    screenshot = Image.open("11_stopMovie.png")
    print("Movie Stopped --> SUCCESS", file = sourceFile)
except:
    print("Movie cant stopped--> FAIL", file = sourceFile)


time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[2]/button[4]').click()
    driver.save_screenshot("12_GoFullscreen.png")
    screenshot = Image.open("12_GoFullscreen.png")
    print("Go Fullscreen --> SUCCESS", file = sourceFile)
except:
    print("Can't go full screen--> FAIL", file = sourceFile)


time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[2]/button[4]').click()
    driver.save_screenshot("13_fullscreenOut.png")
    screenshot = Image.open("13_fullscreenOut.png")
    print("Out Fullscreen --> SUCCESS", file = sourceFile)
except:
    print("Can't Out FullScreen--> FAIL", file = sourceFile)

time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[1]/button').click()
    driver.save_screenshot("14_goBackHomePage.png")
    screenshot = Image.open("14_goBackHomePage.png")
    print("Go Back to HomePage --> SUCCESS", file = sourceFile)
except:
    print("Can't Go Back to HomePage-> FAIL", file = sourceFile)


time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="main-view"]/div/span/div/div/div/div/div/div[2]/div/div/div[3]/button').click()
    time.sleep(1)
    driver.save_screenshot("15_checkDetails.png")
    screenshot = Image.open("15_checkDetails.png")
    print("Details Checked --> SUCCESS", file = sourceFile)
except:
    print("Details Checked-> FAIL", file = sourceFile)


sourceFile.close()


#driver.find_element_by_xpath("//*[text()='İntroyu Atla']").click()

#driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/span').click()
#driver.find_element_by_css_selector('#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.profiles-gate-container > div > div > ul > li:nth-child(2) > div > a > span').click()

#javascript_to_execute = 'document.getElementByClassName("video").pause()'
#driver.execute_script(javascript_to_execute)
#driver.find_element_by_xpath('//*[@id="close-button-1604529601736"]').click()
#driver.find_element_by_xpath('//*[@id="wrap-close-button-1604529601736"]').click()
#driver.find_element_by_xpath('document.querySelector("#close-button-1604529601736")').click()




