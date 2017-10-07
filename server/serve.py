import os

from time import strftime

from flask import (
    Flask,
    render_template,
    request)

from PIL import Image
from time import strftime

DEV_MACHINE = 'X86_64'
PROD_MACHINE = 'armv7l'
PROD_MODE = False
DEBUG = True

if os.uname()[-1] == PROD_MACHINE:
    from PIL import Image
    from picamera import PiCamera
    camera = PiCamera(sensor_mode=5)
    PROD_MODE = True
    DEBUG = False


app = Flask(__name__)


def generate_filename():
    timestamps = strftime("%m%d%Y-%H%M%S")
    return timestamps + '.jpg'

@app.route("/", methods=["GET", "POST"])
def capture_image():

    # PRODUCTION ENVIRONMENT
    if PROD_MODE == True:
        if request.method == "POST":
            filename = generate_filename()
            camera.resolution = (1280, 720)
            camera.crop =  (0.25, 0.4, 1, 2)
            camera.capture("static/"+filename)
            im = Image.open("static/"+filename)
            rgb_im = im.convert('RGB')
            R,G,B = rgb_im.getpixel((1, 1))
            grey_value = (0.3 * R, 0.59 * G, 0.11 * B)
            return render_template('prod.html', rgb=(R, G, B), grey_value=grey_value, filename=filename)

        return render_template("prod.html")


    # DEVELOPMENT ENVIRONMENT
    if request.method == "POST":
        R, G, B = 12, 34, 56
        grey_value = (0.3 * R, 0.59 * G, 0.11 * B)
        return render_template('dev.html', rgb=(R, G, B), grey_value=grey_value)

    return render_template("dev.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=DEBUG)
