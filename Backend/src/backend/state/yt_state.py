from typing import TypedDict

# for YT video summary
#

class YTState(TypedDict):
    url : str
    transcript : str
    author : str
    author_info : str
    topic : str
    summary : str