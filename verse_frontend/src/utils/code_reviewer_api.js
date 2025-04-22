import axios from 'axios'

export const fetchReview = async (code) => {
    try {
        const response = await axios.post("http://localhost:8000/review_code", { code } );
        return response.data;
      } catch (error) {
        console.error("API Error:", error);
        throw error;
      }
}