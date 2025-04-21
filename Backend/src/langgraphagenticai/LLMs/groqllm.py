import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


class GroqLLM : 

    def __init__(self):
        
        
        self.model = "Gemma2-9b-It"
       

    def get_llm_model(self):
        
        try:

            load_dotenv()
            
            GROQ_API_KEY = os.getenv("GROQ_API_KEY")
            os.environ["GROQ_API_KEY"] = GROQ_API_KEY

            llm = ChatGroq(api_key = GROQ_API_KEY, model  = "Gemma2-9b-It")

        except Exception as e:
            
            raise ValueError(f"Error occured llm : {e}")
        
        return llm