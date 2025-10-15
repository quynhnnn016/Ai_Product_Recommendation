# models/embedding_model.py
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Hàm khởi tạo model (dùng model nhẹ để chạy nhanh)
def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    """
    Load pre-trained sentence transformer model.
    """
    return SentenceTransformer(model_name)

# Hàm sinh embedding cho 1 đoạn văn bản
def get_embedding(text, model):
    """
    Trả về vector embedding cho 1 chuỗi text.
    """
    return model.encode(text, show_progress_bar=False, convert_to_numpy=True)

# Hàm sinh embedding cho danh sách text (nhiều dòng)
def generate_embeddings(text_list, model=None):
    """
    Generate embeddings for a list of text strings.
    """
    if model is None:
        model = load_embedding_model()
    embeddings = model.encode(text_list, show_progress_bar=False, convert_to_numpy=True)
    return np.array(embeddings)
