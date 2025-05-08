import streamlit as st
import numpy as np
import pandas as pd
import time
import io

# Konfigurasi halaman
st.set_page_config(page_title="Limbah Industri", page_icon="♻", layout="wide")

# Animasi & CSS
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f0f4f8;
    }
    .main-title {
        font-size: 40px;
        color: #2C3E50;
        text-align: center;
        padding-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }
    .stButton>button {
        background-color: #2C3E50;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(-20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("♻ Limbah Track")
    st.markdown("*Belajar & Simulasi Pengolahan Limbah Industri* 🌍")
    st.markdown("---")
    menu = st.radio("Navigasi", ["🏠 Beranda", "⚙ Proses", "🧪 Uji Lab", "🧩 Simulasi", "ℹ Tentang"])
    st.markdown("---")
    st.caption("© 2025 Kelompok 6 - 1F PLI AKA")

# BERANDA
if menu == "🏠 Beranda":
    st.markdown('<div class="main-title">♻ Aplikasi Pengolahan Limbah Industri ♻</div>', unsafe_allow_html=True)
    st.write("### Selamat datang!")
    st.info("Aplikasi ini dirancang untuk membantu memahami dan mensimulasikan proses pengolahan limbah industri.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/1866/1866365.png", width=80)
        st.subheader("Edukasi Proses")
        st.caption("Kenali tahapan pengolahan limbah dari awal hingga akhir.")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135823.png", width=80)
        st.subheader("Uji Laboratorium")
        st.caption("Hitung nilai COD, BOD, TSS, dan pH dari data sampel.")
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/2933/2933820.png", width=80)
        st.subheader("Simulasi Interaktif")
        st.caption("Simulasikan pengolahan limbah secara virtual.")

# PROSES
elif menu == "⚙ Proses":
    st.markdown('<div class="main-title">⚙ Tahapan Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.markdown("""
    #### 1. Pra-Pengolahan
    - Screening: Menyaring benda kasar
    - Grit Chamber: Mengendapkan partikel berat
    - Equalization Tank: Menstabilkan aliran

    #### 2. Pengolahan Primer
    - Primary Clarifier: Mengendapkan padatan tersuspensi

    #### 3. Pengolahan Sekunder
    - Aerob: Activated Sludge, Trickling Filter
    - Anaerob: Digester, septic tank

    #### 4. Pengolahan Tersier
    - Filtrasi, Kimia, Reverse Osmosis

    #### 5. Pengolahan Lumpur
    - Thickening, Digestion, Dewatering

    #### 6. Pembuangan Akhir
    - Limbah cair yang telah memenuhi baku mutu
    """)

# UJI LAB
elif menu == "🧪 Uji Lab":
    st.markdown('<div class="main-title">🧪 Kalkulator Uji Laboratorium</div>', unsafe_allow_html=True)
    uji = st.selectbox("Pilih jenis uji:", ["COD", "BOD", "TSS", "pH"])

    if uji == "COD":
        v = st.number_input("Volume titran (mL)", value=10.0)
        n = st.number_input("Normalitas titran (N)", value=0.25)
        vs = st.number_input("Volume sampel (mL)", value=50.0)
        if st.button("Hitung COD"):
            hasil = (v * n * 8000) / vs
            st.success(f"COD = {hasil:.2f} mg/L")
            buffer = io.StringIO()
            buffer.write(f"Hasil Uji COD\nVolume titran: {v} mL\nNormalitas: {n} N\nVolume sampel: {vs} mL\n=> COD = {hasil:.2f} mg/L")
            st.download_button("📄 Unduh Hasil", buffer.getvalue(), file_name="hasil_uji_cod.txt")

    elif uji == "BOD":
        awal = st.number_input("DO Awal (mg/L)", value=8.0)
        akhir = st.number_input("DO Akhir (mg/L)", value=2.0)
        if st.button("Hitung BOD"):
            hasil = awal - akhir
            st.success(f"BOD = {hasil:.2f} mg/L")
            buffer = io.StringIO()
            buffer.write(f"Hasil Uji BOD\nDO Awal: {awal} mg/L\nDO Akhir: {akhir} mg/L\n=> BOD = {hasil:.2f} mg/L")
            st.download_button("📄 Unduh Hasil", buffer.getvalue(), file_name="hasil_uji_bod.txt")

    elif uji == "TSS":
        awal = st.number_input("Berat filter awal (mg)", value=100.0)
        akhir = st.number_input("Berat filter akhir (mg)", value=120.0)
        volume = st.number_input("Volume sampel (L)", value=1.0)
        if st.button("Hitung TSS"):
            hasil = (akhir - awal) / volume
            st.success(f"TSS = {hasil:.2f} mg/L")
            buffer = io.StringIO()
            buffer.write(f"Hasil Uji TSS\nBerat awal: {awal} mg\nBerat akhir: {akhir} mg\nVolume: {volume} L\n=> TSS = {hasil:.2f} mg/L")
            st.download_button("📄 Unduh Hasil", buffer.getvalue(), file_name="hasil_uji_tss.txt")

    elif uji == "pH":
        ph = st.slider("pH sampel", 0.0, 14.0, 7.0)
        st.info(f"pH = {ph}")

# SIMULASI
elif menu == "🧩 Simulasi":
    st.markdown('<div class="main-title">🔄 Simulasi Pengolahan Limbah</div>', unsafe_allow_html=True)
    jenis = st.selectbox("Jenis limbah", ["Organik", "Kimia", "Campuran"])
    awal = st.number_input("Konsentrasi awal (mg/L)", value=500.0)

    efisiensi = {"Organik": 0.85, "Kimia": 0.70, "Campuran": 0.60}[jenis]
    if st.button("▶ Mulai Simulasi"):
        akhir = awal * (1 - efisiensi)
        st.success(f"Hasil akhir: {akhir:.2f} mg/L ({efisiensi*100:.0f}% efisiensi)")
        buffer = io.StringIO()
        buffer.write(f"Simulasi Pengolahan Limbah\nJenis: {jenis}\nKonsentrasi awal: {awal} mg/L\nEfisiensi: {efisiensi*100:.0f}%\n=> Hasil akhir: {akhir:.2f} mg/L")
        st.download_button("📄 Unduh Hasil", buffer.getvalue(), file_name="hasil_simulasi.txt")

# TENTANG
elif menu == "ℹ Tentang":
    st.markdown('<div class="main-title">ℹ Tentang Aplikasi Ini</div>', unsafe_allow_html=True)
    st.write("""
    Aplikasi edukatif ini dibuat untuk mengenalkan proses pengolahan limbah industri secara interaktif.
    
    - *Teknologi:* Python + Streamlit
    - *Pengembang:* Kelompok 6 - 1F PLI AKA
    - *Versi:* 1.0
    - *Sumber:* Modul Teknik Lingkungan, Litbang KLHK
    """)
