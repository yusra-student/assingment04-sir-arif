import streamlit as st
import time

# Initialize session state variables
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False
if "time_left" not in st.session_state:
    st.session_state.time_left = 0

# Function to start the timer
def start_timer():
    st.session_state.timer_running = True
    while st.session_state.time_left > 0 and st.session_state.timer_running:
        mins, secs = divmod(st.session_state.time_left, 60)
        st.write(f"⏳ Time Left: {mins:02d}:{secs:02d}")
        time.sleep(1)
        st.session_state.time_left -= 1
        st.rerun()

    if st.session_state.time_left == 0:
        st.success("🎉 Time's up!")

# Streamlit UI
st.title("⏳ Countdown Timer in Streamlit")

# User input for countdown time
hours = st.number_input("Hours:", min_value=0, max_value=24, value=0, step=1)
minutes = st.number_input("Minutes:", min_value=0, max_value=59, value=0, step=1)
seconds = st.number_input("Seconds:", min_value=0, max_value=59, value=0, step=1)

# Set the total time when the user clicks "Set Timer"
if st.button("Set Timer"):
    st.session_state.time_left = (hours * 3600) + (minutes * 60) + seconds
    st.session_state.timer_running = False
    st.rerun()

# Start the countdown
if st.button("Start") and st.session_state.time_left > 0:
    start_timer()

# Stop the countdown
if st.button("Pause"):
    st.session_state.timer_running = False

# Reset the countdown
if st.button("Reset"):
    st.session_state.timer_running = False
    st.session_state.time_left = 0
    st.rerun()
