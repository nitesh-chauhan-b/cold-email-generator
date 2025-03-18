import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Firefox()

#trying to create a csv file of this data
data ={"Field":[],"Title":[],"Categorty & Location":[],"Link":[]}

for file in os.listdir("ibm_data"):
    print(file)

    try:
        #Opening file 
        with open(f"ibm_data/{file}","r") as file:
            html_doc = file.read()

        soup = BeautifulSoup(html_doc,"html.parser")
        
        
        job_field = soup.find("div",attrs={"class":"bx--card__eyebrow"}).text
        # print(jop_field.text)

        job_title = soup.find("div",attrs={"class":"bx--card__heading"}).text
        # print(job_title.text)
        # job_title = job_title.text

        job_category = soup.find("div",attrs={'class':"ibm--card__copy__inner"}).text
        # print(job_category.text)

        job_link = soup.find("a")['href']
        # print(job_link)

        data["Field"].append(job_field)
        data["Title"].append(job_title)
        data["Categorty & Location"].append(job_category)
        data["Link"].append(job_link)

    except Exception as e:
        print(e)



#Creating a csv file of retrived data
df = pd.DataFrame(data=data)

df.to_csv("IBM_jobs.csv")