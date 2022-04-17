from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    welcome_message = '''
    Hello! new flask app
    ...
    You are in home page.
    '''
    return welcome_message

if __name__ == "__main__":
    app.run(debug=True)
