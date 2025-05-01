import React from "react";
import ReviewCard from "./ReviewCard";

const ReviewSummaryDisplay = ({ summary }) => (
  <div className="mt-8">
    <h2 className="text-2xl font-semibold mb-4">Review Summary</h2>
    <ReviewCard title="Language" content={summary.language} />
    <ReviewCard title="Lint Analysis" content={summary.lint_analysis} />
    <ReviewCard title="Logic Analysis" content={summary.logic_analysis} />
    <ReviewCard title="Best Practices" content={summary.best_practices} />
    <ReviewCard title="Security & Performance" content={summary.security_performance} />
    <ReviewCard title="Test Report" content={summary.test_report} />
    <ReviewCard title="Overall Comment" content={summary.overall_comment} />
  </div>
);

export default ReviewSummaryDisplay;
