from openai import OpenAI
import streamlit as st
import json

# Load clubs
with open("clubs.json") as f:
    clubs = json.load(f)

client = OpenAI(api_key=st.secrets["openai_api_key"])

st.title("🎓 Club Finder")
query = st.text_input("What kind of club are you looking for?")

if st.button("Find Club") and query:
    full_data = json.dumps(clubs, indent=2)

    response = client.chat.completions.create(
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
    st.write(response.choices[0].message.content)
