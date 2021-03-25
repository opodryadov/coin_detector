import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from detector import CoinDetector

secret_key = os.urandom(12).hex()
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = secret_key


def coin_detector(input_image):
    detector = CoinDetector(input_image)
    detector.find_contours()
    return detector


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
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')


@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    image = coin_detector(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template(
        'result.html',
        img=filename,
        size=" x ".join(map(str, image.size)),
        average_color=image.average_color,
        total_coins=image.total_coins,
        total_amount=image.total_amount
    )


if __name__ == "__main__":
    app.run(debug=True)
