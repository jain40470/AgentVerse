import React from "react";

const parseContent = (text) => {
  const lines = text.split("\n").filter(line => line.trim() !== "");

  // Parse inline bold text (i.e. **bold text**)
  const parseInlineBold = (line, keyPrefix = "") => {
    const parts = line.split(/(\*\*.*?\*\*)/g); // Split by bold markers

    return parts.map((part, i) => {
      if (part.startsWith("**") && part.endsWith("**")) {
        return <strong key={`${keyPrefix}-${i}`} className="font-bold text-blue-600">{part.slice(2, -2)}</strong>;
      }
      return <span key={`${keyPrefix}-${i}`} className="text-gray-800">{part}</span>;
    });
  };

  return lines.map((line, idx) => {
    const trimmed = line.trim();

    // Heading (line is ONLY bold, i.e., meant as a heading)
    if (trimmed.startsWith("**") && trimmed.endsWith("**") && trimmed.split("**").length === 3) {
      return (
        <h4 key={idx} className="text-2xl font-semibold text-gray-900 mt-6">{trimmed.replace(/\*\*/g, "")}</h4>
      );
    }

    // Bullet points
    if (trimmed.startsWith("*") || trimmed.startsWith("-")) {
      const content = trimmed.replace(/^(\*|-)\s*/, "");
      return (
        <li key={idx} className="ml-6 list-disc text-gray-700">
          {parseInlineBold(content, `li-${idx}`)}
        </li>
      );
    }

    // Regular paragraph
    return (
      <p key={idx} className="text-gray-800 mt-4 leading-relaxed">
        {parseInlineBold(trimmed, `p-${idx}`)}
      </p>
    );
  });
};

const ReviewCard = ({ title, content }) => (
  <div className="bg-white p-8 rounded-xl shadow-lg mb-8">
    <h3 className="text-3xl font-semibold text-indigo-600">{title}</h3>
    <ul className="mt-6 space-y-4">{parseContent(content)}</ul>
  </div>
);

export default ReviewCard;
