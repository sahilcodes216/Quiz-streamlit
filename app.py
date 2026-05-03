import streamlit as st
import random

# Page config
st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊")

st.title("✊ Rock Paper Scissors Game")
st.write("Play against the computer!")

# Initialize session state for score
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "com_score" not in st.session_state:
    st.session_state.com_score = 0

choices = {
    "rock": "rock.jpeg",
    "paper": "paper.jpeg",
    "scissor": "scissor.jpeg"
}

# User input
user_choice = st.selectbox("Choose your option", list(choices.keys()))

# Buttons
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    play = st.button("🎮 PLAY")

with col_btn2:
    reset = st.button("🔄 Reset Score")

# Reset logic
if reset:
    st.session_state.user_score = 0
    st.session_state.com_score = 0
    st.success("Score reset!")

# Game logic
if play:
    com_choice = random.choice(list(choices.keys()))

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.image(choices[user_choice], caption=f"You: {user_choice}")

    with col2:
        st.markdown("## ⚔️")

    with col3:
        st.image(choices[com_choice], caption=f"Computer: {com_choice}")

    # Determine winner
    if user_choice == com_choice:
        st.info("It's a tie! 🤝")
    elif ((user_choice == "rock" and com_choice == "scissor") or 
          (user_choice == "paper" and com_choice == "rock") or 
          (user_choice == "scissor" and com_choice == "paper")):
        st.success("You win! 🏆")
        st.session_state.user_score += 1
    else:
        st.error("You lose! 😢")
        st.session_state.com_score += 1

# Scoreboard
st.markdown("---")
st.subheader("📊 Scoreboard")

col_s1, col_s2 = st.columns(2)
col_s1.metric("Your Score", st.session_state.user_score)
col_s2.metric("Computer Score", st.session_state.com_score)
