import streamlit as st
import requests

# Streamlit app title
st.title("AI Virtual Career Counsellor")

# Text input for user query
user_input = st.text_input("Enter your skills or interests:")

# Button to send input to Rasa
if st.button("Get Recommendation"):
    try:
        # Send request to Rasa REST API
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input}
        )

        # If response is OK
        if response.status_code == 200:
            messages = response.json()
            if messages:
                for msg in messages:
                    st.write(msg.get("text", ""))
            else:
                st.warning("No response from bot.")
        else:
            st.error(f"Error {response.status_code}: Could not connect to Rasa server.")

    except Exception as e:
        st.error(f"Exception occurred: {e}")
