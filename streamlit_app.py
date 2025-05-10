import streamlit as st
import re
import requests
from streamlit_lottie import st_lottie

# ------------ Fungsi Tambahan ------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------------ Data & Fungsi Mr ------------
massa_atom = {
    "H": 1.008, "O": 16.00, "C": 12.01, "N": 14.01, "Cl": 35.45,
    "Na": 22.99, "K": 39.10, "Ca": 40.08, "Fe": 55.85
}

def hitung_mr(rumus):
    elemen = re.findall(r'([A-Z][a-z]*)(\d*)', rumus)
    mr = 0
    for simbol, jumlah in elemen:
        jumlah = int(jumlah) if jumlah else 1
        mr += massa_atom.get(simbol, 0) * jumlah
    return mr

# ------------ Lottie Animasi ------------
anim_dashboard = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_yzoqyyqv.json")
anim_kimia = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_q6zr3sdd.json")

# ------------ Konfigurasi Aplikasi ------------
st.set_page_config(page_title="Limbah Industri", layout="centered", page_icon="♻️")

with st.sidebar:
    st.title("♻️ Navigasi")
    menu = st.radio("Pilih Halaman", ["Beranda", "Edukasi", "Simulasi", "Kalkulator Mr"])
    st.caption("Aplikasi edukatif pengolahan limbah industri")

# ------------ Halaman Beranda ------------
if menu == "Beranda":
    st.title("Aplikasi Pengolahan Limbah Industri")
    if anim_dashboard:
        st_lottie(anim_dashboard, height=200)
    st.write("Selamat datang! Gunakan menu di samping untuk belajar dan simulasi.")
    st.success("Aplikasi ini cocok untuk edukasi, laboratorium, atau pelatihan.")

# ------------ Halaman Edukasi ------------
elif menu == "Edukasi":
    st.title("Materi Edukasi Limbah Industri")
    st.markdown("""
    ### Jenis Limbah
    - Limbah Cair
    - Limbah Padat
    - Limbah Gas

    ### Proses Pengolahan
    1. Koagulasi
    2. Flokulasi
    3. Sedimentasi
    4. Filtrasi
    5. Disinfeksi
    """)
    st.info("Penjelasan detail bisa ditambahkan di versi lanjutan.")

# ------------ Halaman Simulasi ------------
elif menu == "Simulasi":
    st.title("Simulasi Pengolahan")
    st.warning("Fitur simulasi seperti uji pH, COD, dan dosis bahan kimia akan hadir selanjutnya.")

# ------------ Halaman Kalkulator Mr ------------
elif menu == "Kalkulator Mr":
    st.title("⚗️ Kalkulator Massa Molekul Relatif (Mr)")
    col1, col2 = st.columns([1, 2])
    with col1:
        if anim_kimia:
            st_lottie(anim_kimia, height=150)
    with col2:
        st.markdown("Masukkan rumus kimia senyawa untuk menghitung nilai Mr.")

    rumus = st.text_input("Masukkan Rumus Kimia", placeholder="Contoh: NaCl, H2SO4")
    if rumus:
        hasil = hitung_mr(rumus)
        st.success(f"Mr dari **{rumus.upper()}** adalah **{hasil:.2f} g/mol**")
