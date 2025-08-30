# Sales Data Automation Pipeline

## Overview

This project demonstrates an end-to-end automation workflow:

- **SQL**: Stores and retrieves sales data from a SQLite database.
- **Python**: Processes the data, creates summaries and charts.
- **Excel**: Generates a report with raw data, summary, and charts.
- **API**: Serves the Excel file via a Flask endpoint.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2.Initialize the database:

```bash
python create_db.py
```

3.Run the Flask API:

```bash
python app.py
```

4.Download the report:
Visit `http://127.0.0.1:5000/report` in your browser.
