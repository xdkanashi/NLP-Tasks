from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity #pip install scikit-learn

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

words = ["māja", "dzīvoklis", "jūra"]

word_vectors = []
for word in words:
    inputs = tokenizer(word, return_tensors="pt")
    outputs = model(**inputs)
    vector = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    word_vectors.append(vector)

word_vectors = torch.cat([torch.tensor(v) for v in word_vectors], dim=0).numpy()

similarities = cosine_similarity(word_vectors)

print("Cosine Similarity Matrix:")
print(similarities)
