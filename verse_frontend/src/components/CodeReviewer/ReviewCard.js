import React from "react";

// Simple parser for markdown-like formatting
const parseContent = (text) => {
  const lines = text.split("\n").filter(line => line.trim() !== "");

  const parseInlineBold = (line, keyPrefix = "") => {
    const parts = line.split(/(\*\*.*?\*\*)/g); // Split by bold markers

    return parts.map((part, i) => {
      if (part.startsWith("**") && part.endsWith("**")) {
        return <strong key={`${keyPrefix}-${i}`}>{part.slice(2, -2)}</strong>;
      }
      return <span key={`${keyPrefix}-${i}`}>{part}</span>;
    });
  };

  return lines.map((line, idx) => {
    const trimmed = line.trim();

    // Heading (line is ONLY bold, i.e., meant as a heading)
    if (trimmed.startsWith("**") && trimmed.endsWith("**") && trimmed.split("**").length === 3) {
      return <h4 key={idx} className="review-subtitle">{trimmed.replace(/\*\*/g, "")}</h4>;
    }

    // Bullet points
    if (trimmed.startsWith("*") || trimmed.startsWith("-")) {
      const content = trimmed.replace(/^(\*|-)\s*/, "");
      return <li key={idx} className="review-item">{parseInlineBold(content, `li-${idx}`)}</li>;
    }

    // Regular paragraph
    return <p key={idx} className="review-paragraph">{parseInlineBold(trimmed, `p-${idx}`)}</p>;
  });
};

// created with help of ai


const ReviewCard = ({ title, content }) => (
  <div className="review-card">
    <h3 className="review-title">{title}</h3>
    {/* <p className="review-content">{content}</p> */}
    <ul className="review-content">
        {parseContent(content)}
      </ul>
  </div>
);

export default ReviewCard;
