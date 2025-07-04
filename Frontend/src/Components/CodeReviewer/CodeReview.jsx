import React, { useState } from 'react';
import { fetchReview } from '../../Utils/code_reviewer_api'
import CodeInput from './CodeInput';
import ReviewSummaryDisplay from './ReviewSummary';

const CodeReview = () => {
  
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false); 


  const handleSubmit = async (code) => {
    setLoading(true);
    setSummary(null); // Optional: Clear previous review
    try {
      const review = await fetchReview(code);
      setSummary(review);
    } catch (error) {
      console.error('Error fetching review:', error);
    } finally {
      setLoading(false);
    }
    // const review = await fetchReview(code);
    // setSummary(review);
  };

  return (
  
  <div className="max-w-4xl mx-auto p-6">
    <h1 className="text-3xl font-semibold mb-4 text-center text-gray-800">Code Review Assistant</h1>
    <div className="flex flex-col space-y-6 h-160 overflow-y-auto">
      <CodeInput onSubmit={handleSubmit} />
       {loading && (
          <div className="text-center text-blue-600 animate-pulse">
            Analyzing code, please wait...
          </div>
        )}
      {summary && <ReviewSummaryDisplay summary={summary} />}
    </div>
  </div>

  );
};

export default CodeReview;
