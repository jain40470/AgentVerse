import React from 'react';
import Message from './Message';

const ChatBox = ({ chatHistory }) => {
  return (
    <div className="flex flex-col space-y-2 p-4 overflow-auto max-h-96">
      {chatHistory.map((msg, index) => (
        <Message key={index} role={msg.role} content={msg.content} />
      ))}
    </div>
  );
};

export default ChatBox;
