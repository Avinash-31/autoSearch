from flask import Flask, render_template, request, jsonify
import pyautogui as rocky
import time
import random
from questions import question

# Create a Flask app
app = Flask(__name__)

def open_edge_with_run_command():
    rocky.hotkey('win', 'r')
    time.sleep(1)
    rocky.typewrite('msedge')
    time.sleep(1)
    rocky.press('enter')
    time.sleep(3)

def google_search(query):
    rocky.typewrite(query, interval=0.04)  # Increase typing speed in Searching time {slow = 1 , fast = 0.02}
    rocky.press('enter')
    time.sleep(random.uniform(1, 4))

def close_edge():
    rocky.hotkey('alt', 'f4')
    time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_edge')
def open_edge():
    open_edge_with_run_command()
    return 'Edge opened successfully!'

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    num_questions = data.get('num_questions', 40)
    open_edge_with_run_command()
    random_questions = random.sample(question, num_questions)
    for query in random_questions:
        google_search(" " + query)
        time.sleep(3)
    close_edge()
    return jsonify({'message': 'Search completed successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') What i