import os
from src.text import *
from src.MyRegex import *
from flask import Flask, render_template, request, redirect, url_for, send_from_directory


# Initialize the Flask application
app = Flask(__name__)

# Path untuk menyimpan multiple file
app.config['UPLOAD_FOLDER'] = 'uploads/'
# Ekstensi file yang diterima

app.config['ALLOWED_EXTENSIONS'] = set(['txt'])

# Menyeleksi ekstensi file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result', methods=['POST'])
def result():
    option = request.form['options']
    tek = request.form['fname']
    
    uploaded_files = request.files.getlist("file[]")
    files = []
    for file in uploaded_files:
        # Cek apakah file ekstensinya sesuai yang diminta
        if file and allowed_file(file.filename):
            filename = file.filename
            # Move the file form the temporal folder to the upload
            # folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #Buat kelas teks dan masukkan pada files
            files.append(Text("uploads/"+filename))
  
    string = ""
    for text in files:
        s = text.match(tek,int(option))
        if(s!=None):
            string += '<p>Jumlah: ' +cetakInt(s)+ '  Waktu: '+ findAllTime(s) +'<br>Kalimat:<br>' + s +'<br>Nama File: '+ text.filename +'</p>'
    return '<h2>Result!</h2>' + string 


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )
