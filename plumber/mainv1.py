from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
from csv_DataList_writer import write_list

start_time = time.time()

def ScrollAndDetect():
    try:
        scrollbar = web.find_element(By.CSS_SELECTOR, "div:nth-child(5) .hfpxzc").click
        scrollbar = web.find_element(By.CSS_SELECTOR, "div:nth-child(5) .hfpxzc").send_keys(Keys.END)
        time.sleep(0.7)
        End_text = web.find_element(By.CSS_SELECTOR, ".HlvSq").text
        scrollbar = web.find_element(By.CSS_SELECTOR, "div:nth-child(5) .hfpxzc").send_keys(Keys.END)
    except:
        scrollbar = web.find_element(By.CSS_SELECTOR, "div:nth-child(5) .hfpxzc").send_keys(Keys.END)
        ScrollAndDetect()


def nextBox():
    try:
        time.sleep(1.2)
        main_img = web.find_element(By.CSS_SELECTOR, ".aoRNLd > img").get_attribute("src")
        return main_img
    except:
        time.sleep(0.85)
        nextBox()

def getDetails(Boxes_list):
    details_list = ["Image,Tilte,Location,Phone number,Website"]

    for box in Boxes:
        try:
            location_text = web.find_element(By.CSS_SELECTOR, "div.RcCsl:nth-child(3) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").text
        except:
            location_text = "Not Specified"


        try:
            box.click()
            box.click()
        except:
            web.execute_script("arguments[0].click();", box)
        time.sleep(0.9)
        main_img = nextBox()
        title = web.find_element(By.CSS_SELECTOR, ".DUwDvf > span:nth-child(1)").text
        details_options = web.find_elements(By.CSS_SELECTOR, "div.RcCsl")
        phone_num = "ERROR_num"
        Website_name = "No website"
        time.sleep(1.5)
        for detail in details_options:
            try:
                ld = list(detail.text)
                if "+" in ld[0]:
                    phone_num = detail.text
            except:
                pass
    
            try:
                web_code = requests.get("http://"+detail.text).status_code
                Website_name = detail.text
            except:
                pass
            
            details = f"{main_img},{title},{location_text},{phone_num},{Website_name}"
        details_list.append(details)

    return details_list



FireOptions = Options()
FireOptions.headless = False

web = webdriver.Firefox(options=FireOptions)

web.get("https://www.google.com/maps/search/furniture+shops+in+uk")
End_text = ScrollAndDetect()

Boxes = web.find_element(By.CSS_SELECTOR, "div.DxyBCb:nth-child(1)").find_elements(By.CLASS_NAME, "hfpxzc")
up_time = time.time() - start_time
print(len(Boxes), " Boxes in this research! in ", up_time, " seconds.")

#BUG: list have duplicates
Boxes[0].click()
time.sleep(5)
details = getDetails(Boxes)
write_list(details, "test.csv")

up_time = time.time() - start_time
print("Done in ", up_time, " seconds")
web.quit()