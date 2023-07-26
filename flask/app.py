from flask import Flask, render_template, request,jsonify,session
from prompthandler import PromptHandler
import dotenv,os
from datetime import timedelta

dotenv.load_dotenv()



app = Flask(__name__)

# Set up your OpenAI API credentials
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY')
chat_model = PromptHandler(api_key=OPENAI_API_KEY)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
# Define your routes and other Flask configurations here
@app.route('/')
def index():
    history = session.get('message_history')
    if history:
        return render_template('index.html',history=history['messages'])
    else:
        return render_template('index.html')

@app.route('/process-command', methods=['POST'])
def answer():
    command = request.json['command']
    base_history_messages = session.get('message_history')
    if base_history_messages:
        chat_model.load(base_history_messages)
    else:
        with open('static/persona.txt','r') as f:
            summary = f.read()
        chat_model.add_system(f"Hey this is the summary of the person {summary} Now pretend that you are that person",to_head=True)

    answer = chat_model.get_completion(message=command,update_history=True)
    
    session['message_history'] = chat_model.dump()
    print(answer)
    return jsonify({'output': answer})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
