#Importing important packages
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
#loading env file
load_dotenv()

#Creating llm
llm = ChatGroq(
    model = "llama3-70b-8192",
    temperature=0.6,
    max_tokens=2000,
    max_retries=3
)

#TEsting
# print(llm.invoke("jhelka"))

def get_web_data(url):
    #Loading data
    loader = WebBaseLoader(web_path=url)
    page_data = loader.load().pop().page_content

    #Passing page_data to llm to get the required JSON data
    #Prompt template

    prompt_text = PromptTemplate(
        input_variables=["page_data"],
        template="""
            You Are a a Cold Email Generator Assiatant. Who's job is to generate a cold emails based on the documents provided by the user.
            Task : Your task is to analiyze whole document provided to you and generate a JSON Fileds.
            Which Are : job_title,required_skills,preferred_skills,exerience,job_description

            The Above Filed are the must fileds. Which you have to generate. 

            Apart, from this you can generate some additional fields into a json which seems to be important for writing a email for job. But, the specifiled fileds are the must ones.

            ## NO PREAMBLE
            ## ONLY RETURN VALID JSON

            The document is given below,
            {page_data}

            Do not include heading. Not even anything apart from JSON reponse(nothing else).
        """
    )

    #Calling llm based on prompt
    prompt_json = prompt_text | llm
    response = prompt_json.invoke({"page_data": page_data})
    print(response.content)


url = "https://careers.ibm.com/job/20978143/software-developer-intern-2025-san-jose-ca/?codes=WEB_Search_INDIA"
get_web_data(url)
