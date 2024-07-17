# Lyzr Disaster Simulation and Training Chatbot

Welcome to the **Lyzr Disaster Simulation and Training Chatbot**! This application leverages the power of Lyzr's QABot to train emergency responders by simulating various disaster scenarios and providing comprehensive preparedness data.

## Features

- **Home Page**: Overview of the app and suggested questions to ask the chatbot.
- **Chat Interface**: Interactive chat with the Lyzr QABot to get answers on disaster preparedness and response.
- **PDF Integration**: Uses a PDF file (`Disaster.pdf`) to generate embeddings for the chatbot.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/lyzr-disaster-chatbot.git
    cd lyzr-disaster-chatbot
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add your OpenAI API key**:
    - You will be prompted to enter your OpenAI API key in the sidebar when running the app.

4. **Place the necessary files**:
    - Ensure you have `Disaster.pdf` in the root directory.

## Usage

To run the Streamlit app, use the following command:

```bash
streamlit run app.py
