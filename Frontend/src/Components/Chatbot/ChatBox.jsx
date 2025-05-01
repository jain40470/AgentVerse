import React, { useEffect, useRef } from 'react';
import Message from './Message';

const ChatBox = ({ chatHistory }) => {

  const chatEndRef = useRef(null);

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [chatHistory]);

  return (
    <div className="flex flex-col space-y-2 p-4 overflow-auto">
      {chatHistory.map((msg, index) => (
        <Message key={index} role={msg.role} content={msg.content} />
      ))}
      <div ref={chatEndRef} />
    </div>
  );
};

export default ChatBox;


// import React from 'react';
// import Message from './Message';

// const ChatBox = ({ chatHistory }) => {
//   return (
//     <div className="flex flex-col space-y-2 p-4 overflow-auto max-h-96">
//       {chatHistory.map((msg, index) => (
//         <Message key={index} role={msg.role} content={msg.content} />
//       ))}
//     </div>
//   );
// };

// export default ChatBox;
