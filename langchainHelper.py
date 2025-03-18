#Creating a Cold Email Generator
import uuid

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
import pandas as pd
import chromadb
from langchain_core.output_parsers import JsonOutputParser
import utils

#Loading Environment variables
load_dotenv()

#Creating llm
llm = ChatGroq(
    temperature=0.6,
    model = "llama3-70b-8192",
    max_tokens=1800,
    max_retries=2
)


#Testign llm connection
# print(llm.invoke("Hello"))


#Creating a function to get the web data
def get_web_data(url):
    #Loading data using document loader
    loader = WebBaseLoader(web_path=url)

    #Gatting the page content from document.
    page_data = loader.load().pop().page_content

    #Filtering page_data
    page_data = utils.clean_text(page_data)

    return page_data

def get_json_data(page_data):
    #Passing the page data to llm to convert it into JSON field of required data.
    prompt_text = PromptTemplate(
        input_variables=["page_data"],
        template="""
            You Are a a Cold Email Generator Assistant. Who's job is to generate a cold emails based on the documents provided by the user.
            Task : Your task is to analyze whole document provided to you and generate a JSON fields.
            Which Are : job_title,skills,experience,job_description

            The Above Filed are the must fields. Which you have to generate. 
            
            Apart, from this you can generate some additional fields into a json which seems to be important for writing a email for job. But, the specifiled fileds are the must ones.
            
            ## NO PREAMBLE
            ## ONLY RETURN VALID JSON

            The document is given below,
            {page_data}

            Do not include heading. Not even anything apart from JSON response(nothing else).
        """
    )


    #Using this prompt template through pipeline operator.
    prompt_json = prompt_text | llm
    json_data = prompt_json.invoke(input={"page_data":page_data})


    #Converting str json data into actual JSON format.
    json_parser = JsonOutputParser()
    json_page_data = json_parser.parse(json_data.content)

    print(json_data.content)
    return json_page_data

def store_company_portfolio(csv):
    #Reading company portfolio file about tech and their projects
    company_portfolio = pd.read_csv(csv)

    #Creating a chromadb and storing csv data into chromadb for similaritySearch

    #This will create a local database into a file structure for further use.
    client = chromadb.PersistentClient("company_portfolio")

    #Creating a collection to store the data
    collection = client.get_or_create_collection("company_portfolio")

    #Adding data into collection from csv file.
    if not collection.count():
        for i,row in company_portfolio.iterrows():
            #Adding data into collection for similaritySearch
            collection.add(
                documents=row["Techstack"],
                metadatas={"links":row["Links"]},
                ids = [str(uuid.uuid4())]
            )

    #Finally company portfolio is store into a json file.
    print("The portfolio is stored successfully!")

def get_relevant_links(json_data):
    #Reading vector database for finding links through similaritySearch
    client= chromadb.PersistentClient("company_portfolio")

    #getting collection
    collection = client.get_or_create_collection("company_portfolio")

    #Getting relevant links based on the skills from scrapped JSON data
    links =[]
    if json_data["skills"]:
        skills = collection.query(
            query_texts=json_data["skills"],
            n_results=2,
        )["metadatas"]
        if skills:
            links.extend(skills)
        return links
    else:
        return links
    #
    # perf_skills = collection.query(
    #     query_texts=json_data["preferred_skills"],
    #     n_results=2
    # )["metadatas"]

    # links.extend(skills)
    # links.append(perf_skills)


    # if skills:
    #     links.extend(skills)
    # else:
    #     return links

    #Testing
    # print(links)
    # if links:
    #     return links
    # else:
    #     return [""]

def get_cold_email(json_data,links):

    #Creating a prompt to get the cold email based on the given info of json_data,links to find most relevant link
    prompt_email = PromptTemplate(
        input_variables=["json_data","company_name","link_list"],
        template="""
        ### JOB DESCRIPTION
        {json_data}

        ### INSTRUCTIONS
        Generate a Professional Cold Email from above given data. Do not include heading(NO PREAMBLE) or anything else apart from just email.
        
        {company_name} Which is service based company and would like client to hire them for the job.
        This company has a 12+ years of experience in development. Is one of the best known for their service.
        It should be a best combination of professional and marketing email.
        The cold email must be professional email from company {company_name}.

        Also add most relevant links from the following to show case {company_name} work {link_list}
        Information to use in case required,
        Contact Information : info@drcsystems.com
        Your Name : Kamal
        Position : Marketing Department
        """
    )

    ### Don't add heading in response. Not even anything else apart from email only(NO HEADING).
    ### EMAIL (NO PREAMBLE):
    # print(prompt_email.format(json_data=json_data,company_name ="DRC Systems India Limited.",link_list=links))

    #Creating a chain to get the cold email
    email_chain = prompt_email | llm
    cold_email = email_chain.invoke(input={"json_data":json_data,"company_name":"DRC Systems India Limited.","link_list":links})

    # print(cold_email.content)
    return cold_email

url = "https://careers.ibm.com/job/20978143/software-developer-intern-2025-san-jose-ca/?codes=WEB_Search_INDIA"

if __name__ == "__main__":
    try:
        if url:
            page_data = get_web_data(url)
            json_page_data = get_json_data(page_data)

            # print(type(json_response))

            #Storing company portfolio
            store_company_portfolio("resource/my_portfolio.csv")

            # print(type(json_page_data))
            #Getting relevant links from the vector database for job
            links = get_relevant_links(json_page_data)

            #Getting Cold Email
            cold_email = get_cold_email(json_page_data,links)

            #getting cold email
            print(cold_email.content)

    except Exception as e:
        print("Something went wrong. Please Try again!",e)
