import datetime

from state.state import State
from nodes.basic_chatbot_node import BasicChatbotNode

from langgraph.graph import StateGraph, START , END
from langgraph.prebuilt import tools_condition , ToolNode

class GraphBuilder:

    def __init__(self,model):

        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        
        """
        Builds a basic Chatbot graph using LangGraph.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrate it into the graph . The chatbot node is set as both the 
        entry and exit of graph
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot" , self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START , "chatbot")
        self.graph_builder.add_edge("chatbot",END)

    
    def setup_graph(self , usecase : str):
        
        """
        Set up the graph for the selected use case
        """

        if usecase == "Chatbot":
            self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()



