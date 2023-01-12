from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time, os
import requests
import colorama
from colorama import Fore, Style

####INPUTS
places_work = "furniture shops in uk"
outfile = "out.csv"

start_time = time.time()

def write_csv(Line, outfile):
    fl = "Title, Location , Website , Phone number"
    if os.path.exists(outfile) == False:
        File = open(outfile, "a")
        File.write(fl)
    File = open(outfile, "a")
    File.write(f"\n{Line}")


def chk_site(site):
    try:
        #print(site) #To Find Bugs
        requests.get(f"http://{site}", timeout=10)
        return site
    except:
        return "Website Not Working"

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


def Extract(Boxes, outFile):
    print(f"{Fore.GREEN}[*] Extraction started! ...{Style.RESET_ALL}")
    bn = 1
    Boxes[0].click()
    time.sleep(5)
    for box in Boxes:
        print(Fore.YELLOW, f"Extracting from box no : {bn}", Style.RESET_ALL)
        box.click()
        time.sleep(5)
        title = "getting"
        while title == "getting":
            try:
                title = web.find_element(By.CSS_SELECTOR, ".DUwDvf > span:nth-child(1)").text
            except:
                title = "getting"

        time.sleep(2)



        details_load = 0
        while details_load == 0:

            try:
                time.sleep(3)
                try:
                    Details_box = web.find_element(By.CSS_SELECTOR, "div.m6QErb:nth-child(9)")
                    details_load = 1
                except:
                    Details_box = web.find_element(By.CSS_SELECTOR, "div.m6QErb:nth-child(13)")
                    details_load = 1
            except:
                pass

        Location = Details_box.find_element(By.CSS_SELECTOR, "div.RcCsl:nth-child(3) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div").text
        Location = Location.replace(",", "'")


        try:
            Website = Details_box.find_element(By.CSS_SELECTOR, ".ITvuef > div").text
            Website = chk_site(Website)
        except  Exception as e:
            print(e)
            Website = "Not specified"

        phone_num = "Not specified"
        try:
            phone_num = Details_box.find_element(By.CSS_SELECTOR, "div.RcCsl:nth-child(6) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div").text
            if "+" in phone_num:
                phone_num = phone_num
            else:
                phone_num = "Not specified"
        except:
            phone_num = "Not specified"
        Line = f"{title},{Location},{Website},{phone_num}"
        print(Line)
        write_csv(Line, outFile)
        bn = bn + 1

FireOptions = Options()
FireOptions.headless = True

web = webdriver.Firefox(options=FireOptions)

web.get(f'https://www.google.com/maps/search/{places_work.replace(" ", "+")}')
End_text = ScrollAndDetect()

Boxes = web.find_element(By.CSS_SELECTOR, "div.DxyBCb:nth-child(1)").find_elements(By.CLASS_NAME, "hfpxzc")
up_time = time.time() - start_time
print(Fore.BLUE, len(Boxes), " Boxes in this research! in ", up_time, " seconds.", Style.RESET_ALL)

Extract(Boxes, outfile)
up_time = time.time() - start_time
print(Fore.GREEN, "Done in ", up_time, " seconds", Style.RESET_ALL)
web.quit()