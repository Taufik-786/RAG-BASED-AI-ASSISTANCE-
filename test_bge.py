from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")

embedding = model.encode(["hello world"])
print(embedding.shape)
