import axios from 'axios'

export const fetchYtUrl = async (url) => {
    try {
        const response = await axios.post("https://agentverse-jnkb.onrender.com/yt_transcript_analysis", { url } );
        return  {
          "author" : response.data["author"],
          "author_info" : response.data["author_info"],
          "topic" : response.data["topic"],
          "summary" : response.data["summary"]
        }
      } catch (error) {
        console.error("API Error:", error);
        throw error;
      }
}