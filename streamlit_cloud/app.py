"""Streamlit Community Cloud portfolio adapter for oop-project.

This does not replace the original implementation.
"""
from pathlib import Path

import streamlit as st

TITLE = "Flatmates Bill Splitter"
ICON = "🏠"
DESC = "Split shared bills according to how many days each flatmate stayed."
CATEGORY = "Python OOP / Bill calculator"
NOTICE = "The Streamlit calculator below is an independent adaptation of the Tkinter desktop program; no user data is uploaded."
GITHUB = "https://github.com/mohsinattasial/oop-project"
VERCEL = "https://mohsin-flatmates-splitter.vercel.app"
LOCAL_COMMAND = "python main.py"
FEATURES = ["Proportional day-based splitting","Input validation","Two-decimal currency shares"]

st.set_page_config(page_title=TITLE + " | Mohsin Atta", page_icon=ICON, layout="wide")
st.caption("Mohsin Atta · GitHub Portfolio · Streamlit Cloud edition")
st.title(ICON + " " + TITLE)
st.write(DESC)
st.caption(CATEGORY)

left, right = st.columns(2)
with left:
    st.link_button("GitHub source code", GITHUB, use_container_width=True)
with right:
    st.link_button("Existing browser version", VERCEL, use_container_width=True)

st.info(NOTICE)
with st.expander("Original project and features", expanded=False):
    for feature in FEATURES:
        st.write("• " + feature)
    st.code(LOCAL_COMMAND, language="bash")

st.subheader("Split a bill by days stayed")
total = st.number_input("Bill amount (PKR)", min_value=0.0, value=6000.0, step=100.0)
entries = st.text_area("One flatmate per line: Name, Days", value="Ali, 30\nSara, 20\nAyesha, 10", height=120)
if st.button("Calculate shares", type="primary"):
    people = []
    for number, line in enumerate(entries.splitlines(), 1):
        if not line.strip():
            continue
        try:
            name, days_text = [part.strip() for part in line.split(",", 1)]
            days = float(days_text)
            if not name or not 0 < days < float("inf"):
                raise ValueError("Invalid name or days")
            people.append((name, days))
        except ValueError:
            st.error("Line " + str(number) + ": please use Name, positive days.")
            st.stop()
    if not people:
        st.warning("Please enter at least one flatmate.")
    else:
        total_days = sum(d for _, d in people)
        amount_paisa = round(total * 100)
        allocated = 0
        output = []
        for index, (name, days) in enumerate(people):
            part = round(amount_paisa * days / total_days) if index < len(people)-1 else amount_paisa - allocated
            allocated += part
            output.append({"Flatmate": name, "Days": days, "Share (PKR)": round(part / 100, 2)})
        st.dataframe(output, use_container_width=True, hide_index=True)
        st.success("Bill distributed: Rs " + format(amount_paisa / 100, ",.2f"))

st.divider()
st.caption("© 2026 Mohsin Atta · Educational portfolio · MIT-licensed original code where applicable")
