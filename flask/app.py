from flask import Flask, render_template, request,jsonify,session
import chat
import dotenv,os
from datetime import timedelta

dotenv.load_dotenv()



app = Flask(__name__)

# Set up your OpenAI API credentials
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY')
chat_model = chat.chat_api(OPENAI_API_KEY)
app.secret_key = os.environ.get('SECRET_KEY')
# Define your routes and other Flask configurations here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-command', methods=['POST'])
def answer():
    command = request.json['command']
    base_history_messages = session.get('message_history')
    base_history = chat.message()
    if base_history_messages:
        base_history.messages = base_history_messages
    else:
        base_history.load_persona()
    print(base_history.messages)
    answer = chat_model.get_completion(base_history,message=command,update_history=True)
    session['message_history'] = base_history.messages
    
    return jsonify({'output': answer})

if __name__ == '__main__':
    app.run(debug=True)
