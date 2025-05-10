import streamlit as st
import re 
from streamlit_lottie import st_lottie
import requests

# ----------------------
# Fungsi umum
# ----------------------

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

massa_atom = {
    "H": 1.008, "O": 16.00, "C": 12.01, "N": 14.01, "Cl": 35.45,
    "Na": 22.99, "K": 39.10, "Ca": 40.08, "Fe": 55.85
}

def hitung_mr(rumus):
    elemen = re.findall(r'([A-Z][a-z]*)(\d*)', rumus)
    mr = 0
    for simbol, jumlah in elemen:
        jumlah = int(jumlah) if jumlah else 1
        massa = massa_atom.get(simbol, 0)
        mr += massa * jumlah
    return mr

lottie_kimia = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_q6zr3sdd.json")
lottie_dashboard = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_yzoqyyqv.json")

# ----------------------
# Halaman
# ----------------------

def halaman_beranda():
    st.title("Dashboard Pengolahan Limbah Industri")
    st.markdown("Selamat datang di aplikasi edukasi & simulasi pengolahan limbah industri.")
    if lottie_dashboard:
        st_lottie(lottie_dashboard, height=200)
    st.info("Gunakan menu di sebelah kiri untuk mengakses fitur edukasi, simulasi, dan kalkulator.")

def halaman_edukasi():
    st.title("Materi Edukasi")
    st.markdown("""
    #### Jenis Limbah Industri
    - Limbah cair (contoh: limbah pabrik tekstil)
    - Limbah padat (contoh: lumpur industri)
    - Limbah gas (contoh: emisi pabrik)
    
    #### Proses Pengolahan Limbah
    1. **Koagulasi-Flokulasi**
    2. **Sedimentasi**
    3. **Filtrasi**
    4. **Disinfeksi**
    
    Pelajari tiap proses di modul interaktif (akan dikembangkan).
    """)

def halaman_simulasi():
    st.title("Simulasi Pengolahan Limbah")
    st.warning("Simulasi interaktif sedang dikembangkan.")
    st.write("Contoh yang bisa ditambahkan: uji pH, COD, dosis bahan kimia, efisiensi proses, dll.")

def halaman_kalkulator_mr():
    st.title("⚗️ Kalkulator Massa Molekul Relatif (Mr)")
    col1, col2 = st.columns([1, 2])
    with col1:
        if lottie_kimia:
            st_lottie(lottie_kimia, height=150)
    with col2:
        st.markdown("Masukkan rumus kimia senyawa untuk menghitung nilai **Mr**.")

    rumus = st.text_input("Masukkan Rumus Kimia", placeholder="Contoh: NaCl, H2SO4")

    if rumus:
        hasil = hitung_mr(rumus)
        st.success(f"Mr dari **{rumus.upper()}** adalah **{hasil:.2f} g/mol**")

# ----------------------
# Layout & Navigasi
# ----------------------

st.set_page_config(page_title="Limbah Industri Edukasi", layout="centered", page_icon="♻️")

with st.sidebar:
    st.title("♻️ Menu Navigasi")
    menu = st.radio("Pilih Halaman", ["Beranda", "Edukasi", "Simulasi", "Kalkulator Mr"])
    st.markdown("---")
    st.caption("By: Proyek Edukasi Industri")

if menu == "Beranda":
    halaman_beranda()
elif menu == "Edukasi":
    halaman_edukasi()
elif menu == "Simulasi":
    halaman_simulasi()
elif menu == "Kalkulator Mr":
    halaman_kalkulator_mr()
