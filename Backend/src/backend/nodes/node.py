from state.state import State
from state.state import CodeReviewerState
from models.request_model import ReviewSummary


# for basicchatbot
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

# For code reviewer
class CodeReviewerNode:

    def __init__(self , model):
        self.llm = model

    def detect_language(self , state: CodeReviewerState):
        """
        Detect the language of the code
        """
        prompt = f"""What programming language is this code?
            {state['code']}
             Respond with just the language name."""
        response = self.llm.invoke( prompt )
        return { "language" : response.content }
    
    def lint_checker(self , state: CodeReviewerState):
        
        prompt = f"Perform linting and identify style issues in the following {state['language']} code:\n\n{state['code']}"
        response = self.llm.invoke( prompt )
        return { "lint_checker" : response.content }
    
    
    def logic_analysis(self , state: CodeReviewerState) :
        
        prompt = f"Analyze the logic of the following {state['language']} code and point out any logical errors or improvements:\n\n{state['code']}"
        response = self.llm.invoke( prompt )
    
        return {"logic_analysis" : response.content}

    def best_practices(self , state: CodeReviewerState) :
        
        prompt = f"Check whether the following {state['language']} code follows best practices and recommend any improvements:\n\n{state['code']}"
        response = self.llm.invoke( prompt )
        return { "best_practices" : response.content }
    
    def security_check(self , state: CodeReviewerState):
        
        prompt = f"Review this {state['language']} code for any security or performance issues:\n\n{state['code']}"
        response = self.llm.invoke( prompt )
        return { "security_analysis" : response.content }


    def generate_test_cases(self , state: CodeReviewerState) :
        
        prompt = f"Generate test cases for this {state['language']} code. Include normal and edge cases. Return only code:\n\n{state['code']}"
        response = self.llm.invoke( prompt )
        return { "test_cases" : response.content }
    
    
    def run_test_cases(self , state: CodeReviewerState) :
        prompt = f"""
            You're a code reviewer. Simulate running the following test cases for this {state['language']} code.
            Mark each test as pass/fail and explain failures if any.

            Code:\n{state['code']}

            Test Cases:\n{state['test_cases']}
            """
        response = self.llm.invoke( prompt )
        return { "test_results" : response.content }
    
    def analyze_failed_tests(self , state: CodeReviewerState) :

        prompt = f"""
        Analyze the failed test cases and explain what might be causing the issues.
        Also suggest how to fix the code to make them pass.
        Lets keep the report generalized and formal

        Code:\n{state['code']}
        Test Results:\n{state['test_results']}
        """
        response = self.llm.invoke( prompt )
        return { "test_analysis" : response.content }
    
    
    def review_summary(self , state: CodeReviewerState):
        
        """
        Use the LLM to generate a structured review summary aggregating all aspects.
        """
        prompt = f"""
        You're a senior software engineer and code reviewer. Based on the following analyses of a {state['language']} code snippet, write a structured final review.

        Use clear headers and concise feedback for each section:
        - Linting & Style
        - Logic & Correctness
        - Best Practices
        - Security & Performance
        - Test Case Evaluation
        - Final Verdict

        === Linting Analysis ===
        {state['lint_checker']}

        === Logic Analysis ===
        {state['logic_analysis']}

        === Best Practices ===
        {state['best_practices']}

        === Security & Performance ===
        {state['security_analysis']}

        === Test Analysis ===
        {state.get('test_analysis', 'No test analysis available')}

        Return the summary in markdown format.
        """
        response = self.llm.invoke(prompt)

        summary = ReviewSummary(
            language=state["language"],
            lint_analysis=state["lint_checker"],
            logic_analysis=state["logic_analysis"],
            best_practices=state["best_practices"],
            security_performance=state["security_analysis"],
            test_report=state.get('test_analysis', 'No test analysis available'),
            overall_comment=response.content  # LLM will generate this section
        )

        return {"review_summary": summary}
