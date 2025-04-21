
# LG_AgentVerse

**LG_AgentVerse** is a web application that leverages LangGraph agents to create a variety of interactive use cases. Built with a FastAPI backend and a React frontend, it demonstrates different agent functionalities such as a basic chatbot and many more.

## 🚀 Features

- **FastAPI Backend**: The backend is built using FastAPI and exposes multiple endpoints for LangGraph agents to handle different tasks.
- **LangGraph Agents**: Implementations include a basic chatbot, code reviewer, and other customizable agents.
- **React Frontend**: The frontend is built with React, providing a user-friendly interface to interact with the agents.

## 📁 Project Structure

```
LG_AgentVerse/
├── Backend/src/backend/                  # Backend (FastAPI) source code
│                  └── src/               # Backend source code, API routes
│                  └── main.py
├── verse_frontend/                 # Frontend (React) code
│   └── public/               # Public assets (HTML, images)
│   └── src/                  # React components, state management
├── .gitignore                # Git ignore file
├── requirement.txt           # Backend dependencies
└── package.json              # Frontend dependencies and scripts
```

## 🛠 Installation

### Prerequisites

- Python 3.7+
- Node.js (for React frontend)

### Step 1: Clone the repository

```bash
git clone https://github.com/jain40470/LG_AgentVerse.git
cd LG_AgentVerse
```

### Step 2: Install Backend Dependencies

1. Navigate to the `backend/` directory:
   
   ```bash
   cd backend
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirement.txt
   ```

### Step 3: Install Frontend Dependencies

1. Navigate to the `frontend/` directory:

   ```bash
   cd verse_frontend
   ```

2. Install Node.js dependencies:

   ```bash
   npm install
   ```

### Step 4: Run the Application

1. Start the FastAPI backend:

   ```bash
   cd backend
   uvicorn src.main:app --reload
   ```

2. Start the React frontend:

   ```bash
   cd frontend
   npm start
   ```

   Visit `http://localhost:3000` to interact with the agents.

## 🧑‍💻 Usage

- **Basic Chatbot**: Interact with a LangGraph-powered chatbot through the frontend.
<!-- - **Code Reviewer**: Submit code snippets to get feedback and suggestions from the LangGraph agent. -->
- **Many more to add**

### Example API Usage

- **Chatbot**: Send a POST request to `/chat` with a user message to receive a response from the chatbot.
- **Code Review**: Send a POST request to `/code-review` with the code you want to be reviewed, and the agent will provide feedback.

## 📄 License

This project is licensed under the MIT License.

## 📬 Contact

For inquiries or contributions, feel free to open an issue or contact [your_email@example.com](mailto:your_email@example.com).
