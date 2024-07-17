import streamlit as st
from streamlit_option_menu import option_menu
from lyzr import QABot
from PIL import Image


st.set_page_config(
    page_title="Lyzr Disaster Simulation and Training Chatbot",
    layout="wide",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.sidebar.image(image, width=150)


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Chat'],
        icons=['house', 'chat'], menu_icon="cast", default_index=0)


@st.cache_resource
def rag_implementation():
    with st.spinner("Generating Embeddings...."):
        qa = QABot.pdf_qa(
            input_files=["Disaster.pdf"],
        )
    return qa


if selected == "Home":
    st.title("Lyzr Disaster Simulation and Training Chatbot")
    st.markdown("### Welcome to the Lyzr Disaster Simulation and Training Chatbot!")
    st.markdown(
        "This app uses Lyzr QABot to train emergency responders by simulating various disaster conditions and outcomes. We have integrated comprehensive Disaster preparedness data to provide accurate and helpful information.")
    st.markdown("##Suggested Quetions:")
    st.markdown("What items to include in a flood emergency kit?")
    st.markdown("Where to evacuate during a wildfire alert?")
    st.markdown("How to secure home before a hurricane?")



if selected == "Chat":
    st.session_state["chatbot"] = rag_implementation()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if "chatbot" in st.session_state:
        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = st.session_state["chatbot"].query(prompt)
                chat_response = response.response
                response = st.write(chat_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": chat_response}
            )
