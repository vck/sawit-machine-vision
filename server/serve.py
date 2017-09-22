import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image
from picamera import PiCamera

camera = PiCamera()

UPLOAD_FOLDER = '/home/vickydasta/git/sawit-machine-vision/uploads/'
ALLOWED_EXTENSIONS = set(['doc', 'pptx', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            im = Image.open(UPLOAD_FOLDER+filename)
            rgb_im = im.convert("RGB")
            r, g, b = rgb_im.getpixel((1, 1))

            return """
            <h1>red value: {}</h1>
            <h1>green value: {}</h1>
            <h1>blue value: {}</h1>
            """.format(r, g, b)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

from flask import send_from_directory



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route("/capture", methods=["GET", "POST"])
def capture_image():
   if request.method == "GET":
      return """

      <form method="POST" action="/capture">
         <input type="submit" name="capture">
      </form>
      """
   
   camera.capture("static/test.jpg")
   
   im = Image.open("static/test.jpg")
   rgb_im = im.convert('RGB')
   r,g,b = rgb_im.getpixel((1, 1))
   return render_template("index.html", data=(r, g, b, "test.jpg"))

   
app.run('0.0.0.0', port=8000)

