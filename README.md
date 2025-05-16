# 🤖 Cold Email Generator Using AI

Welcome to the **Cold Email Generator**, an AI-powered marketing tool designed to automate personalized outreach for businesses. By extracting details from job post URLs and combining them with your company's portfolio, this tool drafts highly relevant cold emails — saving time, increasing precision, and boosting client engagement.

---

## 🚀 Features

- 🔍 **Smart Job Post Parsing**  
  Automatically extracts structured data such as **job title**, **skills**, **qualifications**, **preferred experience**, and **company information** from any job post URL.

- 🧠 **LLM-Powered Personalization**  
  Uses **LangChain** and **LLaMA3** to generate customized cold emails tailored to the job post and your company’s offerings.

- 🗂️ **Portfolio Integration with ChromaDB**  
  Upload your company’s portfolio; the tool stores it as a **vectorized database** and finds the most relevant documents to attach along with the email.

- 📬 **Email Drafting via Gmail Toolkit**  
  Emails are automatically saved as **drafts** in the logged-in user's Gmail account, ready to review and send.

- 🌐 **User-Friendly Streamlit Interface**  
  Simple, elegant, and interactive web UI built with **Streamlit**.

---

## 🧰 Tech Stack

| Technology     | Purpose                                      |
|----------------|----------------------------------------------|
| 🦜 LangChain    | LLM orchestration and prompt templating      |
| 🧠 LLaMA3       | Language model for generating cold emails    |
| 📦 ChromaDB     | Vector store for portfolio document search   |
| 🌐 Streamlit    | Frontend interface for user interaction      |
| 🧰 Selenium + BS| Web scraping job post content (optional)     |
| 📧 Gmail Toolkit| Send email drafts to Gmail                   |

---

## 📌 How It Works

1. **Input Job Post URL**  
   The user provides a link to a job posting.

2. **Data Extraction**  
   The tool extracts essential details like title, skills, qualifications, and company information from the post.

3. **Portfolio Upload**  
   The user uploads the company portfolio documents, which are stored and vectorized in **ChromaDB**.

4. **Email Generation**  
   LangChain and LLaMA3 combine the extracted job data with company information to craft a **highly personalized email**.

5. **Draft to Gmail**  
   The email is automatically saved as a **draft** in the user’s Gmail account for review and sending.

---


