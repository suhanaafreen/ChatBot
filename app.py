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
    st.title("Suhana's GPT chat with me ")
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
openai_api_key = "sk-dHdzcWcpcKJY70NLR4ZluIB4Sb25hchrQWIAul1CSmT3BlbkFJxJDEWISgiNkPY3TVEshK-1aNO6N661oGCSEsqGTUgA"

# Run the main function
if __name__ == "__main__":
    main()
