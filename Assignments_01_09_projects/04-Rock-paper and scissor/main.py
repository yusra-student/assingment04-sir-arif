import streamlit as st
import random
import time

st.title("🤖 AI Decision Maker!")
st.write("Can't decide? Let AI pick for you! 🎲")

if "choices" not in st.session_state:
    st.session_state.choices = []

# User input for choices
new_choice = st.text_input("Enter an option and press 'Add':")

if st.button("➕ Add Choice"):
    if new_choice:
        st.session_state.choices.append(new_choice)
        st.success(f"✅ '{new_choice}' added!")
    else:
        st.warning("⚠️ Please enter a valid option.")

# Display current choices
if st.session_state.choices:
    st.subheader("🎯 Your Choices:")
    st.write(", ".join(st.session_state.choices))

# Decision-making button
if st.button("🎰 Pick a Random Choice"):
    if st.session_state.choices:
        st.subheader("🤔 Thinking...")
        time.sleep(1)  # Simulate suspense
        decision = random.choice(st.session_state.choices)
        st.success(f"✨ AI picked: **{decision}** 🎉")
    else:
        st.warning("⚠️ Please add some choices first!")

# Reset button
if st.button("🔄 Reset Choices"):
    st.session_state.choices = []
    st.rerun()
