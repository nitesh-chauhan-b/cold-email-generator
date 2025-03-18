import streamlit as st
import subprocess
import time
#Scrapping data
def scrap():
    #Scrapping the website
    subprocess.run(["python","Web_Scrapping/apple_scrapper.py"])
    subprocess.run(["python","Web_Scrapping/ibm_scrapper.py"])
    subprocess.run(["python","Web_Scrapping/capgemini_scrapper.py"])
    subprocess.run(["python","Web_Scrapping/cognizant_scrapper.py"])
    subprocess.run(["python","Web_Scrapping/oracle_scrapper.py"])
    subprocess.run(["python","Web_Scrapping/sap_scrapper.py"])

    return True

def collect():

    #Collectors for getting data from scrapped website's html files
    subprocess.run(["python","Web_Scrapping/apple_collector.py"])
    subprocess.run(["python","Web_Scrapping/ibm_collector.py"])
    subprocess.run(["python","Web_Scrapping/capgemini_collector.py"])
    subprocess.run(["python","Web_Scrapping/cognizant_collector.py"])
    subprocess.run(["python","Web_Scrapping/oracle_collector.py"])
    subprocess.run(["python","Web_Scrapping/sap_collector.py"])

    return True

def save_data():
    subprocess.run(["python","combine_scrapped_data.py"])
    print("The data has has been saved successfully!")
    return True

if __name__ =="__main__":
    scrap()
    print("Scrapping")
    save_data()
    print("The data has been saved successfully!")