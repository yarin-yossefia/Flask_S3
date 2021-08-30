import s3
from flask import Flask, render_template, redirect, request, jsonify
import s3
import os
from dotnev import load_dotnev
load_dotnev()
key_env  =os.getenv('SECRET_ACCESS_KEY')
id_env  =os.getenv('_ACCESS_KEY_ID')
app = Flask(__name__)
@app.route('/file')
def GetFile():
    if request.args.get("error") == "FileNotExist":
        error = "The File is not exist"
    else:
        error = None
    return render_template('index.html', error=error)
@app.route('/Download_file', methods=["POST"])
def download():
    id1 = request.form["Id"].strip()
    key1 = request.form["Key"].strip()
    file1 = request.form["File"].strip()
    s3.Download_file(id1 = id_env, key1=key_env, file1=file1)
    return redirect("/file")
app.run(host='0.0.0.0', port=80, debug=True)
