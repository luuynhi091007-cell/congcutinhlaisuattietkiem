import streamlit as st
st.image("logo.jpg.JPG")
# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="🏦",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("APP TÍNH TIỀN GỬI TIẾT KIỆM TẠI NGÂN HÀNG_Lưu Ý Nhi")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================

# Số tiền gửi
tien_gui = st.number_input(
    "💰 Số tiền gửi (VNĐ)",
    min_value=0,
    value=500_000_000,
    step=1_000_000,
    format="%d"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=3,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=6.0,
    step=0.1
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# =========================
# TÍNH TOÁN
# =========================

if st.button("🧮 TÍNH TIỀN LÃI", use_container_width=True):

    # Đổi lãi suất % về số thập phân
    lai_suat_nam = lai_suat / 100

    # Đổi kỳ hạn từ tháng sang năm
    thoi_gian_nam = ky_han / 12

    # Tổng tiền lãi theo lãi đơn
    tong_tien_lai = tien_gui * lai_suat_nam * thoi_gian_nam

    # Tổng tiền nhận
    tong_tien_nhan = tien_gui + tong_tien_lai

    # =========================
    # TÍNH LÃI ĐỊNH KỲ
    # =========================

    if hinh_thuc == "Cuối kỳ":
        so_ky_nhan_lai = 1
        lai_dinh_ky = tong_tien_lai

    elif hinh_thuc == "Hàng tháng":
        so_ky_nhan_lai = ky_han
        lai_dinh_ky = tong_tien_lai / so_ky_nhan_lai

    else:  # Hàng quý
        so_ky_nhan_lai = ky_han / 3
        lai_dinh_ky = tong_tien_lai / so_ky_nhan_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("✅ Đã tính toán thành công!")

    st.subheader("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Tiền lãi định kỳ",
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

    st.metric(
        "🏦 Tổng tiền gốc + lãi",
        f"{tong_tien_nhan:,.0f} VNĐ"
    )

    # =========================
    # THÔNG TIN CHI TIẾT
    # =========================

    st.divider()

    st.subheader("📋 Chi tiết khoản tiền gửi")

    st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    if hinh_thuc == "Cuối kỳ":
        st.info(
            f"Bạn nhận toàn bộ tiền lãi {lai_dinh_ky:,.0f} VNĐ "
            f"vào cuối kỳ."
        )

    elif hinh_thuc == "Hàng tháng":
        st.info(
            f"Mỗi tháng bạn nhận khoảng "
            f"{lai_dinh_ky:,.0f} VNĐ tiền lãi."
        )

    else:
        st.info(
            f"Mỗi quý bạn nhận khoảng "
            f"{lai_dinh_ky:,.0f} VNĐ tiền lãi."
        )
