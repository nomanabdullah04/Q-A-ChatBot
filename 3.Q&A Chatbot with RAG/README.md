# RAG Document Q&A with Groq and Hugging Face

A Streamlit application for asking questions about research PDFs. The app converts the PDFs in the local `research/` folder into a FAISS vector index, retrieves relevant passages for each question, and uses Groq's `openai/gpt-oss-120b` model to answer from that context.

## What it does

- Loads PDF documents from `research/` when **Document Embedding** is clicked.
- Splits the extracted text into chunks of 1,000 characters with 250 characters of overlap.
- Creates embeddings with `sentence-transformers/all-MiniLM-L6-v2` and stores them in a FAISS index in Streamlit session state.
- Retrieves relevant document passages for a question and asks the Groq model to answer using the supplied context.
- Shows the response time and retrieved passages under **Document Similarity Search**.
- Applies the Nexus Lab dark theme and footer.

## Requirements

- Python 3.9 or newer
- A Groq API key
- PDF files to query, placed in the `research/` folder

## Setup

Create and activate a virtual environment in the project directory:

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

Install the dependencies:

```bash
python -m pip install -r requirement.txt
```

Set the Groq key as an environment variable before starting the app. You can also put it in a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your_groq_api_key
```

The application loads `.env` with `python-dotenv`. Do not commit real API keys to version control.

## Add PDF documents

Put one or more PDF files directly in the `research/` directory. The application reads that folder; it does not provide a PDF upload control. The first indexing run may download the Hugging Face embedding model, so internet access is needed for that initial download.

## Run

Start the Streamlit app from the project directory:

```bash
streamlit run main.py
```

In the app:

1. Select **Document Embedding** and wait for the vector database to finish building.
2. Enter a question in the research paper query field.
3. Read the answer and expand **Document Similarity Search** to inspect the retrieved text.

The embedding index is held in Streamlit session state. If the session resets, click **Document Embedding** again to rebuild it.

## Model and answer behavior

The Groq model is set in `main.py` to `openai/gpt-oss-120b` with temperature `0.7`. The prompt instructs the model to answer from the provided document context. There are no model-selection controls or web search in the current interface.

## Project files

```text
.
├── main.py                 # PDF indexing and RAG question-answering interface
├── style.py                # Dark theme and Nexus Lab footer
├── footer.py               # Additional footer module
├── requirement.txt         # Python dependencies
├── research/               # Place source PDFs here
└── .streamlit/config.toml  # Streamlit theme and server configuration
```
