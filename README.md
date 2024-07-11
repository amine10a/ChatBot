# Chat-Bot 

This is a chatbot application using the Gemini-1.5-Flash model, built with Flask.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/amine10a/ChatBot
    cd chat-bot-gemini-1.5-flash
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. Open your browser and go to `http://127.0.0.1:5000`.

## API

### POST /chat

- Send a JSON object with a `message` to receive a chatbot response.
    ```json
    {
        "message": "Hello!"
    }
    ```


