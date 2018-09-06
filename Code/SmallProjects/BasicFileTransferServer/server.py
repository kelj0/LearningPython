#! /usr/bin/python3

import os,fileinput,re
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, session
from werkzeug.utils import secure_filename
from registration import RegistrationFrom

# =========GLOBALS=========
UPLOAD_FOLDER = os.getcwd()+'/FILES'
ALLOWED_EXTENSIONS = set(['txt','pdf','zip','7z','tar','png','jpeg','jpg','gif','mp3','mp4','py','cpp'])
STORED_FILES = [f for f in os.listdir(UPLOAD_FOLDER)\
            if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]


# Create Flash application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# =========FUNCTIONS=========
def allowed_file(filename):
    '''Returns true if file is valid to be uploaded'''
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


# =========APP.ROUTE=========
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')


@app.route('/upload',methods=['GET','POST'])
def upload_file():
    global STORED_FILES
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        f = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if f.filename == '':
            print("Someone pressed upload without selecting file!")
            return redirect(request.url)
        if f.filename in STORED_FILES:
            print("File already stored")
            return redirect(url_for('stored'))
        elif f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            STORED_FILES.append(f.filename)
            return redirect(url_for('uploaded_file',filename=filename))
        else:
            print("Bad file")
            return redirect(url_for('badfile'))
    return render_template('upload_file.html')


@app.route('/uploaded')
def uploaded_file():
    return render_template('upload_complete.html')


@app.route('/badfile')
def bad_file():
    return render_template('bad_file.html')


@app.route('/stored')
def stored():
    return render_template('stored.html')


@app.route('/files', methods=['GET'])
def show_files():
    """Generates html code based on uploaded 
    files and returns render_template(show_files.html)
    """
    noFiles = False
    with open("./templates/show_files.html", "w") as f:
        if len(STORED_FILES) is 0:
            t = '<!doctype html>\n<title>Show Files</title>\n<p>\
            <a href="{{ url_for(\'home\') }}">Go back</a>\n<h2>There are 0 stored files</h2>\n'
            noFiles = True
        else:
            t = '<!doctype html>\n<title>Show Files</title>\n<p>\
            <a href="{{ url_for(\'home\') }}">Go back</a>\n<h2>Files:(opens in new tab)</h2>\n'
        f.write(t)
    if not noFiles:
        with open("./templates/show_files.html", "a") as f:
            css = open("./templates/dropdowncss.txt").read()
            f.write(css)
            for name in STORED_FILES:
                f.write('<p><a target="_blank" rel="noopener noreferrer"  href="/files/{0}">{0}</a>\n'.format(name))
            f.write("""<div class="dropdown">\n  <button class="dropbtn">Delete files\
            </button>\n  <div class="dropdown-content">""")
            for name in STORED_FILES:
                f.write("""    <a href="/delete/{0}">{0}</a>\n""".format(name))
            f.write("  </div>\n</div>")
    return render_template('show_files.html')


@app.route('/files/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)


@app.route('/delete/<path:filename>',methods=['GET','POST'])
def delete(filename):
    global STORED_FILES
    with open('./templates/delete.html') as f:
        filedata = f.read()

    r = re.compile('<h2>Successfully deleted .*').findall(filedata)[0]
    filedata = filedata.replace(r,"<h2>Successfully deleted %s</h2>\n" % filename)
    with open('./templates/delete.html','w') as f:
        f.write(filedata)
        STORED_FILES.remove(filename)
        os.remove("./FILES/"+filename)
    return render_template('delete.html')


@app.route('/login',methods=['POST'])
def login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        return render_template('wrongpassword.html')
    return home()


@app.route('/registration',methods=['GET','POST'])
def reg():
    form = RegistrationFrom()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('RegForm/registration.html',form = form)
        else:
            return render_template('RegForm/success.html')
    else:
        return render_template('RegForm/registration.html',form = form)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

# =========ERROR HANDLERS=========


@app.errorhandler(404)
def page_not_found(e):
    return render_template('Errors/404.html'),404

# ===========================

def main():
    print("Starting server..")
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',debug=True)


if __name__ == '__main__':
    main()
