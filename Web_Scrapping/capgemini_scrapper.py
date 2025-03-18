from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from query_Manager import  QuerySingleton
instance = QuerySingleton()
print("Scrapping Data for query :",instance.query,"from Capgemini...")
query= instance.query

size = 80
driver = webdriver.Firefox()
wait = WebDriverWait(driver,10)


try:
    url = f"https://www.capgemini.com/careers/join-capgemini/job-search/?keyword={query}&country_code=en-in&size={size}"

    driver.get(url)

    #Finding page
    # page = driver.find_element(By.CSS_SELECTOR,"div .table")
    page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div .table")))
    page_html = page.get_attribute("outerHTML")

    file_path = f"Web_Scrapping/scrapped_data/capgemini_data/{query}_page.html"

    #saving html file
    with open(file_path,"w",encoding="utf-8") as file:
        file.write(page_html)

except Exception as e:
    print(e)

driver.close()