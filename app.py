import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

st.set_page_config(
    page_title="RAG Course Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 RAG Course Assistant")
st.write("Ask questions about your course content.")

df = joblib.load("embedding.joblib")

embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.6-flash")

query = st.text_input("Ask a question about the course")

def create_embedding(text_list):
    return embedding_model.encode(
        text_list,
        normalize_embeddings=True
    )

def inference(prompt):
    response = model.generate_content(prompt)
    return response.text

if st.button("Ask"):

    question_embedding = create_embedding([query])[0]

    similarities = cosine_similarity(
        np.vstack(df["embedding"]),
        [question_embedding]
    ).flatten()

    top_result = 7
    max_indx = similarities.argsort()[::-1][:top_result]

    new_df = df.iloc[max_indx]

    prompt = f"""
You are an assistant for a Web Development course that contains 10 videos.

Below are relevant video chunks from the course:
{new_df[['number','title','text','start','end']].to_json(orient="records")}

Student Question:
{query}

Your task:
- Answer the question directly.
- Tell the learner which video number contains the topic.
- Mention the timestamp.
- Briefly explain what is taught there.
- Guide the learner politely to watch that section.

Now answer the question.
"""

    response = inference(prompt)

    st.subheader("Answer")
    st.write(response)
    
    st.subheader("Retrieved Context")

    st.dataframe(new_df[["number", "title", "start", "end", "text"]])