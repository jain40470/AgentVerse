from pydantic import BaseModel

# for YT video summary

class YTurlInput(BaseModel):
    url : str

class YTResponse(BaseModel):
    
    author : str
    author_info : str
    topic : str
    summary : str

class YTSpecialist(BaseModel):
    specialist : str
    specialist_bio : str