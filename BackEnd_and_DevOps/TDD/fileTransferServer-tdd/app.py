import os
from flask import Flask,url_for,render_template, send_from_directory

basedir = os.path.abspath(os.path.dirname(__file__))

FILES_FOLDER = "FILES"
DEBUG = True
SECRET_KEY = "change_this"

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    files = [x for x in os.listdir(os.path.join(basedir,FILES_FOLDER))]
    return render_template('index.html',files = files,current_dir=FILES_FOLDER)

@app.route('/<path:filename>')
def get_file(filename):
    return send_from_directory(directory=os.path.join(basedir,FILES_FOLDER),filename=filename)

if __name__ == "__main__":
    if not os.path.exists('FILES'):
        print("FILES folder does not exist, creating new one")
        os.mkdir(os.path.join(basedir,FILES_FOLDER))
    app.run()