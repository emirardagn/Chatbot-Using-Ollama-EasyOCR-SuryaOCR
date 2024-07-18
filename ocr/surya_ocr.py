import subprocess
import json
import os

def surya_to_json(pdf_path,file_name):
    file_name = file_name.split(".")[0]
    print(file_name)
    command = ["surya_ocr",pdf_path, "--images", "--langs", "tr"]
    subprocess.run(command)


    with open(f'results/surya/{file_name}/results.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_data = {file_name: []}

    for item in data[file_name]:
        new_text_lines = []
        for line in item['text_lines']:
            new_text_lines.append({
                'bbox': line['bbox'],
                'text': line['text']
            })
        new_data[file_name].append(new_text_lines)
    with open('ocr_output.json', 'w', encoding='utf-8') as file:
        json.dump(new_data[file_name][0], file, ensure_ascii=False)
    

    
    os.remove(f"results/surya/{file_name}/results")