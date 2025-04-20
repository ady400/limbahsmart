import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Limbah Industri", layout="wide")

# Tambahkan CSS kustom
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f1f8f4;
        }

        .main-title {
            font-size: 40px;
            font-weight: 700;
            color: #2e7d32;
            text-align: center;
            padding-top: 30px;
        }

        .subtitle {
            font-size: 20px;
            color: #4caf50;
            text-align: center;
            margin-bottom: 20px;
        }

        .content-box {
            background-color: #e8f5e9;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            margin: auto;
        }

        .section {
            text-align: center;
            margin-top: 40px;
        }

        .icon-title {
            font-size: 18px;
            font-weight: 600;
            margin-top: 10px;
        }

        .icon-desc {
            font-size: 14px;
            color: #444;
        }

        .cta {
            background-color: #c8e6c9;
            text-align: center;
            padding: 20px;
            border-radius: 12px;
            margin: 40px auto 0;
            max-width: 600px;
        }

        .feature-icon {
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Judul halaman
st.markdown('<div class="main-title">Selamat Datang di Aplikasi Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simulasi & Edukasi untuk Lingkungan yang Lebih Bersih dan Berkelanjutan</div>', unsafe_allow_html=True)

# Gambar utama
image_url = "https://images.unsplash.com/photo-1600691962274-d2f71c82b9cd?auto=format&fit=crop&w=1400&q=80"
try:
    st.image(image_url, use_container_width=True, caption="Ilustrasi Pengolahan Limbah Industri")
except:
    st.warning("Gagal memuat gambar utama.")

# Konten utama
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

# Ikon fitur
st.markdown('<div class="section"><h4>Fitur Utama Aplikasi</h4></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://img.icons8.com/color/96/lab-items.png", width=64, class_="feature-icon")
    st.markdown('<div class="icon-title">Simulasi Uji Lab</div>', unsafe_allow_html=True)
    st.markdown('<div class="icon-desc">Hitung parameter limbah dan uji pengolahan secara virtual.</div>', unsafe_allow_html=True)

with col2:
    st.image("https://img.icons8.com/color/96/education.png", width=64, class_="feature-icon")
    st.markdown('<div class="icon-title">Edukasi Proses</div>', unsafe_allow_html=True)
    st.markdown('<div class="icon-desc">Pelajari tahapan pengolahan limbah secara menyeluruh.</div>', unsafe_allow_html=True)

with col3:
    st.image("https://img.icons8.com/color/96/data-configuration.png", width=64, class_="feature-icon")
    st.markdown('<div class="icon-title">Manajemen Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="icon-desc">Simpan dan kelola hasil simulasi untuk keperluan analisis.</div>', unsafe_allow_html=True)

# CTA (Call to Action)
st.markdown("""
<div class="cta">
    <h4>Siap Mulai? Ayo Eksplorasi Fitur Kami!</h4>
</div>
""", unsafe_allow_html=True)

# Navigasi tombol
colA, colB, colC = st.columns(3)
with colA:
    if st.button("▶ Edukasi"):
        st.info("Halaman edukasi belum tersedia.")
with colB:
    if st.button("⚗ Simulasi"):
        st.info("Halaman simulasi belum tersedia.")
with colC:
    if st.button("📂 Data"):
        st.info("Halaman data belum tersedia.")
