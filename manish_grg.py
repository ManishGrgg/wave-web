from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE=THIS_DIR / "style" / "style.css"
ASSETS=THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "wave.json"

# Function to load and display the lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    

# Function to apply emoji rainfall effect
def run_snow_animation():
    rain(emoji="🤙", font_size=30, falling_speed=5, animation_length="infinite")

# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]

# Page comfiguration
st.set_page_config(page_title="Welcome to my website", page_icon="🤙")

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Displau header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Hello there !! I am Manish👋", anchor=False)
st.subheader(f"I am new to the web development and I found it very interesting!!")

# Display the lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, height=300)

st.container()
st.write("---")


st.container()
st.header("Welcome to my website!! ")
st.subheader("It is still on developmental stage 🛠️💻.  Many things are going to add up here. ")
st.subheader("So, stay tuned for amazing interfaces. Thank You !!")
st.write("---")




















