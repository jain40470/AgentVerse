from fastapi import APIRouter, HTTPException

from models.request_model import MessageRequest

from graph.graph_builder import Chatbot_GraphBuilder
from graph.graph_builder import CodeReviewer_GraphBuilder
from LLMs.groqllm  import GroqLLM

from models.request_model import ReviewSummary
from models.request_model import CodeInput

router = APIRouter()

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
        # raise HTTPException(status_code=500, detail=str(e))



@router.post("/chatbot")
def chatbot(req: MessageRequest):
    
    try:
        
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
        

        # check whether it is working or not
        # tgraph_builder = CodeReviewer_GraphBuilder(model)
        # tgraph = tgraph_builder.setup_graph("Code Reviewer")
        # tresponse = tgraph.invoke( {"code" : """
        #     def add(a , b) :
        #         return a + b

        #     """} )
        # print(tresponse)
        #

        messages = []

        for event in graph.stream({'message': ("user", req.message)}):
            for value in event.values():
                    role = value["message"].type
                    messages.append({"role": role, "content": value["message"].content})

        return {"message": messages}

    except Exception as e:

        raise ValueError(f"Error occured here : {e}")
        # raise HTTPException(status_code=500, detail=str(e))

