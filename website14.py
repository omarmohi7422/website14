from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run locally: python website14.py  then open http://127.0.0.1:5000
    app.run(debug=True)
