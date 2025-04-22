import React, { useState } from 'react'
import {fetchReview} from '../../utils/code_reviewer_api';
import CodeInput from './CodeInput';
import ReviewSummaryDisplay from './ReviewSummary';

const CodeReview = () => {

    const [summary , setSummary] = useState(null)

    const handleSubmit = async (code) => {
        const review = await fetchReview(code);
        setSummary(review);
    }; // passed as props

    return(
        <>
         <div className="app-container">
            <h1 className="main-header">Code Review Assistant</h1>
            <CodeInput onSubmit={handleSubmit} />
            {summary && <ReviewSummaryDisplay summary={summary} />}
         </div>
        </>
    );

};

export default CodeReview;


// revise props concept again.