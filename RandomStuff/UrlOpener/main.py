from flask import Flask,render_template
from flask import request as frequest
import ast
import random
import string

app = Flask(__name__)

codes = {}
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url/<code>')
def redirect(code):
    return render_template('redirect.html',urls=codes[code])

@app.route('/createUrl',methods=['POST'])
def createUrls():
    global codes
    resp = frequest.form['urls']
    urls = resp.split(',')
    print(urls)
    c = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    codes[c] = urls
    return render_template('createUrl.html',ss="localhost:5000/url/"+(c),urls=urls)

def main():
    print("Starting server...")
    app.secret_key = "testing"
    app.run(host='0.0.0.0',debug=True)

if __name__ == '__main__':
    main()
