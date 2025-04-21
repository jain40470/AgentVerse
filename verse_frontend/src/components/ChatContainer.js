import React, { useState, useEffect } from 'react';
import ChatBox from './ChatBox';
import MessageInput from './MessageInput';
import { fetchResponse } from '../utils/api';

const ChatContainer = () => {
  const [message, setMessage] = useState("");  // User's input message
  const [chatHistory, setChatHistory] = useState([]);  // Store all messages (user + AI)

  // Load chat history from localStorage on initial load
  useEffect(() => {
    const storedHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    setChatHistory(storedHistory);
  }, []);

  // Handle sending the message
  const handleSendMessage = async () => {
    if (!message) return;

    const userMessage = { role: "user", content: message };

    // Append the user's message to the chat history
    const updatedChatHistory = [...chatHistory, userMessage];
    setChatHistory(updatedChatHistory);

    // Save updated history to localStorage
    localStorage.setItem('chatHistory', JSON.stringify(updatedChatHistory));

    // Clear the input field
    setMessage("");

    try {
      // Fetch the AI response
      const aiMessage = await fetchResponse(message);

      // Append the AI's response to the chat history
      const updatedHistoryWithAI = [...updatedChatHistory, aiMessage];
      setChatHistory(updatedHistoryWithAI);

      // Save updated history with AI response to localStorage
      localStorage.setItem('chatHistory', JSON.stringify(updatedHistoryWithAI));
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  return (
    <div className="chat-container">
      {/* Render the chat history */}
      <ChatBox chatHistory={chatHistory} />

      {/* Render the message input and send button */}
      <MessageInput message={message} setMessage={setMessage} handleSendMessage={handleSendMessage} />
    </div>
  );
};

export default ChatContainer;
