import streamlit as st
from streamlit_option_menu import option_menu
import random

# Sidebar navigation
navigation = st.sidebar.radio("Navigation", ["Portfolio", "Guessing Game"])

# Portfolio section
if navigation == "Portfolio":
    st.write("I have foundational knowledge of HTML, SQL, and Python, which I actively apply in my projects to enhance both functionality and design.")
    st.write("I am proficient in basic HTML for creating structured web pages, SQL for database management, and Python for data analysis and automation tasks.")
    st.write("I am constantly learning and adapting new skills to improve my technical abilities and stay updated with industry trends.")
    st.write('-----')

    # Horizontal menu
    selected = option_menu(
        menu_title=None,
        options=['About', 'Skills', 'Contact'],
        orientation='horizontal'
    )

    if selected == 'About':
        st.title("ABOUT")
        st.write("⁕ Name: Anusha")
        st.write("⁕ Father's Name: Anbazhagan")
        st.write("⁕ Place: Ariyalur")
        st.write("⁕ College: KGISL Institute of Technology")
        st.write("⁕ Course: B.Tech AI&DS") 
        st.write("⁕ Short-Term Goal: To place in a good company")
        st.write("⁕ Strength: Belief in Myself")  

    elif selected == 'Skills':
        st.title('SKILLS')
        st.write("✨ PYTHON: Beginner level, actively learning and building foundational programming skills.")
        st.write("✨ SQL: Currently learning SQL, with a focus on understanding databases and writing basic queries.")
        st.write("✨ HTML: Created a basic web page, gaining experience in structuring and styling content for the web.")
        st.write("✨ PUBLIC SPEAKING: Some experience in public speaking, comfortable presenting ideas and engaging with an audience.")

    elif selected == 'Contact':
        st.title('CONTACT')
        st.write("‣ Contact No: 9354723012")
        st.write("‣ Email: anusha6500@gmail.com")
        st.write("‣ LinkedIn profile: Anusha Anbazhagan")

# Guessing Game section
elif navigation == "Guessing Game":
    st.title("Word Guess Game")

    # Initialize session state variables if not already present
    if 'random_word' not in st.session_state:
        animals = ['rabbit', 'lion', 'tiger', 'cat', 'rat'] 
        fruits = ['orange', 'grapes', 'apple', 'pomegranate', 'pineapple']
        st.session_state.random_word = random.choice(animals + fruits)
        st.session_state.user_guesses = ''
        st.session_state.chances = 5
        st.session_state.hint = "It is an animal" if st.session_state.random_word in animals else "It is a fruit"

    st.write("** Word Guess Game **")
    st.write("Hint:", st.session_state.hint)
    
    # Display current word progress
    display_word = ' '.join([char if char in st.session_state.user_guesses else '_' for char in st.session_state.random_word])
    st.write(display_word)

    # Check if user has won
    if '_' not in display_word:
        st.success("You win! The word is: " + st.session_state.random_word)
        if st.button("Play Again"):
            st.session_state.clear()  # Reset game
    else:
        # Allow user to guess a letter
        guess = st.text_input("Guess a letter:", key="guess_input").lower()

        if guess:
            if guess not in st.session_state.user_guesses:
                st.session_state.user_guesses += guess

                if guess not in st.session_state.random_word:
                    st.session_state.chances -= 1
                    st.write("Wrong guess! You have", st.session_state.chances, "more chances.")

                # Check if user has lost
                if st.session_state.chances == 0:
                    st.error("Game over! You lose. The word was: " + st.session_state.random_word)
                    if st.button("Play Again"):
                        st.session_state.clear()