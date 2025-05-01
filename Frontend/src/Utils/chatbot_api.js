import axios from "axios";

export const fetchResponse_chatbot = async (message) => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/chatbot", {
      message,
    });
    return {
      role: "ai",
      content: response.data.message[0].content, // Take the first message from the response
    };
  } catch (error) {
    console.error("API Error:", error);
    if (error.response) {
      // Log the response error
      console.error("Error Response:", error.response.data);
      console.error("Error Status:", error.response.status);
    } else if (error.request) {
      // Log the request error
      console.error("Error Request:", error.request);
    } else {
      console.error("Unknown Error:", error.message);
    }
    throw error;
  }
};

// https://agentverse-jnkb.onrender.com
// http://localhost:8000