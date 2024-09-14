import streamlit as st
import openai

# Set up your OpenAI API key (temporarily hardcoded)
openai.api_key = "sk-DLPeERgxGO2ytWXBeJKHN-rIJmyBlBgN30QUIwN3AVT3BlbkFJtuIV4II7RAUX-Nnpz2Sp2gqSZwq561guQFVzPwAmgA"

# Function to query GPT API
def chatbot(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Streamlit app starts here
def main():
    st.title("Suhana's GPT Chat with Me")
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

# Run the main function
if __name__ == "__main__":
    main()
