from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

wait = WebDriverWait(driver,10)
query = "python"
i=1

try:    
    url = "https://ibegin.tcs.com/iBegin/jobs/search"
    driver.get(url)
    # wait.until(EC.url_to_be((driver.get(url))))
    search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"select-single-box")))

    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    for i in range(1,11):

        page_navigation = driver.find_element(By.CLASS_NAME,"pagination")

        #Finding page 
        next_page_btn = page_navigation

        #Getting page
        page = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"jobs-container-keep")))

        html_page = page.get_attribute("outerHTML")

        file_path = f"scrapped_data/tcs_data/{query}_page_{i}.html"

        with open(file_path,"w",encoding="utf-8") as file:
            file.write(html_page)

except Exception as e:
    print(e)


time.sleep(5)
driver.close()