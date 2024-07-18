from flask import Flask,request,jsonify
import base64
from PIL import Image
from io import BytesIO
from predict import predict_butterfly
app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    if 'image' in data:
        base64_image = data['image']
        image_bytes = base64.b64decode(base64_image)
        image = Image.open(BytesIO(image_bytes))
        temp_image_path = 'requests/image.jpg'
        image.save(temp_image_path)
        confidence,label = predict_butterfly(temp_image_path)
        response_data = {
            'message':"Image Recieved",
            'confidence':confidence,
            'label':label
        }
        return jsonify(response_data),200
    
    else:
        return jsonify({'error':"No Image data found in request"}),400
    



if __name__ == '__main__':
    app.run(debug=True)