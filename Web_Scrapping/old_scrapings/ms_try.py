from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
query = "python"
i = 1

url = f"https://jobs.careers.microsoft.com/global/en/search?q={query}&l=en_us&pg={i}&pgSz=20&o=Relevance"

driver.get(url)

wait = WebDriverWait(driver,20)

link =[]
def get_card_link(card,j_link):

    link_driver = webdriver.Firefox()

    link_driver.get(j_link)
    #Getting card link
    card.click()
    job_link = driver.current_url
    link.append(job_link)
    link_driver.close()


try:
    #Finding cards
    cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"ms-List-cell")))

    for index in range(len(cards)):

        #Reloacting the cards for getting next card in line
        cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"ms-List-cell")))
        card = cards[index]

        #Getting titel

        current_url = driver.current_url

        card.click()
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME,"V1_4F5i9Mw6wdP8mvFWx")))
        time.sleep(0.5)
        job_link = driver.current_url
        link.append(job_link)

        driver.back()
except Exception as e:
    print("ERROR : ",e)
    # time.sleep(5)
    driver.close()

# time.sleep(5)
# driver.close()
print(len(link))
print(link)
# driver.close()