import openai
import os


# Set up your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-dHdzcWcpcKJY70NLR4ZluIB4Sb25hchrQWIAul1CSmT3BlbkFJxJDEWISgiNkPY3TVEshK-1aNO6N661oGCSEsqGTUgA""
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert medical professional and Somebody who can help people with general medical queries and guide them to a correct medical professional  "},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

# Example chat interaction
user_input = input("Enter your questions here")
bot_response = chatbot(user_input)
print(f"Chatbot: {bot_response}")

import streamlit as st
import openai

# Function to query GPT API
def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app starts here
def main():
    st.title("GPT Chatbot")
    st.write("Enter your question below:")

    # Input text box for user
    user_input = st.text_input("You:", "")

    # Button to send input to chatbot
    if st.button("Submit"):
        if user_input:
            # Call the chatbot function
            response = chatbot(user_input)
            st.write(f"Chatbot: {response}")
        else:
            st.write("Please enter a message.")

# Set up your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Run the main function
if __name__ == "__main__":
    main()


streamlit
openai==0.28.0



