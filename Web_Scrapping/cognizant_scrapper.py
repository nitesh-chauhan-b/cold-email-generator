from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Getting query from global singleton class
from query_Manager import  QuerySingleton
instance = QuerySingleton()
print("Scrapping Data for query :",instance.query,"from Cognizant...")
query= instance.query

driver = webdriver.Firefox()

wait = WebDriverWait(driver,10)
# if not query:
#     query = "python"
# query ="python"
i=1
try:
    for i in range(1,6):
        url = f"https://careers.cognizant.com/global-en/jobs/?page={i}&keyword={query}&location=India&radius=100&cname=India&ccode=IN&pagesize=10#results"
        driver.get(url)

        page = wait.until(EC.presence_of_element_located((By.ID,"js-job-search-results")))

        html_page = page.get_attribute("outerHTML")

        #Saving HTML page into a folder
        file_name = f"Web_Scrapping/scrapped_data/cognizant_data/{query}_page_{i}.html"

        with open(file_name,"w",encoding="utf-8") as file:
            file.write(html_page)

except Exception as e:
    print(e)

driver.close()