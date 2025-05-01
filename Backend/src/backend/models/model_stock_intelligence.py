from pydantic import BaseModel , Field 
from typing import Optional

# For stock Intelligence
class Stock_query(BaseModel):
    user_query : str

class Refined(BaseModel):
    entities : list[str] = Field(description = "entities mentioned if any" )
    intent  : str = Field(description = "intent of the query")
    goal    : str = Field(description = "goal of the query")
    detail_level : str = Field(default="Basic" , description = "detail level what user demands.")
    general_search_query: Optional[str] = Field(description="If the query is general, provide a well-phrased search query string to use directly for a general search.")

class ToolToCall(BaseModel):
    name : str = Field( description = "Name of the tool to call" )
    reason : str = Field( description = "contains reason why should this tool be called" )
    called_content : str  # entity name or query

class ToolSchema(BaseModel):
    name: str
    description: str

class ToolCalling(BaseModel):
    tool_call : list[ToolToCall] = Field(default = None)
