
# To create a virtual environment (on Windows)
# py -3 -m venv venv

# To activate it: venv\Scripts\activate
# To deactivate it: venv\Scripts\deactivate or (Powershell) just 'deactivate'

from flask import Flask, render_template

app = Flask(__name__)

# index
@app.route('/')
def index():
    return "Hello"

# /me    
@app.route("/me", methods=["GET"])
def get_results():
    return "Dummy Result"

if __name__ == "__main__":
    app.run()