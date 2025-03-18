from bs4 import BeautifulSoup
import pandas as pd
import os

#Getting pages in order
pages = os.listdir("Web_Scrapping/scrapped_data/apple_data")
pages= sorted(pages, key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else x)
# print(pages)

#Creating a data dict which will be used to store the retrived data
data = {"Field":[],"Title":[],"Company":[],"Posted At":[],"Location":[],"Link":[]}

print("Collecting Data from apple...")

for page in pages:
    try:
        file_path = f"Web_Scrapping/scrapped_data/apple_data/{page}"
        # print(file_path)
        #opening file   
        with open(file_path,"r",encoding="utf-8") as file:
            html_doc = file.read()

        soup = BeautifulSoup(html_doc,"html.parser")
        # print(html_doc)
        try:
            main_card = soup.find("table",attrs={"id":"tblResultSet"})
            # print(main_card)
            cards = main_card.find_all("tbody")
            # print(len(cards))
            for card in cards:
                # print(card)
                
                #Getting details of the job
                job_link = card.find("a",attrs={"class":"table--advanced-search__title"})["href"]
                job_link = f"https://jobs.apple.com{job_link}"

                job_title = card.find("a",attrs={"class":"table--advanced-search__title"}).text

                job_field = card.find("span",attrs={"class":"table--advanced-search__role"}).text
                job_posted_at = card.find("span",attrs={"class":"table--advanced-search__date"}).text

                job_location = card.find("td",attrs={"class":"table-col-2"}).text


                # print(job_link)
                # print(job_title)
                # print(job_field)
                # print(job_posted_at)
                # print(job_location)

                data["Field"].append(job_field)
                data["Title"].append(job_title)
                data['Company'].append("Apple")
                data["Posted At"].append(job_posted_at)
                data["Location"].append(job_location)
                data["Link"].append(job_link)
            #     break
            # break
        except Exception as e:
            print(e)


    except Exception as e:
        print(e)


#Saving data to CSV file
df = pd.DataFrame(data)

#Saving file
df.to_csv("Web_Scrapping/collection/Apple_Jobs.csv",index=False)