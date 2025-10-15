# app.py
import os
os.makedirs("data", exist_ok=True)
os.makedirs("embeddings", exist_ok=True)

import streamlit as st
import pandas as pd
from models.embedding_model import load_embedding_model   # ✅ Đúng tên
from modules.chat_handler import analyze_intent
from modules.recommender import recommend_products_by_text, recommend_products_by_attribute
from modules.action_simulator import simulate_email_promo, simulate_cart_action

# --- Load data và model ---
data = pd.read_csv("data/products.csv")
model = load_embedding_model()   # ✅ Khớp với hàm ở trên

st.title("💬 AI Product Recommender Chatbot")

# --- Khởi tạo giỏ hàng ---
if "cart" not in st.session_state:
    st.session_state.cart = []

# --- Input ---
user_input = st.text_input("Nhập câu hỏi hoặc mô tả của bạn:", "")

if user_input:
    intent = analyze_intent(user_input)

    if intent == "find_by_attribute":
        recs = recommend_products_by_attribute(data)
        st.subheader("🧴 Sản phẩm phù hợp với làn da của bạn:")
        for _, row in recs.iterrows():
            st.image(row["image"], width=120)
            st.write(f"**{row['name']}**")
            st.caption(row["description"])
            if st.button(f"🛒 Thêm {row['name']} vào giỏ hàng"):
                st.session_state.cart.append(row["name"])
                simulate_cart_action(row["name"])

    elif intent == "find_similar":
        recs = recommend_products_by_text(user_input, data, model)
        st.subheader("✨ Sản phẩm tương tự bạn có thể thích:")
        for _, row in recs.iterrows():
            st.image(row["image"], width=120)
            st.write(f"**{row['name']}**")
            if st.button(f"🔔 Nhận ưu đãi {row['name']}"):
                simulate_email_promo(row["name"])

    else:
        st.write("🤖 Mình chưa hiểu rõ yêu cầu, bạn có thể nói cụ thể hơn không?")

# --- Sidebar: giỏ hàng ---
st.sidebar.header("🛍️ Giỏ hàng của bạn")
if st.session_state.cart:
    for item in st.session_state.cart:
        st.sidebar.write(f"- {item}")
else:
    st.sidebar.write("Giỏ hàng trống.")
