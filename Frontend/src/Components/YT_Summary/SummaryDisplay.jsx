import React from 'react';

const SummaryDisplay = ({ content }) => {

  // Parse inline **bold** text
  const formatBold = (text) => {
    const parts = text.split(/(\*\*.*?\*\*)/); // Split by bold parts
    return parts.map((part, idx) => {
      if (part.startsWith('**') && part.endsWith('**')) {
        return <strong key={idx}>{part.slice(2, -2)}</strong>;
      }
      return part;
    });
  };

  const parseSummary = (text) => {
    const lines = text.split('\n');
    const elements = [];

    let listItems = [];

    lines.forEach((line, index) => {
      if (line.startsWith('- ') || line.startsWith('* ')) {
        listItems.push(<li key={index}>{formatBold(line.slice(2))}</li>);
      } else {
        if (listItems.length > 0) {
          elements.push(
            <ul key={`ul-${index}`} className="list-disc list-inside mb-2">
              {listItems}
            </ul>
          );
          listItems = [];
        }
        if (line.trim()) {
          elements.push(
            <p key={index} className="mb-2">
              {formatBold(line)}
            </p>
          );
        }
      }
    });

    // Handle last batch of list items
    if (listItems.length > 0) {
      elements.push(
        <ul className="list-disc list-inside mb-2" key="last-ul">
          {listItems}
        </ul>
      );
    }

    return elements;
  };

  return (
    <div className="mt-8 px-4 max-w-3xl mx-auto">
      <h1 className="text-4xl font-bold mb-6 text-gray-800">{content.topic}</h1>
      <div className="text-lg leading-relaxed text-gray-700 mb-6">
        {parseSummary(content.summary)}
      </div>
      <h2 className="text-md text-gray-600">
        <span className="font-medium">Summary Written by {content.author}</span>
        {content.author_info && ` – ${content.author_info}`}
      </h2>
    </div>
  );
};

export default SummaryDisplay;
