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

        const errorMessage =
        error.response?.data?.detail ||  // Full backend detail
        error.message ||                 // Axios message fallback
        "Something went wrong!";         // Final fallback
    
        alert(errorMessage); // Show entire detail as popup
        throw error;
      
        // console.error("API Error:", error);
        // throw error;
      }
}