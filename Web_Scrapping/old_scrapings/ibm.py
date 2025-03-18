from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver,5)

query = "python"
i=1
#details
file_no= 1
for i in range(1,11):
    url = f"https://www.ibm.com/in-en/careers/search?q={query}&p={i}"
    driver.get(url)

    #Getting cards
    cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"bx--card-group__cards__col")))
    print(len(cards))

    #Saving cards for further use.
    for card in cards:
        html_data =card.get_attribute("outerHTML")  

        file_path = f"ibm_data/{query}_{file_no}.html"

        #Saving html data
        with open(file_path,"w",encoding="utf-8") as file:
            file.write(html_data)
            file_no+=1


#Closing driver
driver.close()
