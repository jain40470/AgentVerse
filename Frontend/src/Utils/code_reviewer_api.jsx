import axios from 'axios'

export const fetchReview = async (code) => {
    try {
        const response = await axios.post("https://agentverse-jnkb.onrender.com/review_code", { code } );
        return response.data;
      } catch (error) {

        console.error("API Error:", error);

        const errorMessage =
        error.response?.data?.detail ||  // Full backend detail
        error.message ||                 // Axios message fallback
        "Something went wrong!";         // Final fallback
    
        alert(errorMessage); // Show entire detail as popup
        throw error;
        
      }
}
// https://agentverse-jnkb.onrender.com
// http://localhost:8000/review_code
// def fun(a , b):
// return a + b.