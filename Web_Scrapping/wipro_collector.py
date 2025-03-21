from bs4 import BeautifulSoup
import os
import pandas as pd

#data fields
data ={"Field":[],"Title":[],"Company":[],"Posted At":[],"Location":[],"Link":[]}

#Sorting pages
pages = os.listdir("Web_Scrapping/scrapped_data/wipro_data")

pages= sorted(pages, key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else x)
# print(pages)
try:
    print("Collecting Data from Wipro...")
    for page in pages:
        # print(page)
        file_path = f"Web_Scrapping/scrapped_data/wipro_data/{page}"

        with open(file_path,"r") as file:
            html_doc = file.read()

        soup = BeautifulSoup(html_doc,"html.parser")

        #Finding cards 
        cards = soup.find_all("tr",attrs={"class":"data-row"})

        for card in cards:
            try:
                job_link = card.find("a")["href"]
                job_link = "https://careers.wipro.com/"+job_link

                job_title = card.find("a").text

                job_location = card.find_all("span",attrs={"class":"jobLocation"})[1].text
                job_location=job_location.strip()

                job_post_date = card.find("span",attrs={"class":"jobDate"}).text.strip()

                # print(job_link)
                # print(job_title)   
                # print(job_location)
                # print(job_post_date)

                # break

                #Adding data into dict
                data["Field"].append("Software Engineering")
                data["Title"].append(job_title)
                data["Company"].append("Wipro")
                data["Posted At"].append(job_post_date)
                data["Location"].append(job_location)
                data["Link"].append(job_link)

            except Exception as e:
                print(e)
        # break
except Exception as e:
    print(e)


#Adding data to csv file
df = pd.DataFrame(data)

df.to_csv("Web_Scrapping/collection/Wipro_Jobs.csv")