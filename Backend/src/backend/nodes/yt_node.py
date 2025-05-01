from state.yt_state import YTState
from langchain_community.document_loaders import YoutubeLoader
from models.yt_model import YTSpecialist

from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound
import re

class YT_Node:

    def __init__(self,model):
        self.llm = model


    def extract_video_id(self,url: str) -> str:
        
        """
         Extracts the YouTube video ID from various URL formats.
        """
        patterns = [
            r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:\?|&|$)",  # matches watch?v=, /embed/, /youtu.be/
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return "invalid_video_id"


    def fetchTranscript(self,state : YTState):

        try:

            video_id = self.extract_video_id(state["url"])
            if video_id == "invalid_video_id":
                return {"transcript": "No such video exists"}

             # Reconstruct a clean URL
            clean_url = f"https://www.youtube.com/watch?v={video_id}"
            
            # Load YouTube video content using the URL from state
            loader = YoutubeLoader.from_youtube_url(clean_url, add_video_info=False)
            response = loader.load()

            # Check if the transcript is available
            if response and hasattr(response[0], 'page_content') and response[0].page_content:
                return {"transcript": response[0].page_content}
            else:
                return {"transcript": "Transcript not available"}
    
        except Exception as e:
            # If any error occurs (e.g., invalid URL, failed video loading), return an appropriate message
            return {"transcript": f"{e}"}
        
    
    def assign_topic(self,state : YTState):
        
        prompt = f"""
            You are an AI assistant that identifies the main topic of a transcript.
            Please read the following excerpt from a transcript and determine the **primary topic** being discussed. Be concise and return **only the topic** as a short phrase or sentence, without any additional explanation or formatting.
            Transcript:{state['transcript'][:2000]}  
            In output i want only the topic 
        """
        response = self.llm.invoke(prompt)
        return {"topic": response.content}
    
    def assign_specialist(self,state : YTState):
        
        prompt = f""" You are an AI assistant responsible for assigning the most appropriate real-world expert or well-known specialist to summarize content on a specific topic.

        The expert must be:
        - A real, existing person (no fictional or AI-generated names)
        - Recognized in their field with proven credentials or contributions
        - Relevant to the given topic, either through academic, industry, or public work

         Topic: "{state["topic"]}"
        Return me :
        specialist : Name of person/expert
        specialist_bio : A short background on the expert — who they are and why they're relevant to this topic.

        """
    
        structured_llm = self.llm.with_structured_output(YTSpecialist)
        response = structured_llm.invoke(prompt)

        # print(response.specialist)
         # print(response.specialist_bio)

        return {
        "author" : response.specialist , 
        "author_info" : response.specialist_bio
         }
    
    def generate_summary(self,state : YTState):
        
        prompt = f""" 
        
       You are {state["author"]}, widely recognized for: {state["author_info"]}.
       
       Your task is to generate a **detailed, entailed summary** of the following YouTube transcript. The summary should sound like it's written entirely in your **unique voice**—reflecting your tone, perspective, and domain expertise.

        Instructions:
        - Write a **detailed summary** that thoroughly captures all key points, arguments, examples, and conclusions.
        - Every statement must be **entailed**—fully supported by the content in the transcript (no hallucinations or external assumptions).
        - Reflect the **structure and progression** of ideas in the transcript.
        - Use a style and vocabulary that **aligns with how you speak or write** to your audience (e.g., blog, podcast, or talk).
        - Organize the summary in a logical and readable way (bullet points or short paragraphs if needed).

         **Topic**:  
        {state["topic"]}

         **Transcript**:  
        {state["transcript"][:3000]}

        Only return the detailed summary, nothing else.
         """
        
        response = self.llm.invoke(prompt)
        
        return {
            "summary": response.content
        }