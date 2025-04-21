import datetime

from state.state import State
from state.state import CodeReviewerState

from nodes.node import BasicChatbotNode
from nodes.node import CodeReviewerNode

from langgraph.graph import StateGraph, START , END
from langgraph.prebuilt import tools_condition , ToolNode

# for basicChatbot
class Chatbot_GraphBuilder:

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


# For code Reviewer
class CodeReviewer_GraphBuilder:

    def __init__(self,model):

        self.llm = model
        self.graph_builder = StateGraph(CodeReviewerState)
    
    def coder_reviewer_build_graph(self):
        
        """
        Builds a CodeReviewer graph using LangGraph.
        This method initializes a chatbot node using the 'CodeReviewerNode' class
        and integrate it into the graph . The chatbot node is set as both the 
        entry and exit of graph
        """


        self.code_reviewer_node = CodeReviewerNode(self.llm)
        
        self.graph_builder.add_node("recognize_language" , self.code_reviewer_node.detect_language)
        self.graph_builder.add_node("lint_analyzer" , self.code_reviewer_node.lint_checker)
        self.graph_builder.add_node("logic_analyzer" , self.code_reviewer_node.logic_analysis)
        self.graph_builder.add_node("best_practices_to_follow",self.code_reviewer_node.best_practices)
        self.graph_builder.add_node("security_report",self.code_reviewer_node.security_check)
        
        self.graph_builder.add_node("TestCase_Generator",self.code_reviewer_node.generate_test_cases)
        self.graph_builder.add_node("Running_TestCases",self.code_reviewer_node.run_test_cases)
        self.graph_builder.add_node("TestCase_Report",self.code_reviewer_node.analyze_failed_tests)
        
        self.graph_builder.add_node("Final_Review" , self.code_reviewer_node.review_summary)
        
        self.graph_builder.add_edge(START ,"recognize_language")
        
        self.graph_builder.add_edge("recognize_language" , "lint_analyzer")  
        self.graph_builder.add_edge("recognize_language" , "logic_analyzer")
        self.graph_builder.add_edge("recognize_language" , "best_practices_to_follow")
        self.graph_builder.add_edge("recognize_language" , "security_report")
        
        self.graph_builder.add_edge("recognize_language" , "TestCase_Generator")
        self.graph_builder.add_edge("TestCase_Generator" , "Running_TestCases")
        self.graph_builder.add_edge("Running_TestCases" , "TestCase_Report")
        
        self.graph_builder.add_edge("lint_analyzer" , "Final_Review")
        self.graph_builder.add_edge("logic_analyzer" , "Final_Review")
        self.graph_builder.add_edge( "TestCase_Report" , "Final_Review")
        self.graph_builder.add_edge("best_practices_to_follow" , "Final_Review")
        
        self.graph_builder.add_edge("security_report" , "Final_Review")
        
        self.graph_builder.add_edge("Final_Review" , END)
        
        self.graph = self.graph_builder.compile()

    
    def setup_graph(self , usecase : str):
        
        """
        Set up the graph for the selected use case
        """

        if usecase == "Code Reviewer":
            self.coder_reviewer_build_graph()
        
        return self.graph_builder.compile()

