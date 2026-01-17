from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Location-Based Business Success Prediction System is running!"

if __name__ == '__main__':
    app.run(debug=True)
