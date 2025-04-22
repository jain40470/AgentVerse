import React from 'react';

import { useState } from 'react';

import ChatContainer from './components/Chatbot/ChatContainer';
import CodeReview from './components/CodeReviewer/CodeReview';

const App = () => {

  const [activeTab, setActiveTab] = useState("codeReview"); // or "chat"

  return (
    <>
    <div className="tab-buttons">
        <button onClick={() => setActiveTab("codeReview")}>
          Code Review
        </button>
        <button onClick={() => setActiveTab("chat")}>
          Chat
        </button>
    </div>
    <div>
      
      {activeTab === "codeReview" && <CodeReview />}
      {activeTab === "chat" && <ChatContainer />}
      
    </div>
    </>
  
);

};

export default App;

// I have taken help of AI for frontend css 