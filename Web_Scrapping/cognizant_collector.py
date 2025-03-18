from bs4 import BeautifulSoup
import os
import pandas as pd

#a dictionary which will store the retrived results
data ={"Field":[],"Title":[],"Company":[],"Posted At":[],"Location":[],"Link":[]}

#Sorting pages
pages = os.listdir("Web_Scrapping/scrapped_data/cognizant_data")

pages= sorted(pages, key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else x)
# print(pages)
try:
    print("Collecting Data from Cognizant...")
    for path in pages:
        # print(path)
        file_path = f"Web_Scrapping/scrapped_data/cognizant_data/{path}"
        with open(file_path,"r") as file:
            html_doc = file.read()

        
        #using beutiful soup for extraction
        soup = BeautifulSoup(html_doc,"html.parser")

        cards = soup.find_all("div",class_="card-job")
        # print(len(cards))

        for card in cards:
            try:   
                #Finding company details
                job_title = card.find("a").text

                job_link  = card.find("a")["href"]
                job_link = "https://careers.cognizant.com/"+job_link

                #collection of data
                job_collection = card.find_all("li",attrs={"class":"list-inline-item"})

                job_location = job_collection[0].text.strip()
                job_field = job_collection[1].text.strip()

                # print(job_title)
                # print(job_link)
                # print(job_location)
                # print(job_field)

                # break

                data["Field"].append(job_field)
                data["Title"].append(job_title)
                data["Company"].append("IBM")
                data["Posted At"].append("NA")
                data["Location"].append(job_location)
                data["Link"].append(job_link)
                # break
            except Exception as e:
                print("Card Error",e)
        # break
except Exception as e:
    print(e)


#Saving the data of dictionay into a csv file
df = pd.DataFrame(data)

df.to_csv("Web_Scrapping/collection/Cognizant_Jobs.csv",index=False)