from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

conversations = []

@app.route('/')
def index():
    return render_template('index.html', conversations=conversations)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = get_response(user_message)
    conversations.append({'user': user_message, 'bot': bot_response})
    return jsonify({'response': bot_response, 'conversations': conversations})

if __name__ == '__main__':
    app.run(debug=True)

