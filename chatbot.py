import requests
import json
import ocr.easy_ocr as easy_ocr
import ocr.surya_ocr as surya_ocr
import pandas as pd
def send_request(messages,model):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": messages,
        "stream":False,
        "eval_count":1,
        "options": {"num_ctx": 10000}

    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response = response.json()["message"]["content"]
    return(response)

data=[]
messages = []

# pdf->jpeg->json
def pdf_to_json(pdf_path,ocr_type,file_name):
    global data
    
    if (ocr_type=="easy"):
        #if easy ocr
        easy_ocr.pdf_to_jpg(pdf_path)
        easy_ocr.jpg_to_json(easy_ocr.pdf_size)
        with open('ocr_output.json', 'r') as f:
            data = json.load(f)
            print(data)
    else:
        print(file_name)
        surya_ocr.surya_to_json(pdf_path,file_name)
        with open('ocr_output.json', 'r') as f:
            data = json.load(f)
            print(data)


#single page jpg->json
def jpg_to_json(jpg_path,ocr_type,file_name):
    if(ocr_type=="easy"):
        global data
        easy_ocr.jpg_to_json(1)
        with open('ocr_output.json', 'r') as f:
            data = json.load(f)
            print(data)
    else:
        print(file_name)
        surya_ocr.surya_to_json(jpg_path,"page0")
        with open('ocr_output.json', 'r') as f:
            data = json.load(f)
            print(data)
    

#Data as a json format
def summarize_json(data,model):
    messages = [{"role": "user", "content":f"Türkçe bir chatbotsun,sana json formatında atılan belgenin türünü ve bütün bilgileri anlamanı ve soruları cevaplamanı istiyorum {data}"}]
    answer = send_request(messages,model)
    answer_for_array = {"role": "assistant","content": answer}
    messages.append(answer_for_array)
    return(messages,answer)


#User - trained AI side
def ask_question(request,model):
    
    answer = send_request(request,model)
   
    return answer


