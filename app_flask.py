from flask import Flask, request, redirect, url_for, render_template, jsonify
import os
import chatbot

messages=[]
model =""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=["GET", "POST"])
def upload():
    global messages
    global model
    model = request.form["model"]
    doc_type = request.form["doc_type"]
    ocr_type = request.form["ocr_type"]
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            
            if(doc_type=="pdf"):     
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                chatbot.pdf_to_json(file_path,ocr_type,file.filename)
                messages,ai_summarize = chatbot.summarize_json(chatbot.data,model)
            else:
                file_path = os.path.join("output_images", "page0.jpg")
                file.save(file_path)
                chatbot.jpg_to_json(file_path,ocr_type,file.filename)
                messages,ai_summarize = chatbot.summarize_json(chatbot.data,model)

            return redirect(url_for('chat', ai_summarize=ai_summarize, model_name = model))
    return render_template('upload.html')

@app.route('/chat', methods=["GET", "POST"])
def chat():
    ai_summarize = request.args.get('ai_summarize', '')
    return render_template('chat.html', ai_summarize=ai_summarize)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    req_json = {"role": "user", "content": user_message}
    messages.append(req_json)
    ai_response = chatbot.ask_question(messages,model)
    messages.pop()
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
