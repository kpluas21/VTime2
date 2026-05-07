# Date Calculator — Claude Context

## What This Is

A Streamlit date calculator. User picks a start date and enters a number of days; the app shows the result date with a human-readable breakdown.

## Key Files

- `app.py` — UI only. No logic here.
- `calculator.py` — all date logic: `add_days`, `format_result`, `days_breakdown`
- `tests/test_calculator.py` — pytest unit tests for calculator.py

## Running

```bash
streamlit run app.py
pytest tests/ -p no:playwright
```

## Rules

- All logic lives in `calculator.py`. `app.py` only calls it.
- Standard library only for date math — no arrow, pendulum, etc.
- Type hints and a one-line docstring on every public function.
- No comments unless the why is non-obvious.
