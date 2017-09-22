import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash)

from PIL import Image

DEV_MACHINE = 'X86_64'
PROD_MACHINE = 'armv7l'
PROD_MODE = False
DEBUG = True

if os.uname()[-1] == PROD_MACHINE:
    from PIL import Image
    from picamera import PiCamera
    camera = PiCamera()
    PROD_MODE = True
    DEBUG=False


app = Flask(__name__)


app.config["UPLOAD_FOLDER"] = '/home/vickydasta/Pictures'

@app.route("/", methods=["GET", "POST"])
def capture_image():

    # PRODUCTION ENVIRONMENT
    if PROD_MODE == True:
        if request.method == "POST":
            camera.capture("static/test.jpg")
            im = Image.open("static/test.jpg")
            rgb_im = im.convert('RGB')
            R,G,B = rgb_im.getpixel((1, 1))
            grey_value = (0.3 * R, 0.59 * G, 0.11 * B)
            return render_template('prod.html', rgb=(R,G,B), grey_value=grey_value)

        return render_template("prod.html")


    # DEVELOPMENT ENVIRONMENT
    if request.method == "POST":
        R, G, B = 12, 34, 56
        grey_value = (0.3 * R, 0.59 * G, 0.11 * B)
        return render_template('dev.html', rgb=(R,G,B), grey_value=grey_value)

    return render_template("dev.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=DEBUG)
