import React from 'react';
import ChatContainer from './components/Chatbot/ChatContainer';
import CodeReview from './components/CodeReviewer/CodeReview';

const App = () => {
  return (
    <>
    <CodeReview/>
    <div className="app-container">
       <ChatContainer />
    </div>
    </>
  );
};

export default App;

// I have taken help of AI for frontend css 