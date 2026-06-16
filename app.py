from flask import Flask

demoapp = Flask(__name__)

@demoapp.route('/')
def home():
    return "Hello, World!welcome to the Docker Demo App!"

if __name__ == '__main__':
    demoapp.run(host='0.0.0.0', port=5000)