import streamlit as st 
import os
import nltk
nltk.download('punkt')

# NLP Pkgs
from textblob import TextBlob 
from textblob.classifiers import NaiveBayesClassifier

with open('normsdata.json', 'r') as fp:
     cl = NaiveBayesClassifier(fp, format="json")


def main():
	""" NLP Based App with Streamlit """

	# Title
	st.title("Norms Classifier")
	st.subheader("Natural Language Processing On the Go.")

	message = st.text_area("Enter text and classify it as descriptive vs. injunctive norms",
    "Type Here ..")
    
	if st.button("Analyze"):
			nlp_result = cl.classify(message)
			st.success(nlp_result)


	st.sidebar.subheader("Norms Classifier 0.1")
	st.sidebar.text("Textblob App with Streamlit")
	

	st.sidebar.subheader("By")
	st.sidebar.text("Shelby Wilcox and Ralf Schmaelzle")
	st.sidebar.text("[names]@msu.edu")
	

if __name__ == '__main__':
	main()