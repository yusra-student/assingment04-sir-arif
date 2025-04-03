import streamlit as st

def generate_story(noun, verb, adjective, adverb, place):
    return (f"One day, a {adjective} {noun} was walking {adverb} in {place}. "
            f"Suddenly, it decided to {verb} and everyone was amazed!")

def main():
    st.title("MadLibs Fun App 🎉")
    st.write("Fill in the blanks and generate a funny story!")
    
    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    adjective = st.text_input("Enter an adjective:")
    adverb = st.text_input("Enter an adverb:")
    place = st.text_input("Enter a place:")
    
    if st.button("Generate Story"):
        if noun and verb and adjective and adverb and place:
            story = generate_story(noun, verb, adjective, adverb, place)
            st.success(story)
        else:
            st.warning("Please fill in all fields before generating the story!")

if __name__ == "__main__":
    main()
