from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Getting global data about query
from query_Manager import  QuerySingleton
instance = QuerySingleton()
print("Scrapping Data for query :",instance.query,"from Oracle...")
query= instance.query

driver = webdriver.Firefox()
# if not query:
#     query = "python"
# query ="python"

#wait driver
wait = WebDriverWait(driver,15)

try:
    url = f"https://careers.oracle.com/jobs/#en/sites/jobsearch/requisitions?keyword={query}&mode=location"

    # wait.until(EC.presence_of_element_located(driver.get(url)))
    driver.get(url)
    time.sleep(10)

    #Finding button to load more and more jobs

    for i in range(1,6):
        load_btn = wait.until(EC.presence_of_element_located(((By.CLASS_NAME,"search-pagination"))))
        load_btn.click()
        time.sleep(1)

    #Finding getting page
    page = driver.find_element(By.CLASS_NAME,"jobs-grid__list")

    html_page = page.get_attribute("outerHTML")

    #Saving page
    file_path = f"Web_Scrapping/scrapped_data/oracle_data/{query}_page.html"

    with open(file_path,"w",encoding="utf-8") as file:
        file.write(html_page)

except Exception as e:
    print(e)



# time.sleep(5)

driver.close()
# driver.close()

