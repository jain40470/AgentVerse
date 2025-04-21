from pydantic import BaseModel
from typing import Optional


# For basicchatbot 

class MessageRequest(BaseModel):
    message: str

# For CodeReviewer

class ReviewSummary(BaseModel):
    language : str
    lint_analysis: str
    logic_analysis: str
    best_practices: str
    security_performance: str
    test_report: str
    overall_comment: str

class CodeInput(BaseModel):
    code : str
