import React from "react";

const Home = () => {
    return (
      <div className="flex flex-col items-center justify-center h-full text-center space-y-6 px-6">
        <h1 className="text-5xl md:text-6xl font-extrabold text-gray-800">
          Welcome to <span className="text-yellow-500">AgentVerse</span>
        </h1>
        <p className="text-xl md:text-2xl text-gray-600 max-w-3xl">
          In simple words, <strong>AgentVerse</strong> is the universe of intelligent agents — a hub where powerful AI assistants come together to help you with everyday tasks.
        </p>
        <p className="text-lg md:text-xl text-gray-500 max-w-2xl">
          Whether you want to chat with an AI, get your code reviewed, analyze stocks, or summarize YouTube videos — AgentVerse does it all. It’s like a multiverse of purpose-built AI tools under one roof.
        </p>
        <div className="mt-8">
          <span className="text-gray-700 font-semibold text-lg">✨ Dive into the world of AI agents now!</span>
        </div>
      </div>
    );
  };
  
  export default Home;
  