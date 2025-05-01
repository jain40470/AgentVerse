import axios from 'axios'

export const fetchStockquery = async (user_query) => {
    try {
        const response = await axios.post("http://localhost:8000/stock_agent", { user_query } );
        console.log(response.data)
        return {
          "report" : response.data["report"]
        };
      } catch (error) {
        console.error("API Error:", error);
        throw error;
      }
}