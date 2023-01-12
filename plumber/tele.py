import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service



url = "https://web.telegram.org"

s = Service(GeckoDriverManager().install())

web = webdriver.Firefox(service=s)

def vpn():
    web.get("https://addons.mozilla.org/en-US/firefox/addon/cyberghost-vpn-free-proxy/")
    try:
        web.find_element(By.CSS_SELECTOR, ".AMInstallButton-button").click()
    except:
        pass
    input("Press Enter to countinue")
vpn()
web.get(url)


time.sleep(10)
clicked = 0
while clicked == 0:
    try:
        time.sleep(5)
        web.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        clicked = 1
    except:
        pass

    try:
        web.find_element(By.CSS_SELECTOR, ".Button").click()
        clicked = 1
    except:
        pass
time.sleep(5)
try:
    web.find_element(By.CSS_SELECTOR, "div.input-field:nth-child(1) > div").send_keys(Keys.CONTROL + "a")
    web.find_element(By.CSS_SELECTOR, "div.input-field:nth-child(1) > div").send_keys("Uzbekistan")
    web.find_element(By.CSS_SELECTOR, "div.input-field:nth-child(1) > div").send_keys(Keys.ENTER)

except:
    web.find_element(By.CSS_SELECTOR, "#sign-in-phone-code").send_keys(Keys.CONTROL + "a")
    web.find_element(By.CSS_SELECTOR, "#sign-in-phone-code").send_keys("Uzbekistan")
    web.find_element(By.CSS_SELECTOR, "#sign-in-phone-code").send_keys(Keys.ENTER)
phone_num = "995000936" #input("Phone Number : ")
try:
    web.find_element(By.CSS_SELECTOR, '#sign-in-phone-number').send_keys(phone_num)
except:
    web.find_element(By.CSS_SELECTOR, "div.input-field:nth-child(2) > div").send_keys(phone_num)
time.sleep(5)
try:
    web.find_element(By.CSS_SELECTOR, "button.btn-primary:nth-child(4) > div:nth-child(1)").click()
except:
    try:
    
        web.find_element(By.CSS_SELECTOR, "button.btn-primary:nth-child(4) > div").click()
    except:
        try:
            web.find_element(By.CSS_SELECTOR, "button.Button:nth-child(4) > div:nth-child(1)").click()
        except:
            pass
        pass
    pass
time.sleep(15)
verification_code = input("Did u entered verification code can we countinut (ENTER) ")

groups = ["https://web.telegram.org/k/#@Online_Sumkalar_Shop"]

for group in groups:
    web.get(group)
#    try:
#        opn_web = web.find_element(By.CSS_SELECTOR, "").click()
#    except:
#        pass
