from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Hell0'


if __name__ == '__main__':
    app.run()
