from langgraph.graph import StateGraph , START , END
from state.state_stock_intelligence import StockMessageState
from nodes.node_stock_intelligence import Stock_IntelligenceNode

class Stock_Graph_Builder:

    def __init__(self,model):

        self.llm = model
        self.graph_builder = StateGraph(StockMessageState)
    
    def stock_intelligence_build_graph(self):
        
        """
        Builds a Stock Intelligence Agent graph using LangGraph.
        """

        self.node = Stock_IntelligenceNode(self.llm)
        self.graph_builder.add_node("Refining_Query", self.node.refining_query)
        self.graph_builder.add_node("Orchestrator", self.node.orchestrator)
        self.graph_builder.add_node("Agent_Calling_Tools", self.node.AgentCallingTools)
        self.graph_builder.add_node("Synthesizer",self.node.synthesizer)

        self.graph_builder.add_edge(START , "Refining_Query")
        self.graph_builder.add_edge("Refining_Query","Orchestrator")
        self.graph_builder.add_edge("Orchestrator","Agent_Calling_Tools")
        self.graph_builder.add_edge("Agent_Calling_Tools","Synthesizer")
        self.graph_builder.add_edge("Synthesizer",END)
        

    def setup_graph(self , usecase : str):
        
        """
        Set up the graph for the selected use case
        """

        if usecase == "StockAI":
            self.stock_intelligence_build_graph()

        return self.graph_builder.compile()

    