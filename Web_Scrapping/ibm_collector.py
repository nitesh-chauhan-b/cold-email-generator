from bs4 import BeautifulSoup
import os
import pandas as pd

#a dictionary which will store the retrived results
data ={"Field":[],"Title":[],"Company":[],"Posted At":[],"Location":[],"Link":[]}
pages = os.listdir("Web_Scrapping/scrapped_data/ibm_data")
pages= sorted(pages, key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else x)
# print(pages)

try:
    print("Collecting Data from IBM...")
    for path in pages:
        # print(path)
        file_path = f"Web_Scrapping/scrapped_data/ibm_data/{path}"
        with open(file_path,"r") as file:
            html_doc = file.read()

        
        #using beutiful soup for extraction
        soup = BeautifulSoup(html_doc,"html.parser")

        cards = soup.find_all("div",class_="bx--card-group__cards__col")

        try:
            for card in cards:
                job_field = soup.find("div",attrs={"class":"bx--card__eyebrow"}).text
                # print(jop_field.text)

                job_title = soup.find("div",attrs={"class":"bx--card__heading"}).text
                # print(job_title.text)
                # job_title = job_title.text

                job_category_location = soup.find("div",attrs={'class':"ibm--card__copy__inner"})
                c , l =str(job_category_location).split("<br/>")
                #getting details 
                _,_,job_category = c.partition(">")
                job_location,_,_ = l.partition("<")
                # print()
                # print(job_category,job_location)

                job_link = soup.find("a")['href']
                # print(job_link)

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

df.to_csv("Web_Scrapping/collection/IBM_Jobs.csv",index=False)