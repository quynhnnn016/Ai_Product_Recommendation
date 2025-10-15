# modules/action_simulator.py
import streamlit as st

def simulate_email_promo(product_name):
    """Mô phỏng gửi email khuyến mãi."""
    st.success(f"🎉 Ưu đãi cho bạn: Sản phẩm **{product_name}** đang giảm 10%! Mua ngay hôm nay nhé ❤️")

def simulate_cart_action(product_name):
    """Mô phỏng thêm vào giỏ hàng."""
    st.info(f"🛒 {product_name} đã được thêm vào giỏ hàng của bạn!")
