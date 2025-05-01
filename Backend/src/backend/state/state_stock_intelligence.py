from typing_extensions import TypedDict
from models.model_stock_intelligence import Refined , ToolToCall

# Stock Intelligence
class StockMessageState(TypedDict):
    user_query : str
    refined_query : Refined
    tools_to_call : list[ToolToCall] 
    content_from_tools : str 
    report : str