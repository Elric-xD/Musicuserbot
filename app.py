import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! Docker app running on Heroku.'

if __name__ == '__main__':
    # Start the userbot in the background
    print("Starting Userbot...")
    subprocess.Popen(["python3", "userbot/main.py"])
    
    # Start the Flask web server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
