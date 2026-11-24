# Q&A Chatbot with Groq

A simple question-and-answer web app built with Streamlit, LangChain, and Groq. Choose a Groq model, adjust the response temperature and token limit, and ask a question in the browser.

## Features

- Uses Groq-hosted language models through LangChain's `ChatGroq` integration.
- Offers model, temperature, and maximum-token settings in the sidebar.
- Accepts the Groq API key in the app's password-protected sidebar field.
- Optionally sends tracing to LangSmith when a LangSmith API key is configured.

## Requirements

- Python 3.9 or newer
- A [Groq API key](https://console.groq.com/keys)
- Optional: a [LangSmith API key](https://smith.langchain.com/) for tracing

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the packages listed in the repository's `requirement.txt`:

```bash
python -m pip install -r requirement.txt
```

## Run

Start the Streamlit app from the project directory:

```bash
streamlit run main.py
```

Open the local URL shown in the terminal. Enter your Groq API key in the sidebar, select a model, then type a question and select **Submit**.

The models currently offered by the app are `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, and `qwen/qwen3.8-27b`. Model availability can depend on your Groq account.

## Optional LangSmith tracing

The app enables LangSmith tracing and sets the project name to `Q&A ChatBot with GroqAI`. To provide the tracing key, create a `.env` file in the project directory:

```dotenv
LANGCHAIN_API_KEY=your_langsmith_api_key
```

Without this key, the chatbot can still run; LangSmith tracing will not be authenticated. The Groq key is entered in the app and does not need to be stored in `.env`.

## Project files

- `main.py` — Streamlit interface and LangChain/Groq response generation.
- `footer.py` — renders the app footer.
- `requirement.txt` — Python dependencies.
