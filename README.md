

````markdown
# 🧠 Text-to-Text Generator with Cohere
A simple Streamlit web app that uses the Cohere API to perform Text-to-Text tasks like **Summarization**, **Paraphrasing**, and **Custom Prompt** completions.

---

## 🌟 Features
- ✍️ Summarize any given text  
- 🔁 Paraphrase text clearly  
- 💡 Input custom prompts  
- ⚡ Fast and simple UI via Streamlit  

---

## 📸 Preview
![screenshot](https://placehold.co/800x400?text=App+Screenshot)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- A [Cohere API Key](https://dashboard.cohere.com/api-keys)

---

### 🔧 Installation

1. **Clone this repository**
```bash
git clone https://github.com/your-username/text-to-text-cohere.git
cd text-to-text-cohere
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your API Key**
   Open `app.py` and replace the placeholder with your actual API key:

```python
COHERE_API_KEY = "your-api-key-here"
```

⚠️ *Do NOT commit your real API key to a public repository.*

4. **Run the app**

```bash
streamlit run app.py
```

---

## 🗂 Project Structure

```
text-to-text-cohere/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📦 Requirements

Put this into your `requirements.txt` file:

```
streamlit==1.35.0
cohere==4.40
```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE)

---

## 🙏 Acknowledgements

* [Cohere](https://cohere.com/) for their NLP API
* [Streamlit](https://streamlit.io/) for the front-end framework

