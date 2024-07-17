import requests
import json
import ocr
import pandas as pd
import easyocr
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
def pdf_to_json(pdf_path):
    global data
    ocr.pdf_to_jpg(pdf_path)
    ocr.jpg_to_json(ocr.pdf_size)
    with open('ocr_output.json', 'r') as f:
        data = json.load(f)


#Data as a json format
def summarize_json(data,model):
    #messages = [{"role": "user", "content": f"You are a chatbot that understands information related to an e-invoice delivery note. Below is a structure of an e-invoice delivery note in JSON format. By analyzing this structure, you should understand what each component means and provide accurate information to the user. You should extract details. JSON: {data}, Analyze this e-invoice delivery note in JSON format and provide detailed explanations of each component to assist the user."}]
    messages = [{"role": "user", "content":f"Türkçe bir chatbotsun,sana json formatında atılan belgenin türünü ve bütün bilgileri anlamanı ve soruları cevaplamanı istiyorum {data}"}]
    answer = send_request(messages,model)
    answer_for_array = {"role": "assistant","content": answer}
    messages.append(answer_for_array)
    return(messages,answer)


#User - trained AI side
def ask_question(request,model):
    
    answer = send_request(request,model)
   
    return answer


