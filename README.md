Project Title: Document Understanding and Chatbot Interface
Description:
This project aims to develop a web-based application that allows users to upload documents (PDFs or images) and interact with an AI-powered chatbot to understand the content. The application utilizes OCR (Optical Character Recognition) to extract text from the uploaded documents and then summarizes and answers questions about the content using a chatbot model.

Key Features:
Document Upload: Users can upload PDF or image files through the web interface.
OCR Processing: The application supports two types of OCR processing - Easy OCR and Surya OCR, to convert document content into a JSON format.
Content Summarization: The extracted content is summarized by the AI model, providing a concise overview.
Chat Interface: Users can interact with the chatbot to ask questions about the document content.
Flask Backend: The backend is built using Flask, handling file uploads, OCR processing, and chatbot interactions.
Customizable Models: Users can choose different AI models for summarization and question answering.
Technology Stack:
Backend: Flask
Frontend: HTML, CSS, JavaScript
OCR: Easy OCR, Surya OCR
AI Models: Custom models for summarization and question answering
Storage: Local storage for uploaded files and OCR results
Installation:
Clone the repository:
bash
Kodu kopyala
git clone https://github.com/yourusername/yourrepository.git
Install the required packages:
bash
Kodu kopyala
pip install -r requirements.txt
Run the application:
bash
Kodu kopyala
flask run
Usage:
Navigate to the home page.
Upload a document (PDF or image).
Choose the document type and OCR type.
View the summarized content and interact with the chatbot to ask questions about the document.
Future Enhancements:
Add support for more document types and OCR engines.
Improve the AI models for better summarization and question answering.
Implement user authentication and document history tracking.