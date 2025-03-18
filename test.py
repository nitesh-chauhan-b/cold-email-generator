from app.Web_Scrapping.query_Manager import  QuerySingleton

instance = QuerySingleton()
# instance.query = "Machine Learning"
# instance.query = "Hello"
print("The value of query is :",instance.query)