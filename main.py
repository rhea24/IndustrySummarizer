import cohere
import streamlit as st

st.write("# Industry Landscape Generator")

text = st.text_area("Enter several companies in a particular industry separated by commas and I will summarize the industry for you. ")

names = []

co = cohere.Client(api_key) # api_key variable stores Cohere API key (enter your own API key here to run the file as intended)

if (len(text)>0):
    st.write("Loading...")
    summarizePrompt = f"Generate a 5-10 paragraph summary of the industry based on the following companies: {text}"

    response = co.chat(
	    message=summarizePrompt
    )
    
    st.write(response.text)
