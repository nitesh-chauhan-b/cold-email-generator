from bs4 import BeautifulSoup
import os
import pandas as pd

#data fields
data ={"Field":[],"Title":[],"Company":[],"Posted At":[],"Location":[],"Link":[]}


try:
    if os.path.exists("Web_Scrapping/scrapped_data/capgemini_data/python_page.html"):
        file_path = "Web_Scrapping/scrapped_data/capgemini_data/python_page.html"

        with open(file_path,"r") as file:
            html_doc = file.read()

        soup = BeautifulSoup(html_doc,"html.parser")
        
        print("Collecting Data from Capgemini...")

        #Finding cards 
        cards = soup.find_all("a")

        # print(len(cards))


        for card in cards:
            try:
                #Finiding job details
                job_collection = card.find_all("div",attrs={"class":"table-td"})
                
                # print(len(job_collection))
                # print(job_collection)

                #Getting Details
                job_title = job_collection[0]

                job_title = job_title.select(":nth-child(2)")[0].text
                
                job_location = job_collection[2]

                job_location = job_location.select(":nth-child(2)")[0].text

                job_link = card["href"]

                job_link = "https://www.capgemini.com/"+job_link


                # break



                #Adding data

                data["Field"].append("Software Engineering")
                data["Title"].append(job_title)
                data["Company"].append("Capgemini")
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

df.to_csv("Web_Scrapping/collection/Capgemini_Jobs.csv",index=False)