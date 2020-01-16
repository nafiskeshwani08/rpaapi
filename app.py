from flask import Flask

app = Flask(__name__)

@app.route('/test1')
def index():
    return 'OK!'

if __name__ == "__main__":
    app.run()
