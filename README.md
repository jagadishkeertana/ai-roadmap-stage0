\# CSV Clean API



A small FastAPI service that validates and cleans person records (name + age),

built as a Stage 0 foundations project — covers Python, Git, FastAPI, Docker, and SQL.



\## What it does



\- `clean\_data.py` — reads `people.csv`, validates each row (non-empty name, no digits

&#x20; in name, age between 1-130), writes valid rows to `people.json`. Includes logging

&#x20; and timing via a custom decorator.

\- `main\_api.py` — exposes the same validation logic as a `POST /clean` endpoint,

&#x20; accepting a JSON list of records and returning only the valid ones.

\- `setup\_db.py` — creates a small SQLite database (`people.db`) with related

&#x20; `people` and `orders` tables, used to practice joins and aggregations.



\## Setup



&#x20;   python -m venv venv

&#x20;   venv\\Scripts\\activate

&#x20;   pip install -r requirements.txt



\## Running the CSV script



&#x20;   python clean\_data.py



Reads `people.csv` in the current directory, writes `people.json`.



\## Running the API



&#x20;   uvicorn main\_api:app --reload



Visit `http://127.0.0.1:8000/docs` for interactive API docs.



\## Running with Docker



&#x20;   docker build -t csv-clean-api .

&#x20;   docker run -p 8000:8000 csv-clean-api



Visit `http://127.0.0.1:8000/docs` - same as above, now fully containerized.



\## SQL practice



&#x20;   python setup\_db.py

&#x20;   sqlite3 people.db



Includes example queries covering inner joins, left joins, aggregation with

GROUP BY / HAVING, and window functions (RANK()).



\## Stack



Python 3.12, FastAPI, Pydantic, Uvicorn, Docker, SQLite

