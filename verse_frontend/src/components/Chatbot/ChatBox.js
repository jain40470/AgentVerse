import React from 'react';
import Message from './Message';

const ChatBox = ({ chatHistory }) => {
  return (
    <div className="chat-box">
      {chatHistory.map((msg, index) => (
        <Message key={index} role={msg.role} content={msg.content} />
      ))}
    </div>
  );
};

export default ChatBox;