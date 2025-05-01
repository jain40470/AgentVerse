import React, { useState } from 'react';
import { fetchReview } from '../../utils/code_reviewer_api';
import CodeInput from './CodeInput';
import ReviewSummaryDisplay from './ReviewSummary';

const CodeReview = () => {
  const [summary, setSummary] = useState(null);

  const handleSubmit = async (code) => {
    const review = await fetchReview(code);
    setSummary(review);
  };

  return (
  
  <div className="max-w-4xl mx-auto p-6">
    <h1 className="text-3xl font-semibold mb-4 text-center text-gray-800">Code Review Assistant</h1>
    <div className="flex flex-col space-y-6 h-160 overflow-y-auto">
      {summary && <ReviewSummaryDisplay summary={summary} />}
      <CodeInput onSubmit={handleSubmit} />
    </div>
  </div>

  );
};

export default CodeReview;
