import streamlit as st
import random

choices={
    "paper":"paper.jpeg",
    "rock":"rock.jpeg",
    "scissor":"scissor.jpeg"
}
user_choice=st.selectbox("Choose your option",choices.keys())
com_choice=random.choice(list(choices.keys()))

if st.button("PLAY"):
    col1,col2,col3=st.columns([1,1,1])
    with col1:
        st.image(choices[user_choice])
    with col2:
        st.write("V/S")
    with col3:
        st.image(choices[com_choice])

     # Determine the winner
    if user_choice == com_choice:
        st.markdown("### It's a tie! 🤝")
    elif ((user_choice == "rock" and com_choice == "scissor") or 
         (user_choice == "paper" and com_choice == "rock") or 
         (user_choice == "scissor" and com_choice == "paper")):
         st.markdown("### You win! 🏆")
    else:
        st.markdown("### You lose! 😢")