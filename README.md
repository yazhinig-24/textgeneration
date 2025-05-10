🧠 Text-to-Text Generator with Cohere
A simple Streamlit web application that leverages the Cohere API to perform text generation tasks like summarization, paraphrasing, and custom prompt completions.

🌟 Features
✍️ Summarize any given text

🔁 Paraphrase content intelligently

💡 Input your own custom prompts

⚡ Fast and interactive UI using Streamlit

📸 Preview

🚀 Getting Started
Prerequisites
Python 3.7+

A Cohere API Key (Get it here)

Installation
Clone the Repository

git clone https://github.com/your-username/text-to-text-cohere.git
cd text-to-text-cohere

Install Dependencies

pip install -r requirements.txt
Add Your API Key

Open app.py and replace the placeholder:

python
COHERE_API_KEY = "your-api-key-here"
⚠️ Do NOT commit your actual API key to public repositories.

Run the App
streamlit run app.py
🗂 Project Structure


text-to-text-cohere/
├── app.py                    # Streamlit application code
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation


📦 Requirements
Your requirements.txt file should contain:
streamlit==1.35.0
cohere==4.40


📝 License
This project is licensed under the MIT License.

🙏 Acknowledgements
Cohere for their powerful language generation models

Streamlit for enabling quick UI development for ML apps

