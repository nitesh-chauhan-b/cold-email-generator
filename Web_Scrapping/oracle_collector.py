from bs4 import BeautifulSoup
import os
import pandas as pd

#data fields
data ={"Field":[],"Title":[],"Company":[],"Posted At":[],"Location":[],"Link":[]}


try:
    if os.path.exists("Web_Scrapping/scrapped_data/oracle_data/python_page.html"):
        file_path = "Web_Scrapping/scrapped_data/oracle_data/python_page.html"

        with open(file_path,"r") as file:
            html_doc = file.read()

        soup = BeautifulSoup(html_doc,"html.parser")
        
        # print("done")

        #Finding cards 
        cards = soup.find_all("li",attrs={"data-qa":"searchResultItem"})

        # print(len(cards))
        print("Collecting Data from Oracle...")
        for card in cards:
            try:
                job_link = card.find("a")["href"]

                job_title = card.find("span",attrs={"class":"job-tile__title"}).text

                job_location = card.find("span",attrs={"data-bind":"html: primaryLocation"}).text

                job_desc = card.find("p",attrs={"class":"job-grid-item__description"}).text


                # print(job_link)
                # print(job_title)
                # print(job_location)
                # print(job_desc)

                #Adding data

                data["Field"].append("Software Engineering")
                data["Title"].append(job_title)
                data["Company"].append("Oracle")
                data["Posted At"].append("NA")
                data["Link"].append(job_link)
                data["Location"].append(job_location)

                # break
            except Exception as e:
                print(e)
except Exception as e:
    print(e)

#Saving data into csv file
df = pd.DataFrame(data)

df.to_csv("Web_Scrapping/collection/Oracle_Jobs.csv",index=False)