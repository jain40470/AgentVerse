export const fetchResponse = async (message) => {
  try {
    const response = await fetch("http://localhost:8000/chatbot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch response from server");
    }

    const data = await response.json();

    // Assuming the backend returns the message with a `role` and `content`
    return {
      role: "ai",
      content: data.message[0].content, // Take the first message from the response
    };
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};
