from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet')
def greet_person():
    # Get the value of the 'name' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('name')
    # This bot says hi to every name it gets sent!
    return f'hi {name}!'


if __name__ == '__main__':
    app.run()
