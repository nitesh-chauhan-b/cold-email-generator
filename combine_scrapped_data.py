import pandas as pd
import os
import time
#Getting all the files in collection folder
csv_files = os.listdir("Web_Scrapping/collection")


# print(csv_files)
if os.path.exists("Web_Scrapping/collection/All_Jobs.csv"):
    os.remove("Web_Scrapping/collection/All_Jobs.csv")
    csv_files.remove("All_Jobs.csv")
    time.sleep(1)

#Reading csv files into dataframe
jobs_df = []
for i in range(len(csv_files)):
    jobs_df.append(pd.read_csv(f"Web_Scrapping/collection/{csv_files[i]}"))

#Combining CSV files
combined_data = pd.concat(jobs_df,ignore_index=True)


#Saving combined_csv files
combined_data.to_csv("Web_Scrapping/collection/All_Jobs.csv",mode="w")


