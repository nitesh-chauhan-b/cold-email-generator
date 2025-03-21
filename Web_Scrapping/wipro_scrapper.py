from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from query_Manager import  QuerySingleton
instance = QuerySingleton()
print("Scrapping Data for query :",instance.query,"from Wipro...")
query= instance.query

driver = webdriver.Firefox()

wait = WebDriverWait(driver,15)

# query = "python"
file_no=1
startRow = 0
try:

    for i in range(1,6):
        url =f"https://careers.wipro.com/search/?q={query}&locationsearch=India&startrow={startRow}"

        driver.get(url)


        #Getting pages and saving them
        page = wait.until(EC.presence_of_element_located(((By.ID,"searchresults"))))
        html_page = page.get_attribute("outerHTML")

        
        #Saving page
        file_path = f"Web_Scrapping/scrapped_data/wipro_data/{query}_page_{file_no}.html"

        with open(file_path,"w",encoding="utf-8") as file:
            file.write(html_page)
            file_no+=1
        
        startRow+=25

except Exception as e:
    print(e)

driver.close()