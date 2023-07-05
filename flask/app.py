from flask import Flask, render_template, request
import chat
import dotenv,os

dotenv.load_dotenv()

# Set up your OpenAI API credentials
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY')


app = Flask(__name__)

# Define your routes and other Flask configurations here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']
    # Use the GPT model to generate the answer
    chat_model = chat.chat_api(OPENAI_API_KEY)
    base_message = chat.message()
    base_message.load_persona()
    answer = chat_model.get_completion(base_message,message=question)

    
    return render_template('answer.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
