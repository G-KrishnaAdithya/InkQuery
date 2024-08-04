from flask import Flask, request, jsonify, render_template
from funs import extract_text_from_image, call_gemini_api
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    print("Received request")
    if 'file' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['file']
    image_stream = BytesIO(image_file.read())
    predicted_text = extract_text_from_image(image_stream)
    gemini_response = call_gemini_api(predicted_text)
    return jsonify({
        'ocr_output': predicted_text,
        'genai_response': gemini_response
    })

if __name__ == '__main__':
    app.run(debug=True)
