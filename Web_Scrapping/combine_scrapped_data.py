import pandas as pd
import os
import time
#Getting all the files in collection folder
csv_files = os.listdir("collection")


# print(csv_files)
if os.path.exists("collection/All_Jobs.csv"):
    os.remove("collection/All_Jobs.csv")
    csv_files.remove("All_Jobs.csv")
    time.sleep(1)

#Reading csv files into dataframe
jobs_df = []
for i in range(len(csv_files)):
    jobs_df.append(pd.read_csv(f"collection/{csv_files[i]}"))

#Combining CSV files
combined_data = pd.concat(jobs_df,ignore_index=True)


#Saving combined_csv files
combined_data.to_csv("collection/All_Jobs.csv",mode="w")


