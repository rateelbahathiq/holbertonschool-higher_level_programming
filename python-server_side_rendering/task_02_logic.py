from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_list = []

    try:
        json_path = os.path.join(os.path.dirname(__file__), 'items.json')
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, dict) and isinstance(data.get('items'), list):
                items_list = data.get('items')
    except Exception:
        # If file missing or JSON invalid, keep items_list empty
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
