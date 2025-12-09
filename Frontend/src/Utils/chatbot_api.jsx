import axios from "axios";

export const fetchResponse_chatbot = async (message) => {
  try {
    const response = await axios.post("https://agentverse-jnkb.onrender.com/chatbot", {
      message,
    });
    // const response = await axios.post("http://127.0.0.1:8000/chatbot", {
    //   message,
    // });
    return {
      role: "ai",
      content: response.data.message[0].content, // Take the first message from the response
    };
  } catch (error) {

    console.error("API Error:", error);

    const errorMessage =
    error.response?.data?.detail ||  // Full backend detail
    error.message ||                 // Axios message fallback
    "Something went wrong!";         // Final fallback

    alert(errorMessage); // Show entire detail as popup
    throw error;
  
  }
};


// http://127.0.0.1:8000/chatbot
// https://agentverse-jnkb.onrender.com
// http://localhost:8000