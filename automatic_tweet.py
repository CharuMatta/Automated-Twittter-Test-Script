import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome_path = r'/Users/chauabhi/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.implicitly_wait(30)
# navigate to the application home page
driver.get("https://twitter.com/login?lang=en")

# get the username textbox

# login_field = driver.find_element_by_xpath("//div//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1inuy60 r-utggzx r-vmopo1 r-1w50u8q r-1lrr6ok r-1dz5y72 r-fdjqy7 r-13qz1uu']")
login_field = driver.find_elements_by_name("session[username_or_email]")
# enter username
login_field.send_keys("")
time.sleep(1)

#get the password textbox

password_field = driver.find_elements_by_name("session[password]")

#enter password
time.sleep(2)
password_field[0].send_keys("")
time.sleep(2)

login_button = driver.find_element_by_xpath("//span//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']")
login_button.click()

# import pdb;pdb.set_trace()

element = driver.find_element_by_xpath("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']//span")
element.send_keys("""My First Automated Tweet """)


time.sleep(5)
sendTw = driver.find_element_by_xpath("//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-vw2c0b r-1777fci r-eljoum r-dnmrzs r-bcqeeo r-q4m81j r-qvutc0']//span//span[contains(text(),'Tweet')]")
sendTw.click()

time.sleep(3)
driver.close()