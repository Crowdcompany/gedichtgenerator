# streamlit_app.py

import os
import streamlit as st
from langchain.llms import OpenAIChat


# Set the API keys
# os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Render
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

# Create a Streamlit app
st.title("Wichtel Gedicht Generator")
st.text(" (in authentisch schlechter Qualität)")

# Get user input for the person's information
user_input = st.text_input("Geben Sie den Namen und die Schlüsselwörter für die Person ein (kommagetrennt):")
st.text("Beispiel: James Bond, Geheimagent, kein Kassenpatient, elegant, Frauenschwarm")

# Use a button to trigger execution
generate_button = st.button("Losdichten!")
st.image('https://d8wyob5mxqc1u.cloudfront.net/Allgemein/RaimundBauer180pxMagenta.png', caption='©Crowdcompany UG haftungsbeschränkt', use_column_width=False)

# Check if the button is clicked and user_input is not empty
if generate_button and user_input:
    user_input = user_input.split(',')
    name = user_input[0].strip()
    description = ','.join(user_input[1:]).strip()

    # Setup the LLM
    llm = OpenAIChat(model_name='gpt-3.5-turbo', temperature=0, max_tokens=3000)

    # Setting up the prompt with the user's input
    prompt = f"""
    You are a professional German poet, please describe {name} who has a different profession. {name} is {description}. Answer in German and make it rhyme.
    """

    # Run the llm and get the output
    response = llm(prompt)

    # Display the response
    st.subheader("Da, hat die übliche WichtelGedicht-Qualität:")
    st.write(response)
    
    
