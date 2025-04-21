import axios from "axios";
export const fetchResponse_chatbot = async (message) => {
  try {
    const response = await axios.post("http://localhost:8000/chatbot", {
      message,
    });
    return {
      role: "ai",
      content: response.data.message[0].content, // Take the first message from the response
    };
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};
