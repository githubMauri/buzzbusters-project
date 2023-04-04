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
#import globals_v

#reference_picture = cv2.imread(picture_path)
#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture('video/mosquitoes.mp4')
fps = 60  # FPS deseado
cap.set(cv2.CAP_PROP_FPS, fps)  # configurar los FPS
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)


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
        ret, img = cap.read()

        reference_picture = img
        
        results = inference_container(reference_picture)
        #print(results)
       
        boxes = results['predictions'][0]['detection_boxes']
        classes = results['predictions'][0]['detection_classes']
        scores = results['predictions'][0]['detection_scores']
        label_name = results['predictions'][0]['detection_classes_as_text']


        #print(len(boxes))

        for (box,classx,scorex,labelx) in zip(boxes,classes,scores,label_name):
            xmin = int(box[0]*reference_picture.shape[0])
            ymin = int(box[1]*reference_picture.shape[1])
            xmax = int(box[2]*reference_picture.shape[0])
            ymax = int(box[3]*reference_picture.shape[1])
            label_object_det = labelx + '_' f"{scorex:.3f}"
            if classx == 3:
                color = (255, 0, 0)
            elif classx == 2:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
            # if scorex < 0.02:
            #     color = (255, 255, 255)
            # reference_picture = cv2.rectangle(reference_picture, (ymin, xmin), (ymax, xmax), color, 2)
            if scorex > 0.7:
                reference_picture = cv2.putText(reference_picture, label_object_det, (ymin-2, xmin-2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)                
                reference_picture = cv2.rectangle(reference_picture, (ymin, xmin), (ymax, xmax), color, 2)
        #print()
        #reference_picture = cv2.rectangle(reference_picture, (5, 5), (220, 220), (255, 0, 0), 2)
        scale_percent = 200 # percent of original size
        width = int(reference_picture.shape[1] * scale_percent / 100)
        height = int(reference_picture.shape[0] * scale_percent / 100)
        dim = (width, height)
        resize_picture = cv2.resize(reference_picture, dim, interpolation = cv2.INTER_AREA)

        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.imshow('Image', resize_picture)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    