import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Limbah Industri", layout="wide")

# Tambahkan CSS kustom
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Roboto', sans-serif;
            background-color: #f1f8f4;
        }

        .main-title {
            font-size: 48px;
            font-weight: 700;
            color: #2e7d32;
            padding: 30px 0 10px 0;
            text-align: center;
            animation: fadeInDown 1s ease-out;
        }

        .subtitle {
            font-size: 22px;
            color: #4caf50;
            text-align: center;
            margin-bottom: 30px;
            animation: fadeIn 2s ease-in;
        }

        .content-box {
            background-color: #e8f5e9;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            animation: fadeInUp 1.5s ease-out;
            margin: 0 auto;
            max-width: 900px;
        }

        .cta-box {
            background-color: #c8e6c9;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            margin-top: 40px;
        }

        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# Judul Halaman
st.markdown('<div class="main-title">Selamat Datang di Aplikasi Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simulasi & Edukasi untuk Lingkungan yang Lebih Bersih dan Berkelanjutan</div>', unsafe_allow_html=True)

# Gambar utama
st.image("https://images.unsplash.com/photo-1600691962274-d2f71c82b9cd", use_container_width=True)

# Box konten utama
st.markdown("""
<div class="content-box">
    <p>
        Aplikasi ini bertujuan untuk meningkatkan pemahaman tentang proses pengolahan limbah industri melalui pendekatan interaktif dan informatif. 
        Terdapat berbagai fitur seperti edukasi tahapan pengolahan limbah, perhitungan simulasi laboratorium, serta referensi praktis bagi pengguna dari berbagai latar belakang.
    </p>
    <p>
        Baik Anda seorang mahasiswa, peneliti, atau praktisi lingkungan, aplikasi ini dapat membantu merancang solusi yang lebih baik dan berkelanjutan.
    </p>
</div>
""", unsafe_allow_html=True)

# Ikon fitur dengan kolom
st.subheader("Apa yang Bisa Anda Lakukan di Sini?")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://img.icons8.com/color/96/lab-items.png", width=64)
    st.markdown("### Simulasi Uji Lab")
    st.caption("Hitung parameter limbah dan uji pengolahan secara virtual.")

with col2:
    st.image("https://img.icons8.com/color/96/education.png", width=64)
    st.markdown("### Edukasi Proses")
    st.caption("Pelajari tahap demi tahap pengolahan limbah industri.")

with col3:
    st.image("https://img.icons8.com/color/96/data-configuration.png", width=64)
    st.markdown("### Manajemen Data")
    st.caption("Simpan dan kelola data hasil simulasi untuk analisis lanjut.")

# Call-to-action
st.markdown("""
<div class="cta-box">
    <h4>Siap Mulai? Yuk Coba Fitur Kami!</h4>
</div>
""", unsafe_allow_html=True)

# Tombol navigasi
colA, colB, colC = st.columns([1,1,1])
with colA:
    if st.button("▶ Edukasi"):
        st.switch_page("pages/edukasi.py")  # pastikan file ini ada
with colB:
    if st.button("⚗ Simulasi"):
        st.switch_page("pages/simulasi.py")  # pastikan file ini ada
with colC:
    if st.button("📂 Data"):
        st.switch_page("pages/data.py")  # pastikan file ini ada
