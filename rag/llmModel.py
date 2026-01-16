from langchain_google_genai import ChatGoogleGenerativeAI
from envVariables import GOOGLE_API_KEY
    
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=GOOGLE_API_KEY)

print(model.invoke("Hello, world!").content)