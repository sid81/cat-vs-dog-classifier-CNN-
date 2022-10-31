
import sys
import os
import glob
import re
import numpy as np

from tensorflow.keras.preprocessing.image import img_to_array,load_img
from tensorflow.keras.models import load_model
# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='Model_vgg19_malariah5.h5'

# Load your trained model
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    img = load_img(img_path, target_size=(224, 224))
    
    img = img_to_array(img)
    img=img/255
    img = img.reshape(1, 224, 224, 3)
    result = model.predict(img)
    result = result.flatten()
    result = round(result[0])
    if result==0:
        result="parasite"
    else:
        result="uninfected"
    
    return result

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
