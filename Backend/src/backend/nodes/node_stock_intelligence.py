from langchain_core.messages import HumanMessage , SystemMessage
from state.state_stock_intelligence import StockMessageState
from models.model_stock_intelligence import Refined , ToolSchema , ToolCalling
from tools.Stock_Intelligence_tool import Stock_Tools

class Stock_IntelligenceNode:

    def __init__(self,model):

        self.llm = model
        self.tools = Stock_Tools(model)

    def refining_query(self,state : StockMessageState):
        
        prompt = [
            
            SystemMessage( content = "You are a smart assistant that extracts user intent from stock market related queries." ),
            HumanMessage( content = f"""

            User asked : { state["user_query"] }

            Return structured content in form of :

            entities : entities if mentioned 
            intent  : intent of the query
            goal : goal of the query
            detail_level : detail level what user demands.
            general_search_query: If the user's query is general (like asking about overall market situation), create a polished, complete English search query that could be used directly in a web search.

            """ )
        ]
        structured_llm = self.llm.with_structured_output(Refined)
        response = structured_llm.invoke(prompt)
        return {"refined_query" : response}
    
    def getToolinfo(self):

        tools_available = [
            
        ToolSchema(
        name="MarketDataTool",
        description="""
        Use this tool to retrieve current and historical stock performance data (30 days )for a specific company.
        It provides key financial metrics such as stock price, volume, P/E ratio, and market cap—essential for technical 
        analysis, tracking trends, and making informed investment decisions.
        Example: "Get historical stock data for Apple over the past 6 months."
        """
        ),
        ToolSchema(
        name="GeneralSearchTool",
        description="""
        Use this tool for broad, open-ended queries that require general information or exploratory context, 
        especially when the topic isn't limited to a single company. Ideal for understanding market-wide movements, 
        sector trends, macroeconomic updates, or emerging technologies impacting the stock market.
        Example: "How is the stock market performing today?" or "What are the latest trends in AI technology?"
        """
         ),
        ToolSchema(
        name="NewsTool",
        description="""
        Use this tool to retrieve the latest news articles, financial reports, and press releases related to a specific company. 
        It is particularly useful for evaluating current events, earnings announcements, product launches, or regulatory issues 
        that may influence a company's stock performance or market sentiment.
        Example: "Get the latest news about Apple to assess market-moving developments."
        """
        ),
        ToolSchema(
        name="SocialMediaTool",
        description="""
        Use this tool to analyze social media content, trends, and public sentiment related to a specific company, 
        especially in the context of stock market performance. It helps assess how public perception and user-generated 
        posts (e.g., tweets, Reddit threads) might impact investor sentiment, volatility, or trading behavior.
        Example: "Analyze recent social media sentiment around Apple before earnings call."
        """
         )]
        
        tool_list_text = "\n".join([f"{tool.name}: {tool.description.strip()}" for tool in tools_available])
        return tool_list_text

    def orchestrator(self,state: StockMessageState):
        
        tool_list_text = self.getToolinfo()    
        
        prompt = f"""
    
            You are a smart assistant that decides which stock analysis tools to call based on the user's refined query.
    
            ## Refined Query:
            - Entities: {', '.join(state["refined_query"].entities) if state["refined_query"].entities else "None"}
            - General_Search_Query: {state["refined_query"].general_search_query}
            - Intent: {state["refined_query"].intent}
            - Goal: {state["refined_query"].goal}
            - Detail_level: {state["refined_query"].detail_level}
   

        ## Tool List:
        {tool_list_text}

        ## Instructions:
        1. For each entity, determine which tools should be used to fulfill the user's intent and goal. called_content will have the entity name.
        2. Provide a detailed (detail level + what is ultimate goal with this data + reason for analzing data using this tool ) as reason for calling each tool.
        3. If General_Search_Query is not empty , don;t forget to call the GeneralSearchTool and called_content you must have General_Search_Query.

        Return the response output
    
        """

        structured_llm = self.llm.with_structured_output(ToolCalling);
        response = structured_llm.invoke(prompt)
        # print(response)
    
        return {"tools_to_call" : response.tool_call}
    
    def AgentCallingTools(self,state : StockMessageState):
        
        print(state)

        tools = state["tools_to_call"]
        query = state["refined_query"]

        tool_mapping = {
         "MarketDataTool": lambda entity , reason: self.tools.MarketData(entity , reason),
         "NewsTool": lambda entity , reason :self.tools.NewsTool(entity , reason),
         "SocialMediaTool": lambda entity , reason: self.tools.SocialMediaTool(entity , reason),
         "GeneralSearchTool": lambda query , reason: self.tools.GeneralSearchTool(query , reason),
        }

        content = ""

        if( tools ):
            
            for tool in tools:
                name = tool.name
                reason = tool.reason
                param = tool.called_content

                tool_func = tool_mapping.get(name)

                if tool_func:
                    cnt = tool_func(param, reason)
                    content = content + cnt
            
        return { "content_from_tools" : content}
    
    def synthesizer(self,state :StockMessageState) :
        
        prompt = f"""
        You are a top-tier Report Generator AI specialized in transforming structured tool outputs and metadata into polished, human-readable reports.  
        ============================================================
        📥 INPUT DATA:
        ------------------------------------------------------------
        USER QUERY:
        {state["user_query"]}

        REFINED QUERY (Parsed Insight):
        - 🎯 Intent: {state["refined_query"].intent}
        - 🎯 Goal: {state["refined_query"].goal}
        - 🔍 Entities: {state["refined_query"].entities}
        - 📊 Detail Level Requested: {state["refined_query"].detail_level}
        - 🌐 General Search Query (if provided): {state["refined_query"].general_search_query}

        RAW TOOL RESULTS:
        {state["content_from_tools"]}
        ============================================================

        🧠 YOUR TASK:
        Using the information above, generate a high-quality report that fulfills the following:

        ✅ Accurately reflects the user's **intent** and achieves the **goal**  
        ✅ Matches the **requested level of detail** (e.g., high-level summary or deep-dive analysis)  
        ✅ Uses relevant **entities** and context for clarity  
        ✅ Draws from all useful content in the tool output to create insights

        ============================================================    
        📝 REPORT FORMAT GUIDELINES:

        1. ✅ Use **clear section headings** based on the context of the content
        2. ✅ Summarize key points using **bullet points and subheadings**
        3. ✅ Use **emojis** sparingly to enhance readability and structure (not for decoration)
        4. ✅ Maintain **logical flow**, ensuring ideas build on each other clearly
        5. ✅ Avoid generic or vague output — make the report specific, informative, and engaging
        6. ✅ Ensure language is **fluent, professional, and user-focused**


        ============================================================

        📂 For stock analysis-related queries, follow this structure when relevant:
    
        -Company Overview
            - Business summary, market, key offerings
            -💰 Financial Performance
            - Revenue, profit, ratios, trends
        - Stock Performance & Valuation
             - Price movement, valuation, comparison
       
        - Recent News & Developments
             - Key events, updates, regulatory or strategic
        
        - Competitive Landscape
            - Competitors, market position, SWOT highlights

        - Analyst & Market Sentiment
             - Buy/Sell consensus, price targets, insider activity
    
        - Risk Factors
           - Volatility, regulatory, company-specific risks
        
        - Growth Potential & Strategic Outlook
             - Expansion, innovation, future plans
         
        - Summary & Recommendation
             - Overall assessment, suggested action (Buy/Sell/Hold)

        ============================================================


        🎯 FINAL GOAL:
            Deliver a **structured, polished, and valuable** report that looks as if written by an expert analyst. It should be ready to present or deliver directly to an end user.

         """

        # print("hii")
    
        response = self.llm.invoke(prompt)
    
        return { "report" : response.content }
