import requests
import json
import os
import pandas as pd
import joblib

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={"model":"bge-m3","input":text_list})#it creates list of embedding for each elements of list/array 
    embedding=r.json()["embeddings"]
    return embedding

my_dicts=[]
output_json=os.listdir("output_json")
for json_file in output_json:
    print(f"so , now lets go with  {json_file}")
    with open(f"output_json/{json_file}") as f:
        content = json.load(f)
    embedding_texts = create_embedding([chunk["text"] for chunk in content["chunk"]])
    for i,chunk in enumerate(content["chunk"]):
        chunk["embedding"]=embedding_texts[i]
        my_dicts.append(chunk)


df = pd.DataFrame.from_records(my_dicts)
# saving dataframe {df} 
joblib.dump(df,"embedding.joblib")

