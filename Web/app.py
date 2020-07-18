import subprocess
import os, sys
from datetime import datetime
import hashlib
from flask import Flask, render_template, request, jsonify, send_file, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = './Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
resolution = ''

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/error", methods=["GET"])
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
    except Exception as e:
        print(e, file=sys.stderr)
        return url_for('errorPage'),500

    try:
        return jsonify(fileURL=url_for('shrinkedFile',filename='Shrinked_'+resolution+"_"+fname),
                    cfs=int(os.path.getsize("./Uploads/Shrinked_"+resolution+"_"+fname)))
    except Exception as e:
        print(e, file=sys.stderr)
        return url_for('errorPage'),500
 
@app.route('/Uploads/<filename>')
def shrinkedFile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')

