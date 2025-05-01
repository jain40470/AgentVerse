from langgraph.graph import StateGraph , START , END
from state.yt_state import YTState
from nodes.yt_node import YT_Node

class YT_GRAPH_Builder:

    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(YTState)
    
    def yt_build_graph(self):

        self.node = YT_Node(self.llm)

        self.graph_builder.add_node( "fetchTranscript" ,self.node.fetchTranscript )
        self.graph_builder.add_node( "Assigning_Topic" , self.node.assign_topic )
        self.graph_builder.add_node( "Assigning_Specialist" , self.node.assign_specialist )
        self.graph_builder.add_node( "Summary Generator",self.node.generate_summary)

        self.graph_builder.add_edge(START , "fetchTranscript")
        self.graph_builder.add_edge("fetchTranscript" , "Assigning_Topic")
        self.graph_builder.add_edge("Assigning_Topic" ,  "Assigning_Specialist")
        self.graph_builder.add_edge( "Assigning_Specialist" , "Summary Generator" )
        self.graph_builder.add_edge( "Summary Generator" , END)

    def setup_graph(self , usecase : str):

        """
        Set up the graph for the selected use case
        """

        if usecase == "YT_AI":
            self.yt_build_graph()

        return self.graph_builder.compile()

    