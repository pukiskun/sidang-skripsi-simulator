# Thesis Defense Simulation Application (beta)
## (Sidang Skripsi Simulator)
---
This application simulates a thesis defense scenario where a user can upload their thesis in PDF format, and an AI model generates questions related to their thesis. The user can then answer these questions, receive feedback, and proceed with further questions based on their responses.

## Features
1. Upload a PDF file of the thesis.
2. Process the PDF to extract text.
3. Generate questions about the thesis content.
4. Provide answers to questions and receive feedback.
5. Get new questions based on the provided answers.

## Prerequisites
1. Python 3.8 or higher
2. Flask
3. PyPDF2
4. Ollama CLI

## Installation

1. Clone the Repository
   ```bash
   git clone https://github.com/your-username/sidang-skripsi-simulator.git
   ```
3. Navigate to Directory
   ```bash
   cd sidang-skripsi-simulator
   ```
5. Install Required Packages
   ```bash
   pip install -r requirements.txt
   ```
7. Install Ollama from https://ollama.com/
8. Ensure you have the 'llama3' model avaliable. Youcan download and initialize it with:
   ```bash
   ollama run llama3
   ```
10. Start the Flask Server
    ```
    bash python app.py
    ```

## Usage
1. Upload Thesis
->On the main page, upload a PDF file of your thesis.
2. Answer Questions
->After uploading, the AI will generate questions based on your thesis. Answer these questions and submit your responses.
3. Receive Feedback
->You will receive feedback on your answers and be prompted with new questions if needed.
4. Continue Interaction
->You can continue answering questions and receiving feedback as needed.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. this project still lacking so much both from UI and functionality.
