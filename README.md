\# AI Text Summarizer



An AI-powered text summarization application built using Python, Streamlit, and Google's Gemini API. It converts lengthy text into concise, easy-to-understand summaries.



\## Features



\- Summarizes long text using Google Gemini AI.

\- Three summary lengths: Short, Medium, and Detailed.

\- Simple and interactive Streamlit interface.

\- Input validation and error handling.

\- Secure API key management using environment variables.



\## Technologies Used



\- Python

\- Streamlit

\- Google Gemini API

\- Google Gen AI SDK

\- python-dotenv



\## Project Structure



```text

ai-text-summarizer/

│

├── app.py

├── requirements.txt

├── .gitignore

├── .env

└── README.md

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/Chiranjeevi-bonala/ai-text-summarizer.git

cd ai-text-summarizer

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment (Windows)



```bash

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 5. Configure your Gemini API key



Create a `.env` file in the project directory and add:



```env

GEMINI\_API\_KEY=your\_gemini\_api\_key\_here

```



Replace the placeholder with your own API key. Never share or upload your API key.



\### 6. Run the application



```bash

python -m streamlit run app.py

```



The application will open in your browser.



\## Future Enhancements



\- Multilingual text summarization.

\- PDF and DOCX file summarization.

\- Download summaries.

\- Improved user interface.



\## Author



\*\*Chiranjeevi Bonala\*\*



\- GitHub: \[Chiranjeevi-bonala](https://github.com/Chiranjeevi-bonala)

\- LinkedIn: \[Chiranjeevi Bonala](https://www.linkedin.com/in/chiranjeevibonala/)

