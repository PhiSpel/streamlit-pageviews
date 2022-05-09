import streamlit as st
from streamlit import session_state as state
from streamlit_server_state import server_state, server_state_lock

st.title("Pageview Counter Example")

with server_state_lock["gpv"]:  # Lock the "gpv" state for thread-safety
    if "gpv" not in server_state:
        server_state.gpv = 0
        
# initialize session execution count
if 'sec' not in state:
    state.sec = 0
    server_state.gpv += 1 # this should only be done on start of the page, so, the session state setup is a good place
else:
    state.sec += 1

rerun = st.button("Rerun ")

st.write("Session execution count = ", state.sec)
st.write("Global page views = ", server_state.gpv)
