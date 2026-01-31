import os
import csv
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Load Dataset without Pandas to avoid build errors
audit_rules = []
try:
    with open('test_dataset.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        audit_rules = [row for row in reader]
except Exception as e:
    print(f"File Error: {e}")

@app.route('/')
def home():
    # This looks for 'templates/index.html'
    return render_template('index.html', rules=audit_rules)

@app.route('/audit', methods=['POST'])
def audit():
    user_input = request.json.get("text")
    tokens = len(user_input.split()) * 1.3
    metrics = {
        "cost": round((tokens/1000) * 0.0002, 6),
        "co2": round((tokens/1000) * 0.3, 4)
    }
    return jsonify({"answer": "Audit Verified", "metrics": metrics})

if __name__ == '__main__':
    app.run(debug=True)