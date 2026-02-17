# 📩 Email / SMS Spam Detection System

A Machine Learning based Spam Detection Web Application built using **Streamlit**, **Scikit-learn**, and **NLTK**.

This app classifies Email or SMS messages as:

- ✅ Not Spam  
- 🚫 Spam  

---

## 🚀 Live Demo

https://sms-spam-detection-model-2.onrender.com/

---

## 📌 Features

- Professional Streamlit UI
- TF-IDF Vectorization
- Porter Stemming
- Stopword Removal
- Real-time Message Classification
- Cached Model Loading
- Deployment Ready

---

## 🧠 Machine Learning Model

The model was trained using:

- Scikit-learn
- TF-IDF Vectorizer
- NLP Preprocessing (Tokenization, Stopword Removal, Stemming)
- Classification Algorithm (Multinomial Naive Bayes / Logistic Regression)

Training Notebook:
```
Spam_Detection_Model.ipynb
```

Saved Files:
```
model.pkl
vectorizer.pkl
```

---

## 📂 Project Structure

```
spam-detection/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── Spam_Detection_Model.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Bajarang2002/spam-detection.git
cd spam-detection
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt not available:

```bash
pip install streamlit scikit-learn nltk
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🌍 Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Visit https://share.streamlit.io
3. Connect your GitHub repository
4. Select `app.py`
5. Deploy 🚀

---

## 📦 requirements.txt

Create a file named `requirements.txt` and add:

```
nltk==  3.9.2
streamlit
scikit-learn
numpy== 1.26.4
pandas == 2.2.3

```

---

## 🔍 Text Preprocessing Pipeline

The app performs:

1. Lowercasing
2. Tokenization using NLTK
3. Stopword Removal
4. Alphanumeric Filtering
5. Porter Stemming
6. TF-IDF Vectorization
7. Model Prediction

---

## 🛠️ Deployment Issue Fix

If deployed app predicts only **"Not Spam"**, check:

- ✔ Same `model.pkl` used
- ✔ Same `vectorizer.pkl` used
- ✔ Same sklearn version
- ✔ Same preprocessing logic
- ✔ Files properly uploaded to repository

---

## 🧪 Example Messages

### Spam Example
```
Congratulations! You've won a free gift card. Click here now.
```

### Not Spam Example
```
Hi, are we still meeting tomorrow at 6 PM?
```

---

## 👨‍💻 Author

https://github.com/Bajarang2002




⭐ If you found this project helpful, please give it a star on GitHub!
