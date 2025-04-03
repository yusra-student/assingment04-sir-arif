import streamlit as st
import random
import string

# Word list for Hangman
WORD_LIST = ["python", "streamlit", "developer", "innovation", "project"]

# Initialize game state
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORD_LIST).upper()
    st.session_state.display_word = ["_" for _ in st.session_state.word]
    st.session_state.attempts = 6
    st.session_state.guessed_letters = set()
    st.session_state.wrong_guesses = []

# Function to process a guess
def process_guess(guess):
    guess = guess.upper()
    if guess in st.session_state.guessed_letters:
        st.warning("You already guessed that letter!")
    else:
        st.session_state.guessed_letters.add(guess)
        if guess in st.session_state.word:
            for i, letter in enumerate(st.session_state.word):
                if letter == guess:
                    st.session_state.display_word[i] = guess
        else:
            st.session_state.wrong_guesses.append(guess)
            st.session_state.attempts -= 1

# Streamlit UI
st.title("🎮 Hangman Game in Streamlit")
st.write("Guess the word one letter at a time!")

# Display the current word progress
st.subheader("🔠 Word Progress")
st.write(" ".join(st.session_state.display_word))

# Display incorrect guesses
st.write(f"❌ Wrong Guesses: {', '.join(st.session_state.wrong_guesses) if st.session_state.wrong_guesses else 'None'}")
st.write(f"❤️ Remaining Attempts: {st.session_state.attempts}")

# Input for guessing letters
guess = st.text_input("Enter a letter: ", max_chars=1, key="guess_input")

# Process guess when button is clicked
if st.button("Submit Guess"):
    if guess and guess in string.ascii_letters:
        process_guess(guess)
        st.rerun()
    else:
        st.warning("Please enter a valid letter!")

# Game over conditions
if "_" not in st.session_state.display_word:
    st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word}")
    st.session_state.clear()
elif st.session_state.attempts == 0:
    st.error(f"💀 Game Over! The correct word was: {st.session_state.word}")
    st.session_state.clear()
