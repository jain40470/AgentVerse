from state.state import State

class BasicChatbotNode : 

    """
    Basic Chatbot logic implementation
    """

    def __init__(self , model):
        self.llm = model
    
    def process(self , state : State):
        """
        Process the input and generate a chatbot response
        """
        return {"message" : self.llm.invoke(state["message"])}

