# modules/chat_handler.py

def analyze_intent(user_input):
    """
    Phân tích câu người dùng để xác định intent cơ bản.
    Trả về: intent ('find_by_attribute', 'find_similar', 'add_to_cart', ...)
    """
    text = user_input.lower()

    if "tương tự" in text or "giống" in text:
        return "find_similar"
    elif "da dầu" in text or "mụn" in text or "phù hợp" in text:
        return "find_by_attribute"
    elif "thêm vào giỏ" in text or "đặt mua" in text:
        return "add_to_cart"
    else:
        return "general_query"
