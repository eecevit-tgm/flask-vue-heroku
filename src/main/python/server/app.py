from flask import Flask

app = Flask(__name__)

# sanity check route
@app.route('/')
def index():
    return 'OK!'


if __name__ == '__main__':
    app.run()
