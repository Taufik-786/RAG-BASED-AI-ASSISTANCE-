import json
import os
import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

all_chunks = []

for json_file in os.listdir("output_json"):
    print(f"Processing: {json_file}")

    with open(f"output_json/{json_file}", "r", encoding="utf-8") as f:
        content = json.load(f)

    texts = [chunk["text"] for chunk in content["chunk"]]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    for i, chunk in enumerate(content["chunk"]):
        chunk["embedding"] = embeddings[i]
        all_chunks.append(chunk)

df = pd.DataFrame.from_records(all_chunks)

joblib.dump(df, "embedding.joblib")

print("Done")
print(df.shape)