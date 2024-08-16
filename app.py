from flask import Flask, request, render_template, redirect, url_for, session
import os
from ai_module import process_pdf, generate_question_from_text, evaluate_answer, check_model_availability

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'your_secret_key'  # Gantilah dengan kunci rahasia yang kuat

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename and file.filename.endswith('.pdf'):
                # Simpan file PDF
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                
                # Proses PDF
                text = process_pdf(file_path)
                os.remove(file_path)  # Hapus file setelah pemrosesan
                
                # Hasilkan pertanyaan pertama
                question = generate_question_from_text(text)
                
                # Simpan teks dan pertanyaan dalam sesi
                session['text'] = text[:1000]  # Simpan potongan kecil dari teks
                session['question'] = question
                
                return render_template('question.html', question=question)
    
    return render_template('index.html')

@app.route('/check_model', methods=['POST'])
def check_model():
    model_name = request.form.get('model_name', 'llama3')
    model_status = check_model_availability(model_name)
    return render_template('index.html', model_status=model_status)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    answer = request.form['answer']
    question = request.form['question']
    
    # Evaluasi jawaban
    feedback = evaluate_answer(question, answer)
    
    # Simpan umpan balik dalam sesi
    session['feedback'] = feedback
    
    # Hasilkan pertanyaan berikutnya
    text = session.get('text')
    if text:
        question = generate_question_from_text(text)
        session['question'] = question
        return render_template('feedback.html', feedback=feedback, question=question)
    
    # Jika tidak ada teks dalam sesi, kembali ke halaman unggah
    return redirect(url_for('index'))

@app.route('/next_question', methods=['POST'])
def next_question():
    question = request.form['question']
    
    # Simpan pertanyaan dalam sesi
    session['question'] = question
    
    return render_template('question.html', question=question)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
