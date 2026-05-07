# Date Calculator

A lightweight date calculator built with Python and Streamlit. Enter a start date and a number of days — positive or negative — and instantly see the result with a plain-English breakdown.

**Live app:** _coming soon (deploy via Streamlit Cloud)_

## Features

- Add or subtract days from any date
- Shows result weekday and a weekend heads-up
- Breaks the total into weeks + remaining days
- Handles edge cases: zero days, large values, negative results

## Project Structure

```
VTime/
├── app.py               # Streamlit UI
├── calculator.py        # Core date logic (no external dependencies)
├── tests/
│   └── test_calculator.py
├── requirements.txt
└── README.md
```

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Running Tests

```bash
pytest tests/ -p no:playwright
```

## Deployment

1. Push to a public GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect the repo and set `app.py` as the entry point
4. Deploy — free, no credit card needed
