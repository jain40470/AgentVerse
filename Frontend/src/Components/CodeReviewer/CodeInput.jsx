import React, { useState } from "react";

const CodeInput = ({ onSubmit }) => {
  const [code, setCode] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault(); // Stops default form submission
    onSubmit(code);
  };

  return (
    <form onSubmit={handleSubmit} className="mb-6">
      <textarea
        className="w-full p-4 border-2 border-gray-300 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your code here..."
        rows={10}
      />
      <button
        type="submit"
        className="w-full mt-4 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600"
      >
        Analyze Code
      </button>
    </form>
  );
};

export default CodeInput;

