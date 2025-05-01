from langchain_community.tools.tavily_search import TavilySearchResults
import yfinance as yf
from datetime import datetime, timedelta
import requests
import os

class Stock_Tools:

    def __init__(self , model):
        self.llm = model
        
    def SocialMediaTool(self,entity : str , reason : str) -> str:
        
        """
        Collect social media posts about a company or entity from platforms like Reddit, Twitter, and StockTwits.
        and summarize it.

        Args   : 
            entity : str
            reason : str
        Return :
            social media content : str
        """

        search_tool = TavilySearchResults(max_results=15)

        results = search_tool.invoke(f"""
                site:reddit.com OR site:twitter.com OR site:stocktwits.com {entity}" 
         """)

        content = []

        for r in results:
            if r.get('content') and len(r.get('content').strip()) > 100:
                content.append(
                {
                    "name" : r.get('title') ,
                    "content" : r.get('content')
                }
            )

        prompt = f"""
        
        You are a skilled financial and social media analyst AI.
        Your task is to analyze recent social media discussions about **"{entity}"** from platforms like Reddit, Twitter, and StockTwits. Focus your analysis specifically on the following objective: **"{reason}"**.

        Use the content to extract meaningful trends, sentiments, and insights that align with the purpose. Identify any key themes, unusual spikes in opinion, recurring concerns, or positive/negative signals that stand out.

        Here are the posts:
        {content}

        Please insightful summary that includes:
        1. Overall sentiment (positive/negative/mixed)
        2. Key themes or concerns discussed
        3. Any influential or viral opinions
        4. Notable bullish/bearish indicators (if financial)
        5. A final concise summary tailored to the given reason

        Be objective, descriptive and insightful.

         """

        response = self.llm.invoke(prompt)
        # print(response)
        return response.content
    
    def GeneralSearchTool(self,query : str,reason : str) -> str:

        """
         Perform a general web search to gather broader information on any topic,
         and use an LLM to synthesize a clear summary.

        Args  : 
            entity : str
            reason : str
        Return :
            content : str 
        
        """

        search_tool = TavilySearchResults(max_results=15)

        results = search_tool.run(query)

        content = []

        for r in results:
            if r.get('content') and len(r.get('content').strip()) > 100:
                content.append(
                {
                    "name" : r.get('title') ,
                    "content" : r.get('content')
                }
                )

        prompt = f""" You are a knowledgeable research assistant AI.
     
        The user is searching about: **"{query}"**.
     
        Their purpose for this research is: **"{reason}"**.

        Below are the top search results from the web:

        {content}

        Please analyze and summarize the information in a way that best supports the user's reason. Include:
        1. A focused summary relevant to the reason
        2. Key facts, statistics, and trends
        3. Diverse or opposing viewpoints (if applicable)
        4. Important recent updates (news, events, policies, etc.)
        5. A concise conclusion that helps fulfill the reason

        Be accurate, informative, and aligned with the user’s intent.

        """
        

        response = self.llm.invoke(prompt)
        # print(response)
        return response.content
    


    def MarketData(self,entity:str , reason : str) -> str:

        """
         Fetch stock prices and financial data for the past 30 days for a specific company or entity.
         and use an LLM to analyze the data based on a given reason.

         Args   : 
            entity : str
            reason : str
        Return :
            Market data content : str
        """
    
        ticker_response = self.llm.invoke(f"""
            What are the stock ticker symbol for the following company: {entity}?
            If any company doesn't exist, output None for it.
            Return the ticker only with no extra text.
        """)

        ticker = ticker_response.content.strip()
        ticker = ticker.replace("\'", "")

        a = True

        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="30d")
        except Exception as e:
            a = False
            print("Error occured in MarketData from yfinance")

        if a == False:
            summary = f"No data available for {ticker} ({entity}) over the last 30 days."
    
        else:    
            summary = f"Stock data for {ticker} i.e {entity} over the last 30 days:\n"
            for date,row in data.iterrows():
                date_str = date.strftime("%b %d, %Y")
                open_price = row["Open"]
                close_price = row["Close"]
                volume = row["Volume"]    
                summary += f"Date: {date_str}, Open: ${open_price:.2f}, Close: ${close_price:.2f}, Volume: {volume}\n"

        prompt = f"""
        
        You are a stock market analyst.

        A user is interested in analyzing the recent 30-day performance of {ticker} ({entity}) for the following reason: "{reason}".

        Below is the daily stock data (open, close, volume):

        {summary}

        Please analyze this data to:
        1. Identify any short-term trends or patterns
        2. Mention any volatility or price consistency
        3. Highlight any trading signals or market sentiment
        4. Provide a summary tailored to the user's reason

        Be precise, insightful.
        """

        # Step 5: Run the LLM on the prompt
        response = self.llm.invoke(prompt)

        return response.content
    

    def NewsTool(self,entity : str , reason : str) -> str:
        
        """
        Retrieve the latest news headlines related to a company or entity. and
        and use an LLM to analyze and summarize the news based on a specific reason.

        Args   : 
            entity : str
            reason : str 
        Output :
            news related content : str
        """
        
        url = f'https://gnews.io/api/v4/search?q={entity}&lang=en&token={os.environ["GNEWS_API_KEY"]}'
        response = requests.get(url)
        data = response.json()
        if data.get("articles"):
            headlines = [article["title"] for article in data["articles"]]
            content = f"News for {entity}:\n" + "\n".join(headlines) + "\n"
        else:
            content = f"No news found for {entity}.\n"
    

        prompt = f"""
        You are a news analyst AI.
        The user is researching recent news about {entity} with the following reason: "{reason}".

        Here are the latest headlines:

        {content}

        Please provide a summary of the key news trends and insights based on the user's reason. Include:
        1. Relevant trends or developments from the headlines
        2. Sentiment of the news (e.g., positive, negative, neutral)
        3. Key takeaways or potential impacts on the company/market
        4. Concise conclusions or recommendations based on the reason

        Be insightful and structured.
        """

        response = self.llm.invoke( prompt )

        return response.content
