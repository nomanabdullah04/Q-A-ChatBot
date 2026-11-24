# Nexus Lab | Groq AI Chatbot

A dark themed, conversational Q&A chatbot built with Streamlit, LangChain, and Groq. It keeps the current conversation in Streamlit session state and passes earlier turns to the model so follow-up questions have context.

## Features

- Chat-style interface with user and assistant messages.
- Conversation history during the current Streamlit session, with a **Clear Chat History** control.
- Groq model selection, temperature, and maximum response token settings in the sidebar.
- Groq API key entered in a password field in the app.
- Optional LangSmith tracing.
- Custom dark theme and Nexus Lab footer.

## Requirements

- Python 3.9 or newer
- A [Groq API key](https://console.groq.com/keys)
- Optional: a [LangSmith API key](https://smith.langchain.com/) for tracing

## Installation

Create and activate a virtual environment from the project directory:

```bash
python -m venv .venv
```

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirement.txt
```

## Run the app

```bash
streamlit run main.py
```

Open the local address printed by Streamlit. Enter your Groq API key in the sidebar, choose a model and generation settings, then ask a question in the chat input. Use **Clear Chat History** to start a fresh conversation.

The app currently offers these model IDs:

- `openai/gpt-oss-120b`
- `openai/gpt-oss-20b`
- `qwen/qwen3.8-27b`

Model availability depends on your Groq account and the provider's current catalog.

## Optional LangSmith tracing

The app enables LangSmith tracing under the project name `Q&A ChatBot with GroqAI`. To configure tracing, create a `.env` file in the project root with:

```dotenv
LANGCHAIN_API_KEY=your_langsmith_api_key
```

The Groq API key is entered in the app and does not need to be saved in `.env`. Keep API keys private and do not commit `.env` to version control.

## Project structure

```text
.
├── main.py          # Streamlit chat interface and Groq/LangChain logic
├── style.py         # Custom dark theme styles
├── footer.py        # Nexus Lab footer
├── requirement.txt  # Python dependencies
└── .streamlit/
    └── config.toml  # Streamlit theme settings
```
