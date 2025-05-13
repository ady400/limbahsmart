import time
import numpy as np
import pandas as pd
import streamlit as st
import io
from streamlit_lottie import st_lottie
import requests
import io
import plotly.graph_objects as go

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
lottie_interaktif = load_lottie_url("https://lottie.host/05ce74d8-a548-48b4-9dd0-04ec7c20bec1/gKJaJSYHw1.json")


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
    st_lottie(lottie_beranda, speed=1, loop=True, quality="high", height=400)
    st.markdown("""
        <style>
        .hero {
            background: linear-gradient(135deg, #d4edda, #3498db);
            color: green;
            padding: 40px 20px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 30px;
            animation: fadeIn 2s;
        }
        </style>
        <div class='hero'>
            <h1>♻️ Manajemen & Edukasi Limbah Industri ♻️</h1>
            <p>Belajar dan simulasi proses pengolahan limbah industri secara interaktif dan edukatif.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st_lottie(lottie_edukasi, speed=1, loop=True, quality="high", height=150)
        st.markdown("### Edukasi Proses")
        st.write("Kenali tahapan pengolahan limbah dari awal hingga akhir.")
    with col2:
        st_lottie(lottie_laboratorium, speed=1, loop=True, quality="high", height=150)
        st.markdown("### Uji Laboratorium")
        st.write("Hitung nilai COD, BOD, TSS, dan pH dari data sampel.")
    with col3:
        st_lottie(lottie_interaktif, speed=1, loop=True, quality="high", height=150)
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

            fig = go.Figure(data=[go.Pie(
                labels=["COD", "Sisa"],
                values=[hasil, max(1000 - hasil, 0)],
                hole=0.5,
                marker_colors=["#2C3E50", "#95a5a6"]
            )])
            fig.update_layout(width=400, height=300)
            st.plotly_chart(fig)

            buffer = io.StringIO()
            buffer.write(f"Hasil Uji COD\nVolume titran: {v} mL\nNormalitas: {n} N\nVolume sampel: {vs} mL\n=> COD = {hasil:.2f} mg/L")
            st.download_button("📄 Unduh Hasil", buffer.getvalue(), file_name="hasil_uji_cod.txt")

    elif uji == "BOD":
        awal = st.number_input("DO Awal (mg/L)", value=8.0)
        akhir = st.number_input("DO Akhir (mg/L)", value=2.0)
        if st.button("Hitung BOD"):
            hasil = awal - akhir
            st.success(f"BOD = {hasil:.2f} mg/L")

            fig = go.Figure(data=[go.Pie(
                labels=["Terpakai (BOD)", "Tersisa (Oksigen)"],
                values=[hasil, akhir],
                hole=0.5,
                marker_colors=["#3498db", "#ecf0f1"]
            )])
            fig.update_layout(width=400, height=300)
            st.plotly_chart(fig)

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

            fig = go.Figure(data=[go.Pie(
                labels=["Padatan Tersuspensi", "Lainnya"],
                values=[hasil, max(100 - hasil, 0)],
                hole=0.5,
                marker_colors=["#9b59b6", "#dcdde1"]
            )])
            fig.update_layout(width=400, height=300)
            st.plotly_chart(fig)

            buffer = io.StringIO()
            buffer.write(f"Hasil Uji TSS\nBerat awal: {awal} mg\nBerat akhir: {akhir} mg\nVolume: {volume} L\n=> TSS = {hasil:.2f} mg/L")
            st.download_button("📄 Unduh Hasil", buffer.getvalue(), file_name="hasil_uji_tss.txt")

    elif uji == "pH":
        ph = st.slider("pH sampel", 0.0, 14.0, 7.0)
        st.info(f"pH = {ph}")
        warna = "#2ecc71" if 6.5 <= ph <= 8.5 else "#e74c3c"
        fig = go.Figure(data=[go.Pie(
            labels=["pH", "Selisih dari Netral"],
            values=[ph, 14 - ph],
            hole=0.5,
            marker_colors=[warna, "#ecf0f1"]
        )])
        fig.update_layout(width=400, height=300)
        st.plotly_chart(fig)

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

        fig = go.Figure(data=[go.Pie(
            labels=["Terolah", "Tersisa"],
            values=[awal - akhir, akhir],
            hole=0.5,
            marker_colors=["#27ae60", "#e74c3c"]
        )])
        fig.update_layout(width=400, height=300)
        st.plotly_chart(fig)

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
