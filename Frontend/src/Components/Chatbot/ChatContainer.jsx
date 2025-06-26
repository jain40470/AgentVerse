import React, { useState, useEffect } from 'react';
import ChatBox from './ChatBox';
import MessageInput from './MessageInput';
import {fetchResponse_chatbot} from '../../Utils/chatbot_api'

const ChatContainer = () => {

  const [message, setMessage] = useState(""); 
  const [chatHistory, setChatHistory] = useState([]);  
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const storedHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    setChatHistory(storedHistory);
  }, []);

  const handleSendMessage = async () => {

    if (!message) return;
    const userMessage = { role: "user", content: message };
    const updatedChatHistory = [...chatHistory, userMessage];
    setChatHistory(updatedChatHistory);
    localStorage.setItem('chatHistory', JSON.stringify(updatedChatHistory));
    setMessage("");
    setLoading(true);
    try {
      console.log(message)
      const aiMessage = await fetchResponse_chatbot(message);
      const updatedHistoryWithAI = [...updatedChatHistory, aiMessage];
      setChatHistory(updatedHistoryWithAI);
      localStorage.setItem('chatHistory', JSON.stringify(updatedHistoryWithAI));
    } catch (error) {
      console.error("Error sending message:", error);
    }
    finally{
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center bg-gray-100 min-h-screen py-6">
      <div className="bg-white rounded-lg shadow-lg w-96 p-4">
      <div className="flex-1 overflow-auto max-h-[60vh]"> {/* Chat messages */}
        <ChatBox chatHistory={chatHistory} />
        {loading && (
            <div className="text-sm text-gray-500 mt-2 animate-pulse text-center">
              Bot is typing...
            </div>
          )}
      </div>
        <MessageInput message={message} setMessage={setMessage} handleSendMessage={handleSendMessage} />
      </div>
    </div>
  );
};

export default ChatContainer;
