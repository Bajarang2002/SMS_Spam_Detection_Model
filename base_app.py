import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import flask
print(flask.__version__)

# ps = PorterStemmer()


# model = pickle.load(open("model.pkl","rb"))
# tfidf = pickle.load(open("vectorizer.pkl","rb"))

# st.title(" EMAIL SMS Spam Detection")
# # st.subtitle("Model Used to find out  sms or email is spam or not spam")

# def transform_text(text):
#     text= text.lower()
#     text = word_tokenize(text)
    
#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)
         
            
    
#     text = y[:]
#     y.clear()
  
    
#     for i in text:
#         if i  not in stopwords.words('english') and i  not in string.punctuation:
#             y.append(i)
   
    
#     text = y[:]
   
    
#     for i in text:
#         y.append(ps.stem(i))
        
#     return " ".join(y)
   


# text_input = st.text_area("Enter the message")



# if st.button("Predict"):

#     # 1. preprocess
#     preprocessed_sms = transform_text(text_input)

#     # 2. vectoriztion
#     vector_input = tfidf.transform([preprocessed_sms])
#     # 3. Display

#     result = model.predict(vector_input)

#     if result==1:
#         print(st.header(" Spam"))
#     else:
#         print(st.header("Not Spam"))

#     # 4. Deploy

    






