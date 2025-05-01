from typing import Annotated , Literal , Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from models.request_model import ReviewSummary


# For basicchatbot
class State(TypedDict):

    """
    Represent the structure of state used in graph
    """

    message : Annotated[list , add_messages]


# For CodeReviewer
class CodeReviewerState(TypedDict):
    
    code : str
    language : str

    lint_checker : str  # process of using a tool, called a linter,
    # to analyze source code for errors, style issues, and potential bugs.

    logic_analysis : str
    best_practices : str
    security_analysis : str
    test_cases: str
    test_results: str
    test_analysis: str

    review_summary : ReviewSummary

    
