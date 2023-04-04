from datetime import datetime
import time
import pathlib
import sys
import base64
import json
import os
import numpy as np
import requests
import cv2

#reference_picture = cv2.imread(picture_path)
picture_path = 'images/image1.jpg'
reference_picture = cv2.imread(picture_path)

#fps = 60  # FPS deseado
#cap.set(cv2.CAP_PROP_FPS, fps)  # configurar los FPS
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)


def inference_container(img):
    result_container = container_predict(img, 'image_key', port_number=8501)

    #result_container_2 = result_container['predictions'][0]['scores']
    #result_container_2 = np.expand_dims(result_container_2,axis=0)
    #result_container_2 = np.expand_dims(result_container_2,axis=0)
    #print('Result', '= ',result_container)

    return result_container

def preprocess_image(image_file_path, max_width, max_height):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 85]
    im = image_file_path
    [height, width, _] = im.shape
    if height > max_height or width > max_width:
        ratio = max(height / float(max_width), width / float(max_height))
        new_height = int(height / ratio + 0.5)
        new_width = int(width / ratio + 0.5)
        resized_im = cv2.resize(
            im, (new_width, new_height), interpolation=cv2.INTER_AREA)
        _, processed_image = cv2.imencode('.jpg', resized_im, encode_param)
    else:
        _, processed_image = cv2.imencode('.jpg', im, encode_param)
    return base64.b64encode(processed_image).decode('utf-8')

def container_predict(image_file_path, image_key, port_number=8501):
    #print('container_predict_file: ',image_file_path)
    encoded_image = preprocess_image(
        image_file_path=image_file_path, max_width=1920, max_height=1080)
    instances = {
            'instances': [
                    {'image_bytes': {'b64': str(encoded_image)},
                     'key': image_key}
            ]
    }
    url = 'http://localhost:{}/v1/models/default:predict'.format(port_number)
    #print(url)
    response = requests.post(url, data=json.dumps(instances))
    return response.json()

if __name__ == '__main__':
    print('Starting')
    while(True):

        results = inference_container(reference_picture)
        #print(results)
       
        boxes = results['predictions'][0]['detection_boxes']
        classes = results['predictions'][0]['detection_classes']
        scores = results['predictions'][0]['detection_scores']
        label_names = results['predictions'][0]['label_names']
        
        
        
        
        
         
        
