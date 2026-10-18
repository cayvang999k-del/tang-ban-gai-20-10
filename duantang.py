import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# 1. CẤU HÌNH TRANG WEB
# ---------------------------------------------------------
st.set_page_config(
    page_title="Gửi Linh - 20/10 Ý Nghĩa 🌸",
    page_icon="💖",
    layout="centered"
)

# ---------------------------------------------------------
# 2. TẠO CÁC TAB TƯƠNG TÁC
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 Trang Chủ", 
    "📸 Kỷ Niệm", 
    "💌 Hộp Thư Mật Mã", 
    "🎮 Trò Chơi Vui"
])

# ---------------------------------------------------------
# TAB 1: TRANG CHỦ & ĐỒNG HỒ ĐẾM NGƯỢC
# ---------------------------------------------------------
with tab1:
    st.title("💖 Chúc Mừng Ngày 20/10 Linh Nhé!")
    st.subheader("Thế giới nhỏ của anh 🌸")
    
    st.markdown("---")
    
    # Tính số ngày yêu nhau (Bạn hãy chỉnh ngày bắt đầu yêu nhau ở đây: Năm, Tháng, Ngày)
    ngay_bat_dau = datetime(2023, 1, 1) # <--- SỬA NGÀY TẠI ĐÂY
    ngay_hien_tai = datetime.now()
    so_ngay_yeu = (ngay_hien_tai - ngay_bat_dau).days

    st.metric(label="🥰 Số ngày chúng mình đã bên nhau:", value=f"{so_ngay_yeu} ngày")
    
    st.balloons() # Hiệu ứng bóng bay khi vào trang
    st.info("Mỗi ngày trôi qua bên em đều là một ngày đặc biệt đối với anh!")

# ---------------------------------------------------------
# TAB 2: THƯ VIỆN KỶ NIỆM
# ---------------------------------------------------------
with tab2:
    st.header("📸 Góc Kỷ Niệm Của Chúng Mình")
    st.write("Nhấp vào từng kỷ niệm để xem điều đặc biệt nhé!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Chuyến đi cùng nhau")
        # Bạn có thể thay link ảnh bằng đường dẫn ảnh trong máy hoặc link web
        st.image("https://picsum.photos/400/300", caption="Kỷ niệm đẹp")
        with st.expander("Chuyện kể đằng sau bức ảnh..."):
            st.write("Hôm đó là một ngày rất đặc biệt vì...")

    with col2:
        st.subheader("Buổi hẹn hò đáng nhớ")
        st.image("https://picsum.photos/400/301", caption="Nụ cười của em")
        with st.expander("Chuyện kể đằng sau bức ảnh..."):
            st.write("Lần đầu tiên em cười tươi như thế khi...")

# ---------------------------------------------------------
# TAB 3: HỘP THƯ MẬT MÃ
# ---------------------------------------------------------
with tab3:
    st.header("💌 Hộp Thư Mật Mã Tình Yêu")
    st.write("Nhập mật mã bí mật (ví dụ: ngày sinh nhật của em hoặc 2010) để mở thư!")
    
    mat_khaunhap = st.text_input("Nhập mật mã tại đây:", type="password")
    
    # Mật mã mặc định là 2010 (bạn có thể đổi thành ngày sinh nhật, vd: 1510)
    if mat_khaunhap == "2010":
        st.success("🔓 Mở khóa thành công!")
        st.markdown("""
        ### Gửi em - Linh yêu dấu! 🌹
        Cảm ơn em đã luôn ở bên cạnh anh, mang lại cho anh những niềm vui và sự ấm áp. 
        Nhân ngày 20/10, anh chúc em luôn xinh đẹp, hạnh phúc, đạt kết quả thật cao trong học tập 
        và luôn là cô gái tuyệt vời nhất trong lòng anh! ❤️
        """)
        st.snow() # Hiệu ứng tuyết rơi lãng mạn
    elif mat_khaunhap != "":
        st.error("❌ Mật mã chưa đúng rồi, thử lại xem nào!")

# ---------------------------------------------------------
# TAB 4: TRÒ CHƠI NHỎ
# ---------------------------------------------------------
with tab4:
    st.header("🎮 Thử Thách: Em Hiểu Anh Đến Mức Nào?")
    
    cau_hoi = st.radio(
        "Món ăn mà anh thích ăn nhất khi đi cùng em là gì?",
        ["Lẩu thái", "Nướng BBQ", "Bún đậu mắm tôm", "Món em nấu"]
    )
    
    if st.button("Kiểm tra câu trả lời"):
        if cau_hoi == "Món em nấu":
            st.balloons()
            st.success("Chính xác 100%! Món em nấu là tuyệt vời nhất ❤️")
        else:
            st.warning("Gần đúng rồi, nhưng đáp án đúng nhất phải là món do em nấu cơ! 😜")