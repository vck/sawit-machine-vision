import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash)

DEV_MACHINE = 'X86_64'
PROD_MACHINE = 'armv7l'
PROD_MODE = False


if os.uname()[-1] == PROD_MACHINE:
    from PIL import Image
    from picamera import PiCamera
    PROD_MODE = True


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def capture_image():
    if PROD_MODE == True:
        if request.method == "POST":
            camera.capture("static/test.jpg")
            im = Image.open("static/test.jpg")
            rgb_im = im.convert('RGB')
            r,g,b = rgb_im.getpixel((1, 1))
            return render_template("index.html", data=(r, g, b, "test.jpg"))
        else:
            return render_template("prod.html")
    else:
        return render_template("dev.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
