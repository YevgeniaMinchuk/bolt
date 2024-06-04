import json
from difflib import get_close_matches
from flask import Flask, request, render_template

app = Flask(__name__)

# Load knowledge from json file
def load_knowledge(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        # insert new data into json file
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    # n is the amount of answers, cutoff is the margin of accuracy in response
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.8)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge: dict) -> str | None:
    for q in knowledge["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None
        
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    knowledge: dict = load_knowledge('knowledge.json')
    question: str = ''
    answer: str = ''

    if request.method == 'POST':
        question = request.form['question']
        best_match: str = find_best_match(question, [q["question"] for q in knowledge["questions"]])
        if best_match:
            answer = get_answer_for_question(best_match, knowledge)
        else:
            answer = "Sorry, I don't know the answer. Please provide a response or type 'skip' to skip the response."

    return render_template('index.html', question=question, answer=answer)

@app.route('/new_answer', methods=['POST'])
def new_answer():
    knowledge: dict = load_knowledge('knowledge.json')
    question: str = request.form['question']
    new_answer: str = request.form['new_answer']

    if new_answer.lower() != 'skip':
        knowledge["questions"].append({"question": question, "answer": new_answer})
        save_knowledge('knowledge.json', knowledge)
        return render_template('index.html', question='', answer='Thank you! I have learned a new response.')
    else:
        return render_template('index.html', question='', answer='No worries! Please say something else.')

if __name__ == '__main__':
    app.run(debug=True)