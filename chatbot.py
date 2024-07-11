import os
import google.generativeai as genai

# Set the API key directly in the script
API_KEY = "AIzaSyDsuVZ0PDtLJOIPRztwxx7KscmO94y3YLA"

# Configure the API key
genai.configure(api_key=API_KEY)

def get_response(input_text):

    generation_config = {
        "temperature": 1.25,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Create a GenerativeModel instance with the specified configuration
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    # Start a chat session
    chat_session = model.start_chat(
        history=[]
    )
    to_sent = "this site is a no content page to test you(chatbot),write any response with emojies"+input_text
    # Send the input text to the model and get the response
    response = chat_session.send_message(to_sent)
    return response.text

if __name__ == "__main__":
    rep = get_response(input_text="hi")
    print(rep)
