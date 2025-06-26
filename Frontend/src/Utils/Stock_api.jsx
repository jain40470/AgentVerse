import axios from 'axios'

export const fetchStockquery = async (user_query) => {
    try {
        const response = await axios.post("https://agentverse-jnkb.onrender.com/stock_agent", { user_query } );
        console.log(response.data)
        return {
          "report" : response.data["report"]
        };
      } catch (error) {
        console.error("API Error:", error);
        throw error;
      }
}