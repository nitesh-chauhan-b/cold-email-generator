from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Getting global data about query
from query_Manager import  QuerySingleton
instance = QuerySingleton()
print("Scrapping Data for query :",instance.query,"from SAP...")
query= instance.query

driver = webdriver.Firefox()

wait = WebDriverWait(driver,15)

# if not query:
#     query = "python"
# query ="python"

file_no=1
startRow = 0
try:

    for i in range(1,6):
        url =f"https://jobs.sap.com/search/?q={query}&locationsearch=India&optionsFacetsDD_country=IN&startrow={startRow}&scrollToTable=true"

        driver.get(url)


        #Getting pages and saving them
        page = wait.until(EC.presence_of_element_located(((By.ID,"searchresults"))))
        html_page = page.get_attribute("outerHTML")


        #Saving page
        file_path = f"Web_Scrapping/scrapped_data/sap_data/{query}_page_{file_no}.html"

        with open(file_path,"w",encoding="utf-8") as file:
            file.write(html_page)
            file_no+=1

        startRow+=25

    # for i in range(1,10):
    #     next_btn = driver.find_element(By.LINK_TEXT,"»")
    #     next_btn.click()

    #     page = driver.find_element(By.ID,"searchresults")
    #     html_page = page.get_attribute("outerHTML")
    #     #Saving page
    #     file_path = f"scrapped_data/sap_data/{query}_page_{file_no}.html"

    #     with open(file_path,"w",encoding="utf-8") as file:
    #         file.write(html_page)
    #         file_no+=1

except Exception as e:
    print(e)

driver.close()