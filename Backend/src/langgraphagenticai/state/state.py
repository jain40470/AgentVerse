from typing import Annotated , Literal , Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import List
from langchain_core.messages import HumanMessage , AIMessage

class State(TypedDict):

    """
    Represent the structure of state used in graph
    """

    message : Annotated[list , add_messages]

    