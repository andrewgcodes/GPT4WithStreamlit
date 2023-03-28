# Import necessary libraries
import os
import streamlit as st
import openai

# Set GPT-4 API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure Streamlit page settings
st.set_page_config(page_title='GPT4 Streamlit Template',
                   layout="centered",
                   initial_sidebar_state='auto')

# Set the title of the page
st.title("GPT4 Streamlit Template")

# Display a markdown message
st.markdown(
    "Made by [@itsandrewgao](https://twitter.com/itsandrewgao).")
st.markdown("[Source code](https://github.com/andrewgcodes/GPT4WithStreamlit)")
# Display a separator line
st.write("--------------------")

# Initialize messages dictionary or retrieve from session state
if "messages" not in st.session_state:
    # CHANGE THIS MESSAGE!
    st.session_state.messages = [
        {"role": "system", "content": "You are an expert mathematics professor and teacher. Remember what you read from brilliant.org, khanacademy.org, wikipedia.org, and math.stackexchange.com. You are patient and you think step by step. You format your answers in LaTeX. You are skilled in mathematics, including calculus, probability, geometry, combinatorics, statistics, proofs, linear algebra, and more. Answer the student's questions with LaTeX."}
    ]

# Initialize 'something' in session state if not present
if 'something' not in st.session_state:
    st.session_state.something = ''

# Function to submit user input
def submit():
    st.session_state.something = st.session_state.widget
    st.session_state.widget = ''

# Function to handle GPT-4 interaction
def magic():
    try:
        # Prepare the user's query
        # CHANGE THIS MESSAGE TO PREFILL USER QUERIES WITH AN INSTRUCTION

        query = st.session_state.something + "#$Think step by step. Use LaTeX."
        if (len(st.session_state.something) < 2):
            # CHANGE THIS MESSAGE! THIS IS THE USER'S FIRST MESSAGE THAT IS AUTO-SENT

            query = "Hi, can you help me with math please?"
        
        # Add user query to messages dictionary
        st.session_state.messages.append({"role": "user", "content": query})
        
        # Request completion from GPT-4 API
        completion = openai.ChatCompletion.create(
            model="gpt-4-0314",
            messages=st.session_state.messages,
            temperature=0,
        )
        
        # Add assistant response to messages dictionary
        assistant_response = completion.choices[0].message['content']
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        # Display all messages in the conversation
        for message in st.session_state.messages:
            if message["role"] != "system":
                if message["role"] == "user":
                    st.write("You" + ": " + message["content"].split("#$")[0])
                else:
                    # CHANGE MathGPT to your AI's name
                    st.write("MathGPT" + ": " + message["content"].split("#$")[0])
                    st.write("--------------------------------------------")
    except:
        pass

# Call the magic function to handle GPT-4 interaction
magic()

# Create a text input widget for user's question
st.text_input('question', key='widget', max_chars = 500, label_visibility = "collapsed",on_change=submit)
