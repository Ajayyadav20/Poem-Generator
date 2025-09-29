import streamlit as st
from openai import AzureOpenAI

# Set page configuration
st.set_page_config(
    page_title="Poetica",  # title in browser tab
    page_icon="🌸",
    layout="centered"
)

# Load Azure OpenAI credentials from Streamlit Secrets
AZURE_OPENAI_API_KEY = st.secrets["AZURE_OPENAI_API_KEY"]
AZURE_ENDPOINT = st.secrets["AZURE_ENDPOINT"]
AZURE_API_VERSION = st.secrets["AZURE_API_VERSION"]
AZURE_DEPLOYMENT_NAME = st.secrets["AZURE_DEPLOYMENT_NAME"]

# Initialize Azure client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT
)

# Streamlit UI
st.title("🌸Poetica - personal poet")
st.write("Enter a theme, and I’ll generate a short poem for you!")

theme = st.text_input("Enter a theme (e.g., friendship, nature, space)")

if st.button("Generate Poem"):
    if theme.strip() != "":
        try:
            response = client.chat.completions.create(
                model=AZURE_DEPLOYMENT_NAME,  # use your deployment name
                messages=[
                    {"role": "system", "content": "You are a creative poet."},
                    {"role": "user", "content": f"Write a short 4-line poem about {theme}."}
                ],
                temperature=0.8
            )
            poem = response.choices[0].message.content
            st.success(poem)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a theme before generating.")
