import React from 'react';
import ReactDOM from 'react-dom/client';  // Use 'react-dom/client' for React 18
import './index.css';  // Custom CSS for styling
import App from './App';

// Create a root and render the app into the root element
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
