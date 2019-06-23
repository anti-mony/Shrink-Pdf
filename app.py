import subprocess
import os
from datetime import datetime
import hashlib
from flask import Flask, render_template, request, jsonify, send_file, url_for, send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
resolution = ''

from rq import Queue
from worker import conn
import uitl

q = Queue(connection=conn)


@app.route("/")
def main():
    q.enqueue(clean)
    return render_template('index.html')

@app.route("/error")
def errorPage():
    return render_template('error.html')


@app.route('/shrink',methods=['POST'])
def shrinkFile():
    f = request.files['pdffile']
    resolution = request.form['dpi']
    timeHash = hashlib.md5(str(datetime.now()).encode()).hexdigest()
    # print(f.filename)
    fname = timeHash + "_" + secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
    try:
        subprocess.check_call(['./Uploads/shrinkpdf.sh','./Uploads/'+fname,"./Uploads/Shrinked_"+resolution+"_"+fname,resolution])
    except subprocess.CalledProcessError:
        errorPage()
    # return url_for(errorPage), 500
    return jsonify(fileURL=url_for('shrinkedFile',filename='Shrinked_'+resolution+"_"+fname),
                    cfs=int(os.path.getsize("./Uploads/Shrinked_"+resolution+"_"+fname)))
 
@app.route('/Uploads/<filename>')
def shrinkedFile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run()

