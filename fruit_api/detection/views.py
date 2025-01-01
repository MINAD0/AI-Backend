import tensorflow as tf
import numpy as np
from PIL import Image
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import os

# Load TFLite Model
model_path = os.path.join(settings.BASE_DIR, 'detection/models/CNN_fruits.tflite')
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensor details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

@api_view(['POST'])
def predict_fruit(request):
    try:
        # Check if a file is uploaded
        if 'file' not in request.FILES:
            return Response({'error': 'No file uploaded'}, status=400)
        
        image = request.FILES['file']
        img = Image.open(image).convert('RGB')
        
        # Resize the image to match model input shape
        target_size = tuple(input_details[0]['shape'][1:3])  # e.g., (32, 32)
        img = img.resize(target_size)
        
        # Preprocess image
        img = np.array(img, dtype=np.float32) / 255.0  # Normalize if required
        img = np.expand_dims(img, axis=0)  # Add batch dimension

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], img)
        interpreter.invoke()
        
        # Get predictions
        output = interpreter.get_tensor(output_details[0]['index'])
        
        # Mock label names
        labels = ['apple', 'banana', 'kiwi', 'lemon', 'orange', 'watermelon']
        predicted_label = labels[np.argmax(output[0])]
        confidence = float(np.max(output[0]))

        return Response({
            'fruit': predicted_label,
            'confidence': confidence
        })
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)
