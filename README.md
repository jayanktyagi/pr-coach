# PRCoach

PRCoach is a lightweight FastAPI-based coaching support project for ingesting review history, generating coach responses, and connecting to a Groq LLM backend.

## Features

- FastAPI application with a coach API endpoint
- CSV ingestion support for historical review data
- SQLAlchemy-based database layer
- Groq LLM integration via environment-driven configuration

## Getting Started

### Requirements

- Python 3.11+ (recommended)
- MySQL-compatible database
- `GROQ_API_KEY` for Groq API access

### Install dependencies

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root with:

```text
MYSQL_URL=mysql+pymysql://user:password@host:port/database
GROQ_API_KEY=your_groq_api_key
```

> The project uses `python-dotenv` to load `.env` automatically.

### Initialize the database

```bash
python -m scripts.init_db
```

### Run the app

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Project Structure

- `app/main.py` — FastAPI application entrypoint
- `app/api/routes/` — API route definitions
- `app/db/` — SQLAlchemy database models and session setup
- `app/llm/` — Groq client integration
- `app/ingestion/` — CSV ingestion utilities
- `app/graphs/` — Graph-based coach logic

## Environment Variables

- `MYSQL_URL` — SQLAlchemy connection string for a MySQL-compatible database
- `GROQ_API_KEY` — Groq API key for LLM access

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.
