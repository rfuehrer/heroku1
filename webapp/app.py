import os

from flask import Flask

app = Flask(__name__, static_url_path='/apt/webapp')

@app.route('/')
#def hello():
#    return 'Hello world!'
def root():
    return app.send_static_file('index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
