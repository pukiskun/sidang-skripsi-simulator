import subprocess
import tempfile
import os
from PyPDF2 import PdfReader

def process_pdf(pdf_path):
    # Ekstrak teks dari PDF
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ''
    return text

def check_model_availability(model_name="llama3"):
    # Periksa apakah model sudah ada dengan perintah `ollama list`
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True, encoding='utf-8')
    if model_name in result.stdout:
        return f"Model '{model_name}' sudah ada."
    else:
        return f"Model '{model_name}' tidak ditemukan. Silakan jalankan perintah berikut di terminal untuk mengunduh dan menginisiasi model: ollama run {model_name}"

def run_ollama_command(prompt, model_name="llama3"):
    # Pastikan model sudah diunduh sebelum menjalankan perintah
    command = ["ollama", "run", model_name]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    
    try:
        # Kirim prompt ke stdin dari proses
        stdout, stderr = process.communicate(input=prompt)
        
        if process.returncode == 0:
            return stdout.strip()
        else:
            return f"Error: {stderr}"
    except Exception as e:
        return f"Exception: {str(e)}"

def generate_question_from_text(text):
    prompt = f"Generate a question about the following text: {text}"
    response = run_ollama_command(prompt)
    return response

def evaluate_answer(question, answer):
    prompt = f"Here is the question: {question}\nHere is the student's answer: {answer}\nProvide feedback."
    response = run_ollama_command(prompt)
    return response
