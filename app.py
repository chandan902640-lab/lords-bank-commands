from flask import Flask, render_template_string
from blinker import signal

app = Flask(__name__)

# Blinker signal define karein
page_visit_signal = signal('page-visit')

# Signal receiver (Listener function)
@page_visit_signal.connect
def handle_visit(sender, **kwargs):
    visitor_action = kwargs.get('action', 'unknown')
    print(f"[BLINKER EVENT] Sender: {sender} | Action: {visitor_action}")

@app.route('/')
def home():
    # Blinker signal trigger (emit) karein
    page_visit_signal.send('web-client', action='viewing-guild-bank-docs')
    
    # index.html file ko serve karein
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            return render_template_string(file.read())
    except FileNotFoundError:
        return "index.html not found! Please check repository files.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
