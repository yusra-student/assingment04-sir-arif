import streamlit as st
import time

def init_game():
    """Initialize or reset the game session variables."""
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.attempts = 0
    st.session_state.guess = None
    st.session_state.game_over = False

st.title("🎮 AI Guess the Number Game!")
st.write("Think of a number between **1 and 100**, and I'll guess it!")

if "low" not in st.session_state:
    init_game()

if st.session_state.guess is None:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

st.subheader(f"My guess is: **{st.session_state.guess}**")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔽 Too Low"):
        st.session_state.low = st.session_state.guess + 1

with col2:
    if st.button("🔼 Too High"):
        st.session_state.high = st.session_state.guess - 1

with col3:
    if st.button("🎉 Correct!"):
        st.session_state.game_over = True
        st.success(f"🚀 I guessed it in **{st.session_state.attempts + 1}** attempts!")

if not st.session_state.game_over:
    st.session_state.attempts += 1
    time.sleep(0.5)  # Small delay for a smooth effect
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.rerun()

if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        init_game()
        st.rerun()
