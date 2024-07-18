import numpy
import easyocr
import json
from pdf2image import convert_from_path
import os


dataset = []

pdf_size = 1

def pdf_to_jpg(pdf_path):
    global pdf_size
    images = convert_from_path(f'{pdf_path}')
    
    for i in range(len(images)):
        images[i].save('output_images/page'+ str(i) +'.jpg', 'JPEG')

    pdf_size= len(images)

def get_ocr_result(image_path):
    reader = easyocr.Reader(['tr'])
    result = reader.readtext(image_path)
    for (bbox, text, prob) in result:
        if prob > 0.4:
            x1,y1 = bbox[0]
            x2,y2 = bbox[2]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            data = {
                "x1": x1, 
                "y1":y1,
                "x2":x2,
                "y2":y2, 
                "text": text
            }
            dataset.append(data)

def jpg_to_json(pdf_size):
    for i in range(pdf_size):
        img_path = f"output_images/page{i}.jpg"
        get_ocr_result(img_path)
        os.remove(img_path)


    json_data = json.dumps(dataset, ensure_ascii=False)
    with open('ocr_output.json', 'w') as f:
        f.write(json_data)




