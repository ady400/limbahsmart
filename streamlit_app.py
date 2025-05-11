import time
import numpy as np
import pandas as pd
import streamlit as st
import io
from streamlit_lottie import st_lottie
import requests

# Fungsi untuk memuat animasi lottie dari URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animations
lottie_beranda = load_lottie_url("https://lottie.host/947d937e-1b76-43a0-b786-d255c0ee1e74/stE5uwmVhW.json")
lottie_lab = load_lottie_url("https://lottie.host/ad0ad4a2-3e19-4bc4-a8f8-6447dbc72c73/s5hNdaq1uX.json")
lottie_simulasi = load_lottie_url("https://lottie.host/452e722c-e5f7-4a5a-bdaa-4f46c93a4ee6/FlkgyfRxKz.json")
lottie_proses = load_lottie_url("https://lottie.host/83a75fcc-2836-4020-ba68-10b9e0f7aa75/RTuEA9yHNB.json")
lottie_edukasi = load_lottie_url("https://lottie.host/30b3a6b0-a898-4862-a498-5600b93ee6a7/R9YyJLBYSA.json")
lottie_laboratorium = load_lottie_url("https://lottie.host/512b24b7-72c0-4868-93cf-641162ab8ce5/y2TUFxINa1.json")
lottie_interaktif = load_lottie_url("https://lottie.host/c05db921-8621-4615-9dbc-b2426d2498f1/P8ISIUBD92.json")


# Konfigurasi halaman
st.set_page_config(page_title="Limbah Track", page_icon="♻️", layout="wide")

# Sidebar
with st.sidebar:
    st.title("♻️ Limbah Track")
    st.markdown("Belajar & Simulasi Pengolahan Limbah Industri 🌍")
    st.markdown("---")
    menu = st.radio("Navigasi", ["🏠 Beranda", "⚙️ Proses", "🧪 Uji Lab", "🧩 Simulasi", "ℹ️ Tentang"])
    st.markdown("---")
    st.caption("© 2025 Kelompok 6 - 1F PLI AKA")

# CSS tambahan buat mempercantik
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        color: #2C3E50;
        text-align: center;
        padding: 20px 0;
        animation: fadeIn 2s;
    }
    .stButton>button {
        background-color: #2C3E50;
        color: white;
    }
    body {
        background-color: #f5f9ff;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# BERANDA
if menu == "🏠 Beranda":
    st_lottie(lottie_beranda, speed=1, loop=True, quality="high", height=300)
    st.markdown("""
    <div style='text-align: center; padding: 30px 0;'>
        <h1 style='color:#2C3E50;'>♻️ Manajemen & Edukasi Limbah Industri ♻️</h1>
        <p style='font-size:18px; color:#555;'>Belajar dan simulasi proses pengolahan limbah industri secara interaktif dan edukatif.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st_lottie(lottie_edukasi, height=100)
        st.markdown("### Edukasi Proses")
        st.write("Kenali tahapan pengolahan limbah dari awal hingga akhir.")
    with col2:
        st_lottie(lottie_laboratorium, height=100)
        st.markdown("### Uji Laboratorium")
        st.write("Hitung nilai COD, BOD, TSS, dan pH dari data sampel.")
    with col3:
        st_lottie(lottie_interaktif, height=100)
        st.markdown("### Simulasi Interaktif")
        st.write("Lakukan simulasi pengolahan limbah dengan berbagai jenis.")

# PROSES
elif menu == "⚙️ Proses":
    st_lottie(lottie_proses, speed=1, loop=True, quality="high", height=200)
    st.markdown('<div class="main-title">⚙️ Tahapan Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 🧹 1. Pra-Pengolahan (Pre-Treatment)
    - Screening: Menyaring benda kasar seperti plastik dan kayu.
    - Grit Chamber: Mengendapkan partikel berat seperti pasir.
    - Equalization Tank: Menyeimbangkan aliran dan beban limbah.

    ### 🧪 2. Pengolahan Primer
    - Primary Clarifier: Mengendapkan padatan tersuspensi.

    ### 🧬 3. Pengolahan Sekunder (Biologis)
    - Aerob: Dengan oksigen (activated sludge, trickling filter).
    - Anaerob: Tanpa oksigen untuk limbah berat.

    ### 🧼 4. Pengolahan Tersier
    - Filtrasi, Reverse Osmosis, Proses Kimia.

    ### 🧱 5. Pengolahan Lumpur
    - Thickening, Digestion, Dewatering.

    ### 🌊 6. Pembuangan Akhir
    - Limbah cair buangan yang memenuhi standar.
    """)

# UJI LAB
elif menu == "🧪 Uji Lab":
    st_lottie(lottie_lab, speed=1, loop=True, quality="high", height=200)
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
    st_lottie(lottie_simulasi, speed=1, loop=True, quality="high", height=200)
    st.markdown('<div class="main-title">🧩 Simulasi Pengolahan Limbah</div>', unsafe_allow_html=True)
    jenis = st.selectbox("Jenis limbah", ["Organik", "Kimia", "Campuran"])
    awal = st.number_input("Konsentrasi awal (mg/L)", value=500.0)

    efisiensi = {"Organik": 0.85, "Kimia": 0.70, "Campuran": 0.60}[jenis]
    if st.button("Mulai Simulasi"):
        akhir = awal * (1 - efisiensi)
        st.success(f"Hasil akhir: {akhir:.2f} mg/L ({efisiensi*100:.0f}% efisiensi)")

        buffer = io.StringIO()
        buffer.write(f"Simulasi Pengolahan Limbah\nJenis: {jenis}\nKonsentrasi awal: {awal} mg/L\nEfisiensi: {efisiensi*100:.0f}%\n=> Hasil akhir: {akhir:.2f} mg/L")
        st.download_button("📄 Unduh Hasil", buffer.getvalue(), file_name="hasil_simulasi.txt")

# TENTANG
elif menu == "ℹ️ Tentang":
    st.markdown('<div class="main-title">ℹ️ Tentang Aplikasi Ini</div>', unsafe_allow_html=True)
    st.write("""
    Aplikasi edukatif ini dibuat untuk mengenalkan proses pengolahan limbah industri secara interaktif.

    - Teknologi: Python + Streamlit
    - Pengembang: Kelompok 6 - 1F PLI AKA
    - Versi: 1.0
    - Sumber: Modul Teknik Lingkungan, Litbang KLHK
    """)
