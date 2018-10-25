import subprocess
import os
import schedule
from flask import Flask, render_template, request, jsonify, send_file, url_for, send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
resolution = ''
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/error")
def errorPage():
    return render_template('error.html')


@app.route('/shrink',methods=['POST'])
def shrinkFile():
    f = request.files['pdffile']
    resolution = request.form['dpi']
    # print(f.filename)
    fname = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
    subprocess.call(['./Uploads/shrinkpdf.sh','./Uploads/'+fname,"./Uploads/Small_"+resolution+"_"+fname,resolution])
    
    # return url_for(errorPage), 500
    return jsonify(fileURL=url_for('shrinkedFile',filename=fname),
                    cfs=int(os.path.getsize("./Uploads/Small_"+fname)))
 
@app.route('/Uploads/<filename>')
def shrinkedFile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'Small_'+resolution+"_"+filename)

def deleteFiles():
    subprocess.call(['./Uploads/rm -rf *.pdf'])
    schedule.every().hour.do(job)

if __name__ == "__main__":
    app.run()

