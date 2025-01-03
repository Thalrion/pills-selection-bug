import streamlit as st

pills_options = ["Option 1", "Option 2", "Option 3"]

if "pill1" not in st.session_state:
    st.session_state.pill1 = "Option 1"
if "pill2" not in st.session_state:
    st.session_state.pill2 = "Option 2"

st.session_state.pill1 = st.pills(
    "Pills 1 with default randomly resets after selection",
    options=pills_options,
    selection_mode="single",
    key="public_selection",
    default=st.session_state.pill1
)

st.session_state.pill2 = st.pills(
    "Pills w/o default works",
    options=pills_options,
    selection_mode="single",
)

st.caption("Example Video")
st.video("streamlit-streamlit_app-2025-01-03-21-01-02.webm")
