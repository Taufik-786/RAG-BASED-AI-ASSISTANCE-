import requests
import json
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib


df = joblib.load("embedding.joblib")

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={"model":"bge-m3","input":text_list})#it creates list of embedding for each elements of list/array 
    embedding=r.json()["embeddings"]
    return embedding

def inference(prompt):
    r=requests.post("http://localhost:11434/api/generate",json={
        "model":"llama3.2",
        "prompt":prompt,
        "stream":False})#it creates list of embedding for each elements of list/array 
    response=r.json()["response"]
    return response 
    
incoming_query=input("ask the question : ")
question_embedding=create_embedding([incoming_query])[0]
similarities = cosine_similarity(np.vstack(df["embedding"]),[question_embedding]).flatten()
print(similarities)
top_result=7
max_indx=similarities.argsort()[::-1][0:top_result]
# print(max_indx)
new_df = df.iloc[max_indx]
# print(new_df[['title','number','text']])

prompt = f"""
You are an assistant for a Web Development course that contains 10 videos.

Below are relevant video chunks from the course:
{new_df[['number','title','text','start','end']].to_json(orient="records")}

Student Question:
{incoming_query}

Your task:
- Answer the question directly.
- Tell the learner which video number contains the topic.
- Mention the timestamp (start and end seconds).
- Briefly explain what is taught there.
- Guide the learner politely to watch that section.
- If the question is unrelated to the course, say:
  "I can only answer questions related to this course."

Now answer the question.
"""


with open("prompt.txt","w") as f:
    f.write(prompt)
    
    
response =inference(prompt)
print(response)

with open("response.txt","w") as f:
    f.write(response)
    
