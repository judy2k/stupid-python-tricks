import numpy as np

import lasagne
import theano
from theano import tensor as T

import joblib

import cv2

from evil_neural_networks import dnn_architecture


DNN_MODEL_PATH = 'dnn_model/dnn'


EMOTIONS = [
    'Angry-ish',
    'Disgust-ish',
    'Fear-ish',
    'Happy-ish',
    'Sad-ish',
    'Surprise-ish',
    'Neutral-ish'
]

EMOTION_TO_INDEX = {emotion: i for i, emotion in enumerate(EMOTIONS)}


_theano_predict_fn = None
_face_cascade = None

def _get_predict_fn():
    global _theano_predict_fn

    if _theano_predict_fn is None:
        dnn_model = joblib.load(DNN_MODEL_PATH)
        param_values = dnn_model['param_values']

        # For classification use batch size of 1 so it can run on CPU
        l_out, l_in = dnn_architecture.build_model((1,48,48), 7, 1)

        lasagne.layers.set_all_param_values(l_out, param_values)

        X_batch = T.tensor4('x')
        out_eval = lasagne.layers.get_output(l_out, X_batch, deterministic=True)
        _theano_predict_fn = theano.function([X_batch], [out_eval])

    return _theano_predict_fn




def predict_face_greyscale_48(face_48):
    X = face_48.reshape((1, 1, 48, 48))

    X = (X - X.mean()) / X.std()

    pred_fn = _get_predict_fn()

    Y_pred = pred_fn(X)
    return Y_pred[0][0]


def detect_and_predict_face(frame):
    global _face_cascade

    if _face_cascade is None:
        _face_cascade = cv2.CascadeClassifier('face_detector/haarcascade_frontalface_alt.xml')

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = _face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    if len(faces) > 0:
        x,y,w,h = faces[0]

        sz = max(w, h)
        extra_w = (sz - w)/2
        extra_h = (sz - h)/2

        x = max(x - extra_w, 0)
        y = max(y - extra_h, 0)

        face_grey = grey[y:y+sz, x:x+sz]

        face_48 = cv2.resize(face_grey, (48, 48))

        return predict_face_greyscale_48(face_48), faces
    else:
        return None, None



def detect_and_predict_face_emotion(frame):
    # Get probability vector from detect_and_predict_face
    prob, faces = detect_and_predict_face(frame)
    if prob is not None:
        return np.argmax(prob)
    else:
        return None

