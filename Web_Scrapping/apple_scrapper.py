from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from query_Manager import  QuerySingleton
instance = QuerySingleton()
print("Scrapping Data for query :",instance.query,"from Apple...")
query= instance.query
i=1

# print(query)

driver = webdriver.Firefox()

wait = WebDriverWait(driver,10)

try:
    for i in range(1,6):
        url = f"https://jobs.apple.com/en-gb/search?location=india-INDC&search={query}&sort=relevance&page={i}"
        driver.get(url)
        page = wait.until(EC.presence_of_element_located(((By.CLASS_NAME,"results"))))
        if not page:
            break
        html_page = page.get_attribute("outerHTML")

        #Saving search result
        file_path = f"Web_Scrapping/scrapped_data/apple_data/{query}_page_{i}.html"

        with open(file_path,"w",encoding="utf-8") as file:
            file.write(html_page)

except Exception as e:
    print(e)

driver.close()

