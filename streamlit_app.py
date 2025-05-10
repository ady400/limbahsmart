import streamlit as st
import pandas as pd
import numpy as np
import time
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Limbah Track", layout="wide")

# Fungsi load animasi dari Lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets4.lottiefiles.com/packages/lf20_puciaact.json"
lottie_anim = load_lottieurl(lottie_url)

# Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
    background-color: #f0f4f8;
    color: #333;
}
.big-title {
    font-size: 36px;
    font-weight: 600;
    color: #2C3E50;
    text-align: center;
    margin-bottom: 20px;
    animation: slideFade 1s ease-in-out;
}
.card {
    background-color: #fff;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    text-align: center;
}
.card h2 {
    font-size: 32px;
    margin: 0;
}
.card p {
    margin: 0;
    color: #888;
}
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #fff;
    border-top: 1px solid #ccc;
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
}
.bottom-nav div {
    text-align: center;
    font-size: 12px;
    color: #666;
}
@keyframes slideFade {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st_lottie(lottie_anim, height=150, key="anim")
    st.title("♻️ Limbah Track")
    st.markdown("**Belajar & Simulasi Pengolahan Limbah Industri** 🌍")
    menu = st.radio("Navigasi", ["🏠 Beranda", "⚙️ Proses", "🧪 Uji Lab", "🧩 Simulasi", "ℹ️ Tentang"])
    st.caption("© 2025 Kelompok 6 - 1F PLI AKA")

# Konten
if menu == "🏠 Beranda":
    st.markdown('<div class="big-title">♻️ Limbah Track Dashboard</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h2>8.7</h2><p>pH Status</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h2>10.4%</h2><p>Humidity</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h2>430</h2><p>PPM Status</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h2>OK</h2><p>Status</p></div>', unsafe_allow_html=True)

elif menu == "⚙️ Proses":
    st.markdown('<div class="big-title">⚙️ Tahapan Pengolahan Limbah</div>', unsafe_allow_html=True)
    st.write("""
    ### 1. Pra-Pengolahan
    - Screening
    - Grit Chamber
    - Equalization Tank

    ### 2. Pengolahan Primer
    - Primary Clarifier

    ### 3. Pengolahan Sekunder
    - Aerob / Anaerob

    ### 4. Pengolahan Tersier
    - Filtrasi / Kimia

    ### 5. Pengolahan Lumpur
    - Digestion / Dewatering

    ### 6. Pembuangan Akhir
    - Buangan yang memenuhi baku mutu
    """)

elif menu == "🧪 Uji Lab":
    st.markdown('<div class="big-title">🧪 Kalkulator Uji Laboratorium</div>', unsafe_allow_html=True)
    uji = st.selectbox("Pilih jenis uji:", ["COD", "BOD", "TSS", "pH"])

    if uji == "COD":
        v = st.number_input("Volume titran (mL)", value=10.0)
        n = st.number_input("Normalitas titran (N)", value=0.25)
        vs = st.number_input("Volume sampel (mL)", value=50.0)
        if st.button("Hitung COD"):
            hasil = (v * n * 8000) / vs
            st.success(f"COD = {hasil:.2f} mg/L")

    elif uji == "BOD":
        awal = st.number_input("DO Awal (mg/L)", value=8.0)
        akhir = st.number_input("DO Akhir (mg/L)", value=2.0)
        if st.button("Hitung BOD"):
            hasil = awal - akhir
            st.success(f"BOD = {hasil:.2f} mg/L")

    elif uji == "TSS":
        awal = st.number_input("Berat filter awal (mg)", value=100.0)
        akhir = st.number_input("Berat filter akhir (mg)", value=120.0)
        volume = st.number_input("Volume sampel (L)", value=1.0)
        if st.button("Hitung TSS"):
            hasil = (akhir - awal) / volume
            st.success(f"TSS = {hasil:.2f} mg/L")

    elif uji == "pH":
        ph = st.slider("pH sampel", 0.0, 14.0, 7.0)
        st.info(f"pH = {ph}")

elif menu == "🧩 Simulasi":
    st.markdown('<div class="big-title">🔄 Simulasi Pengolahan Limbah</div>', unsafe_allow_html=True)
    jenis = st.selectbox("Jenis limbah", ["Organik", "Kimia", "Campuran"])
    awal = st.number_input("Konsentrasi awal (mg/L)", value=500.0)
    efisiensi = {"Organik": 0.85, "Kimia": 0.70, "Campuran": 0.60}[jenis]
    if st.button("Mulai Simulasi"):
        akhir = awal * (1 - efisiensi)
        st.success(f"Hasil akhir: {akhir:.2f} mg/L ({efisiensi*100:.0f}% efisiensi)")

elif menu == "ℹ️ Tentang":
    st.markdown('<div class="big-title">ℹ️ Tentang Aplikasi Ini</div>', unsafe_allow_html=True)
    st.write("""
    Aplikasi edukatif ini dibuat untuk mengenalkan proses pengolahan limbah industri secara interaktif.
    
    - Teknologi: Python + Streamlit
    - Pengembang: Kelompok 6 - 1F PLI AKA
    - Versi: 1.0
    """)


