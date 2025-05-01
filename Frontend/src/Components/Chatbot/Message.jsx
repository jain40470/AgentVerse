import React from 'react';

const Message = ({ role, content }) => {
  return (
    <div className={`p-3 my-2 rounded-md ${role === 'user' ? 'bg-blue-100 self-end' : 'bg-gray-100'}`}>
      <p className={`text-sm ${role === 'user' ? 'text-blue-800' : 'text-gray-800'}`}>{content}</p>
    </div>
  );
};

export default Message;
