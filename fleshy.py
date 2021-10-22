from flask import Flask
from flask import render_template
from flask import request
import base64, numpy, os
from skimage import data, io, filters
 
UPLOAD_FOLDER = '/pics'

# creates a Flask application, named app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('demo.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    image_b64 = request.form['demo'].split(',')[1]
    image_data = base64.b64decode(image_b64)
    with open("test.png", "wb") as fo:
       fo.write(image_data)

    imageprocess()

    return render_template('result.html')


def imageprocess(name='test.png'):
    #filename = os.path.join(skimage.data_dir, name)
    monster = io.imread(name)
    edges = filters.sobel(monster)
    io.imsave('static/monster.png', edges)


# run the application
if __name__ == "__main__":
    app.run(debug=True)