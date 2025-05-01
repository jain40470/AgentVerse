from fastapi import APIRouter, HTTPException

from models.request_model import MessageRequest

from graph.graph_builder import Chatbot_GraphBuilder
from graph.graph_builder import CodeReviewer_GraphBuilder
from graph.Graph_Builder_Stock_Intelligence import Stock_Graph_Builder
from graph.Yt_graph import YT_GRAPH_Builder

from LLMs.groqllm  import GroqLLM

from models.request_model import ReviewSummary
from models.request_model import CodeInput
from models.model_stock_intelligence import Stock_query 
from models.yt_model import YTResponse , YTurlInput

router = APIRouter()

#Stock intelligence.
@router.post("/stock_agent")
def stock_intelligence_agent(req : Stock_query):
    
    raw = req.user_query
    print("RAW BODY:\n", raw)

    try:
        
        usecase = "StockAI"
        obj_llm = GroqLLM()
        model = obj_llm.get_llm_model()

        if not model:
            print("hi1")
            raise HTTPException(status_code=500, detail="LLM model could not be initialized.")

        graph_builder = Stock_Graph_Builder(model)

        try : 
            graph = graph_builder.setup_graph(usecase)
        except Exception as e :
            print("hi2")
            raise HTTPException(status_code=500, detail="Graph setup failed")
        
        # response = graph.invoke({"user_query" : "check the stock market"})
        response = graph.invoke({"user_query" : raw })
        report = response["report"].strip()
        return {"report" : report}
    
    except Exception as e:
        print("hi3")
        raise ValueError(f"Error occured here : {e}")


# For YT_Transript Analsysis
@router.post("/yt_transcript_analysis" , response_model = YTResponse)
def yt_transcript_analysis(req : YTurlInput):
    
    try:

        obj_llm = GroqLLM()
        usecase = "YT_AI"
        model = obj_llm.get_llm_model()
        print(req.url)
        if not model:
            raise HTTPException(status_code=500, detail="LLM model could not be initialized.")
        graph_builder = YT_GRAPH_Builder(model)
        try : 
            graph = graph_builder.setup_graph(usecase)
        except Exception as e :
            raise HTTPException(status_code=500, detail="Graph setup failed")
        
        response = graph.invoke( {"url" : req.url })
        content = {
            "author" : response["author"],
            "author_info" : response["author_info"],
            "topic" : response["topic"],
            "summary" : response["summary"]
        }
        return content
    
    except Exception as e:

        raise ValueError(f"Error occured here : {e}")

# code Reviewer
@router.post("/review_code" , response_model = ReviewSummary)
def code_reviewer(req : CodeInput ):
    
    try:
        
        obj_llm = GroqLLM()
        usecase = "Code Reviewer"

        model = obj_llm.get_llm_model()

        if not model:
            raise HTTPException(status_code=500, detail="LLM model could not be initialized.")

        graph_builder = CodeReviewer_GraphBuilder(model)
        try : 
            graph = graph_builder.setup_graph(usecase)
        except Exception as e :
            raise HTTPException(status_code=500, detail="Graph setup failed")
        
        response = graph.invoke( {"code" : req.code })
        # print(req.code)
        # print(response)
        summary_data = response.get("review_summary", {})
        return summary_data
    
    except Exception as e:

        raise ValueError(f"Error occured here : {e}")
    

# basic chatbot
@router.post("/chatbot")
def chatbot(req: MessageRequest):
    
    try:

        print(req.message)
        
        obj_llm = GroqLLM()
        usecase = "Chatbot"

        model = obj_llm.get_llm_model()

        if not model:
            raise HTTPException(status_code=500, detail="LLM model could not be initialized.")

        graph_builder = Chatbot_GraphBuilder(model)
        try : 
            graph = graph_builder.setup_graph(usecase)
        except Exception as e :
            raise HTTPException(status_code=500, detail="Graph setup failed")
        
        messages = []

        for event in graph.stream({'message': ("user", req.message)}):
            for value in event.values():
                    role = value["message"].type
                    messages.append({"role": role, "content": value["message"].content})

        return {"message": messages}

    except Exception as e:

        return {"message": f"Error occured here : {e}"}

