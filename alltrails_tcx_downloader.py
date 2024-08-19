import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

running_data_path = r"C:\Users\dhava\Downloads\jobId=bb819631-be31-4271-b4f2-2b49b79460a3\tcx"

cService = webdriver.ChromeService(executable_path=r"C:\Users\dhava\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=cService)

file_upload = "FileUpload-module__hidden___leG7z"
driver.get("https://www.alltrails.com/converter")
for file_name in os.listdir(running_data_path):
    time.sleep(5)
    #driver.get("https://www.alltrails.com/converter")
    print(running_data_path + "/" + file_name)
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, file_upload).send_keys(running_data_path + "\\" + file_name)
    #print(driver.find_element(By.CLASS_NAME, filetype_select))
    time.sleep(5)
    select = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[1]/div/form/div/div[2]/div/label/div[2]/select"))
    select.select_by_visible_text("Google Earth KML")
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[1]/div/form/div/div[4]/button").click()
    seconds = random.randrange(0, 9)
    time.sleep(seconds)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div/div[2]/div/div[3]/a").click()