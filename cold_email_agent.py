#Automated Email Drafting

#Importing required packages
from dotenv import load_dotenv
load_dotenv()
import os
from pydantic import SecretStr
#Creating required llm which is from google
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_community import GmailToolkit
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage,HumanMessage


#LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=SecretStr(os.getenv("GOOGLE_API_KEY")))

#Testing
# print(llm.invoke("Hello"))

def setup_gmail_toolkit():
    #Initial Setup

    #For this it required the authentication from the user to actually sent the email and have permission

    #This authentication is stored in token.json file and allowing the users email id to be a test user.

    #Getting Gmail Tool kit

    #for customization
    from langchain_google_community.gmail.utils import (
        build_resource_service,
        get_gmail_credentials
    )


    #For getting gmail credentials
    credentials = get_gmail_credentials(
        scopes=["https://mail.google.com/"],
        client_secrets_file="credentials.json"

        #Token file is already generated
    )


    #Allowing API access
    api_resource = build_resource_service(credentials=credentials)


    #Creating a GmailToolKit
    gmailToolKit = GmailToolkit(api_resource=api_resource)

    return gmailToolKit


def setup_email_agent(gmailToolKit):
    # Getting tools
    tools = gmailToolKit.get_tools()

    # For Memory
    memory = MemorySaver()

    # Creating Gmail agent with access to tools and with memory
    email_agent = create_react_agent(llm, tools, checkpointer=memory)

    return email_agent


def query_email_agent(query,email_agent):

    #Configuration for memory
    config = {"configurable":{"thread_id":"emailAgentMemory"}}

    #Getting events of agent to print
    events = email_agent.stream(
        {"messages":[
                    SystemMessage(content="You are helpful email assistent who helps user with thier emails which are provided by user in query"),
                    HumanMessage(content=f"Query is :{query}")]},
        stream_mode="values",
        config=config
    )


    #A Loop for printing agent progress
    for event in events:
        event["messages"][-1].pretty_print()

    return True


def activate_email_draft_agent(generated_email,recipient_email):
    # Setting up agent for drafting email
    try:
        if os.path.exists("credentials.json"):
            if os.path.exists("Web_Scrapping/token.json"):
                # Setting up gmail toolkit

                gmailToolKit = setup_gmail_toolkit()

                if generated_email:
                    # setting up email agent

                    email_agent = setup_email_agent(gmailToolKit)

                    if email_agent:
                        # Setting up query for email agent
                        email_text = generated_email

                        # Creating a query for agent
                        email_agent_query = f"Create an email from, \n\n {email_text} and make sure that the email takes full width on screen. Draft it to {recipient_email}"

                        # Finally proving query to gmail agent for drafting generated email and calling agent to draft email
                        agent_operation = query_email_agent(email_agent_query, email_agent)


                        if agent_operation:
                            print("The Email is Successfully Drafted!! You Can check it on Gmail.")
                            return "The Email is Successfully Drafted!! You Can check it on Gmail."
                        else:
                            print("There is some problem!!")
                            return "There is some problem!!"

            else:
                print("You Need to Authorize Gmail for this operation.")
                return "You Need to Authorize Gmail for this operation."

    except Exception as e:
        print(e)
        return f"Opps some error has occurred :{e}"
if __name__ =="__main__":

    # Defining query

    text = """

    Here is a professional cold email that combines marketing and sales elements:

    Subject: Expert Project Consultant for SAP Business AI Solutions

    Dear [Recipient's Name],

    I hope this email finds you well. My name is Kamal, and I am reaching out from DRC Systems India Limited, a renowned service-based company with 12+ years of experience in development. We have a proven track record of delivering exceptional solutions that meet our clients' needs.

    I came across your requirement for a Project Consultant with expertise in SAP Business AI solutions, specifically in Machine Learning, SAP BTP, Cloud Identity services, IaSIPS, TensorFlow, scikit-learn, ABAP, Java, Python, JavaScript, NodeJS, Jupyter Notebook, Database, and Web and Cloud Computing. Our team has extensive experience in these areas, and we believe we can assist you in improving your business results.

    Our consultants have a strong background in machine learning and have successfully implemented projects that leverage the latest technology to drive business growth. We would be delighted to discuss how our expertise can benefit your organization.

    To give you a glimpse of our capabilities, I'd like to share some of our notable projects:

    * Our Machine Learning and Python expertise: https://example.com/ml-python-portfolio
    * Our experience with WordPress development: https://example.com/wordpress-portfolio

    We understand that finding the right partner for your project can be challenging. That's why we want to assure you that our team is committed to delivering high-quality solutions that meet your specific needs.

    If you're interested in learning more about how we can help, I'd be happy to set up a call to discuss your project requirements in more detail.

    Please feel free to contact me at info@drcsystems.com or reply to this email. I look forward to the opportunity to collaborate with you.

    Best regards,

    Kamal
    Marketing Department
    DRC Systems India Limited
    """

    email = "nkchauhan9090@gmail.com"

    query = f"Create an email from, \n\n {text} and make sure that the email takes full width on screen. Draft it to {email}"
    try:
        #Calling cold_email_agent for testing
        gmailToolKit = setup_gmail_toolkit()

        if gmailToolKit:
            #Setting up email agent
            email_agent = setup_email_agent(gmailToolKit)


            if email_agent:
                query = "return the Draft Id Of last email"
                email_query_result = query_email_agent(query,email_agent)

                print(email_query_result)
                if email_query_result:
                    print("\n\n\nThe Email Has been successfully drafted!")

    except Exception as e:
        print(e)