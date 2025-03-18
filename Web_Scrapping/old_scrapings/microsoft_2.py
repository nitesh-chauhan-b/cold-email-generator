from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()

#Wait driver
wait = WebDriverWait(driver,5)

query = "python"
i = 1
page_no = 1
job_url = []
for i in range(1,2):
    try:
        url = f"https://jobs.careers.microsoft.com/global/en/search?q={query}&l=en_us&pg={i}&pgSz=20&o=Relevance"

        driver.get(url)

        #creating getting elements 
        page = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"ms-List-page")))

        #Html page
        html_page = page.get_attribute("outerHTML")

        #Saving page 
        # file_name = f"ms_data/{query}_page_{page_no}.html"
        # with open(file_name,"w",encoding="utf-8") as file:
        #     file.write(html_page)
        #     page_no+=1


        #Gettiing links of jobs
        cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"ms-List-cell")))

        for card in cards:
            title = card.find_element(By.CLASS_NAME,"MZGzlrn8gfgSs8TZHhv2")

            title.click()
            # #Getting url of the job_post
            job_link = driver.current_url
            job_url.append(job_link)

            #Using another approach
            driver.back()



            # print(driver.current_url)

            # #Getting back
            # driver.switch_to.window(driver.window_handles[0])
            #back button 

            # back_btn = driver.find_element(By.CLASS_NAME,"root-529").click()

            # # print(driver.current_url)
            # driver.switch_to.window(driver.window_handles[0])
            # break
        # break
    except Exception as e:
        print(e)

time.sleep(1000)
driver.close()