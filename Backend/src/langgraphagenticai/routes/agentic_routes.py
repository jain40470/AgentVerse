from fastapi import APIRouter, HTTPException

from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from models.request_model import MessageRequest

from graph.graph_builder import GraphBuilder
from LLMs.groqllm  import GroqLLM

router = APIRouter()

@router.post("/process-message")

def process_message(req: MessageRequest):
    
    try:
        
        obj_llm = GroqLLM()
        usecase = "Chatbot"

        model = obj_llm.get_llm_model()

        if not model:
            raise HTTPException(status_code=500, detail="LLM model could not be initialized.")

        graph_builder = GraphBuilder(model)

        try : 
            graph = graph_builder.setup_graph(usecase)
        except Exception as e :
            raise HTTPException(status_code=500, detail="Graph setup failed")
        
        messages = []

        for event in graph.stream({'message': ("user", req.message)}):
            for value in event.values():
                for msg in value["message"]:
                    messages.append(msg)
                    # role = "assistant" if isinstance(msg, AIMessage) else "user"
                    # messages.append({"role": role, "content": msg.content})

        return {"message": messages}

    except Exception as e:

        raise ValueError(f"Error occured here : {e}")
        # raise HTTPException(status_code=500, detail=str(e))

