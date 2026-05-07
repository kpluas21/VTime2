import streamlit as st
from datetime import date

from calculator import add_days, days_breakdown, format_result

st.set_page_config(page_title="Date Calculator", page_icon="📅", layout="centered")

st.title("Date Calculator")
st.caption("Add or subtract days from any date.")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start date", value=date.today())

with col2:
    num_days = st.number_input(
        "Number of days",
        value=30,
        step=1,
        min_value=-999999,
        max_value=999999,
    )

num_days = int(num_days)

st.divider()

try:
    result = add_days(start_date, num_days)
except ValueError as e:
    st.error(str(e))
    st.stop()

summary = format_result(start_date, num_days, result)
bd = days_breakdown(num_days)

st.subheader(result.strftime("%B %d, %Y").replace(" 0", " "))

for line in summary.splitlines():
    st.write(line)

if bd["direction"] != "none":
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Total days", bd["total"])
    c2.metric("Weeks", bd["weeks"])
    c3.metric("Remaining days", bd["remaining_days"])
