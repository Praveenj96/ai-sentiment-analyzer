import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')

st.title("AI Sentiment Analyzer")

text = st.text_area("Enter text")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            st.success("Positive 😊")
        elif polarity < 0:
            st.error("Negative 😠")
        else:
            st.info("Neutral 😐")
            
        st.write("Score:", polarity)

