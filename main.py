import numpy as np
import gradio as gr
from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import load_img
# from tensorflow.keras.preprocessing.image import img_to_array

def predict_image(image):
    model = load_model("final_model.h5")
    img = image.reshape(-1,28,28,1)
    img = img/255.0
    predict_value = model.predict(img)
    digit = np.argmax(predict_value)
    digit = int(digit)
    return digit


iface = gr.Interface(predict_image, inputs="sketchpad",outputs="label")
iface.launch(debug=True,share=True)