from pydantic import BaseModel
from typing import Optional


class MessageRequest(BaseModel):
    message: str
