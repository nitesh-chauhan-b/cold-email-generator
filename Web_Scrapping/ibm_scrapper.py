from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Getting global data about query
from query_Manager import  QuerySingleton
instance = QuerySingleton()
print("Scrapping Data for query :",instance.query,"from IBM...")
query= instance.query

driver = webdriver.Firefox()

wait = WebDriverWait(driver,10)
# if not query:
#     query = "python"
# query ="python"

i=1
try:
    for i in range(1,6):
        url = f"https://www.ibm.com/in-en/careers/search?q={query}&p={i}"
        driver.get(url)
        page = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"bx--card-group__cards__row")))
        html_page = page.get_attribute("outerHTML")

        #Saving HTML page into a folder
        file_name = f"Web_Scrapping/scrapped_data/ibm_data/{query}_page_{i}.html"

        with open(file_name,"w",encoding="utf-8") as file:
            file.write(html_page)

except Exception as e:
    print(e)

driver.close()