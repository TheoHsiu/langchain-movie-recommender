from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd

def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask Movie Database")
    st.header("Ask The Movie Database 🎬")

    # Load the CSV file
    csv_file = "data.csv"

    if os.path.exists(csv_file):
        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))
    else:
        st.error("File 'data.csv' not found.")

if __name__ == "__main__":
    main()
