from flask import Flask, request
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return "Hello World"


@app.route('/contact')
def contact():
    return "You can contact me at 232-123-123, or  email me at test@o2.pl"


@app.route('/log', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # logic
        pass
    else:
        # display login form
        return "test"

if __name__ == "__main__":
    app.run()
