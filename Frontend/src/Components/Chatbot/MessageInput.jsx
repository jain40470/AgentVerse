import React from 'react';

const MessageInput = ({ message, setMessage, handleSendMessage }) => {
  return (
    <div className="flex items-center space-x-2 mt-4">
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message"
        className="p-2 border rounded-md w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        onClick={handleSendMessage}
        className="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 focus:outline-none"
      >
        Send
      </button>
    </div>
  );
};

export default MessageInput;
