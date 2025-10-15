# modules/recommender.py
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from models.embedding_model import get_embedding

def recommend_products_by_text(query, data, model, top_k=5):
    """Gợi ý sản phẩm dựa trên mô tả hoặc tên (content-based)."""
    query_vector = get_embedding(query, model)
    product_vectors = np.array([get_embedding(desc, model) for desc in data["description"]])
    scores = cosine_similarity([query_vector], product_vectors)[0]
    data = data.copy()
    data["score"] = scores
    return data.sort_values(by="score", ascending=False).head(top_k)

def recommend_products_by_attribute(data, skin_type="oily"):
    """Gợi ý sản phẩm theo thuộc tính da."""
    filtered = data[data["description"].str.contains("oil|mụn|bã nhờn", case=False, na=False)]
    return filtered.head(5) if not filtered.empty else data.sample(5)
