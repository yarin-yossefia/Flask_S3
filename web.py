from werkzeug.datastructures import TypeConversionDict
import s3
from flask import Flask, render_template, redirect, request, jsonify
import s3
import os
from decouple import config
key_env  =config('SECRET_ACCESS_KEY')
id_env  =config('ACCESS_KEY_ID')
print(id_env,key_env)
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
    file1 = request.form["File"].strip()
    s3.Download_file(id_env, key_env, file1)
    return redirect("/file")
app.run(host='0.0.0.0', port=80, debug=True)
