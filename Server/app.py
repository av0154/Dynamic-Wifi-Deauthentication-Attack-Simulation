from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    
    ssid = request.form['ssid']
    bssid = request.form['bssid']
    subprocess.Popen(['python3', '../client/deauth.py', ssid, bssid])
    return "Attack started!"

if __name__ == '__main__':
    app.run(debug=True)