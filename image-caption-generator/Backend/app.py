from flask import Flask, render_template, request, jsonify
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io
import requests

app = Flask(__name__)

def initialize_model():
    hf_model = "Salesforce/blip-image-captioning-large"
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    processor = BlipProcessor.from_pretrained(hf_model)
    model = BlipForConditionalGeneration.from_pretrained(hf_model).to(device)
    return processor, model, device

processor, model, device = initialize_model()

def generate_caption(image):
    image = Image.open(io.BytesIO(image))
    inputs = processor(image, return_tensors='pt').to(device)
    out = model.generate(**inputs, max_new_tokens=20)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def generate_caption_from_url(image_url):
    image = Image.open(io.BytesIO(requests.get(image_url).content))
    inputs = processor(image, return_tensors='pt').to(device)
    out = model.generate(**inputs, max_new_tokens=20)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image'].read()
        caption = generate_caption(image)
        return jsonify({'caption': caption})
    elif 'image_url' in request.form:
        image_url = request.form['image_url']
        caption = generate_caption_from_url(image_url)
        return jsonify({'caption': caption})
    else:
        return jsonify({'error': 'No image uploaded or URL provided'})

if __name__ == '__main__':
    app.run(debug=True)