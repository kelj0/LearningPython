import os
from flask import Flask,url_for,render_template, send_from_directory, request,redirect
from werkzeug.utils import secure_filename

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

@app.route('/upload',methods=['POST'])
def upload():
    f = request.files['file']
    if f.filename in os.listdir(os.path.join(basedir,FILES_FOLDER)):
        return redirect(url_for('index'))
    else:
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['FILES_FOLDER'], filename))
        return redirect(url_for('index'))

@app.route('/remove',methods=['POST'])
def remove():
    f = request.form['filename']
    try:
        os.remove(os.path.join(FILES_FOLDER,secure_filename(f)))
    except:
        return redirect(url_for('index')), 405
    return redirect(url_for('index')), 200

if __name__ == "__main__":
    if not os.path.exists('FILES'):
        print("FILES folder does not exist, creating new one")
        os.mkdir(os.path.join(basedir,FILES_FOLDER))
    app.run()