import streamlit as st
import pandas as pd
import numpy as np 
from datetime import datetime, timedelta


# Build a function to generate random, recent data:
def get_recent_data(last_timestamp):
    now = datetime.now()
    if now - last_timestamp > timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    
    sample_time = timedelta(seconds=0.5)
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data

# Initialize Session State values for ur app:
if "data" not in st.session_state:
    st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))

if "stream" not in st.session_state:
    st.session_state.stream = False


# Create a callback function to toggle "stream" between True and False:
def toggle_streaming():
    st.session_state.stream = not st.session_state.stream


# Define the title and sidebar. The sidebar includes buttons and slider.
st.title("Date feed")
st.sidebar.slider("Check for updates every: (secs)", 0.5, 5.0, value=1.0, key="run_every")
st.sidebar.button("Start Streaming", disabled=st.session_state.stream, on_click=toggle_streaming)
st.sidebar.button("Stop Streaming", disabled=not st.session_state.stream, on_click=toggle_streaming)

if st.session_state.stream is True:
    run_every = st.session_state.run_every
else:
    run_every = None


@st.fragment(run_every=run_every)
def show_latest_data():
    last_timestamp = st.session_state.data.index[-1] # Find the last timestamp
    new_data = get_recent_data(last_timestamp)
    st.session_state.data = pd.concat([st.session_state.data, new_data])
    st.session_state.data = st.session_state.data[-100:]
    st.line_chart(st.session_state.data)

show_latest_data()