import streamlit as st
import openai
import json

# Load the constant JSON
with open("clubs.json", "r") as f:
    clubs = json.load(f)

openai.api_key = st.secrets["openai_api_key"]

st.title("🎓 Club Finder")
st.write("Tell me what you're interested in, and I'll find the best student club for you!")

query = st.text_input("What kind of club are you looking for?")

if st.button("Find Club") and query:
    full_data = json.dumps(clubs, indent=2)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a student advisor. Given a list of student clubs and a student's interest, recommend the most relevant club and explain why."
            },
            {
                "role": "user",
                "content": f"Student said: {query}\n\nHere are the clubs:\n{full_data}"
            }
        ]
    )

    st.subheader("💡 Recommended Club")
    st.write(response.choices[0].message["content"])