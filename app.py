import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allwed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def judegeDog(filepath):
    result = subprocess.check_output(["python3", "label_image.py", "--image", filepath,
                                      "--graph", "retrained_graph.pb",  "--labels", "retrained_labels.txt"])
    return result


@app.route('/', methods=['GET', 'POST'])
def uploads_file():
    html = render_template('index.html')
    if request.method == 'POST':
        file = request.files['file']
        if file and allwed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return redirect(url_for('result_page', filename=filename))
    return html


@app.route('/result/<filename>')
def result_page(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    result = judegeDog(filepath)
    return render_template('result.html', result=result, filename=filename)


@app.route('/image/<filename>')
def image_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
