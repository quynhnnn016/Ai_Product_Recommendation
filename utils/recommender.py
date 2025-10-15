import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from models.embedding_model import generate_embeddings

def recommend_products(query, products_df, model=None, embeddings_path="embeddings/product_vectors.npy", top_k=5):
    """
    Recommend top_k similar products based on the input query.
    """
    # Load existing embeddings (if any)
    try:
        product_embeddings = np.load(embeddings_path)
    except FileNotFoundError:
        # Generate and save embeddings if not found
        product_embeddings = generate_embeddings(products_df["description"].tolist(), model)
        np.save(embeddings_path, product_embeddings)

    # Generate embedding for query
    query_embedding = generate_embeddings([query], model)

    # Compute cosine similarity
    similarity_scores = cosine_similarity(query_embedding, product_embeddings)[0]

    # Get top_k results
    top_indices = similarity_scores.argsort()[::-1][:top_k]
    recommendations = products_df.iloc[top_indices].copy()
    recommendations["similarity"] = similarity_scores[top_indices]

    return recommendations[["name", "description", "price", "similarity", "image"]]
