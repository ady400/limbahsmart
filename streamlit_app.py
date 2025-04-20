import streamlit as st

# Konfigurasi
st.set_page_config(page_title="Aplikasi Limbah Industri", layout="wide")

# Sidebar Navigasi
menu = st.sidebar.selectbox("Navigasi", ["Beranda", "Proses Pengolahan", "Kalkulator Uji Lab", "Simulasi Pengolahan", "Tentang Aplikasi"])

# CSS untuk styling
st.markdown("""
    <style>
        .title { font-size: 36px; color: #2c3e50; font-weight: bold; }
        .subtitle { font-size: 24px; color: #34495e; }
    </style>
""", unsafe_allow_html=True)

# Halaman: Beranda
if menu == "Beranda":
    st.markdown('<div class="title">Selamat Datang di Aplikasi Pengolahan Limbah Industri</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1600691962274-d2f71c82b9cd", use_column_width=True)
    st.write("""
        Aplikasi ini memberikan edukasi seputar proses pengolahan limbah industri serta kalkulator simulasi pengujian laboratorium.
        Cocok digunakan oleh mahasiswa, peneliti, maupun praktisi di bidang lingkungan.
    """)

# Halaman: Proses Pengolahan
elif menu == "Proses Pengolahan":
    st.markdown('<div class="title">Proses Pengolahan Limbah</div>', unsafe_allow_html=True)
    st.markdown("""
    Berikut tahapan umum pengolahan limbah:
    
    1. **Pra-pengolahan:** Penyaringan kasar, pemisahan padatan besar.  
    2. **Pengolahan Primer:** Sedimentasi untuk mengendapkan partikel.  
    3. **Pengolahan Sekunder:** Proses biologis (aerob/anaerob).  
    4. **Pengolahan Tersier:** Penghilangan senyawa kimia & disinfeksi.  
    5. **Pembuangan Aman:** Air hasil olahan dibuang sesuai standar baku mutu.
    """)

# Halaman: Kalkulator Uji Lab
elif menu == "Kalkulator Uji Lab":
    st.markdown('<div class="title">Kalkulator Uji Laboratorium</div>', unsafe_allow_html=True)
    opsi = st.radio("Pilih Uji:", ["COD", "BOD", "TSS", "pH"])

    if opsi == "COD":
        V = st.number_input("Volume titran (mL)", 0.0, 100.0, 10.0)
        N = st.number_input("Normalitas titran (N)", 0.0, 1.0, 0.25)
        V_sampel = st.number_input("Volume sampel (mL)", 1.0, 1000.0, 50.0)
        if st.button("Hitung COD"):
            COD = (V * N * 8000) / V_sampel
            st.success(f"Hasil COD: {COD:.2f} mg/L")

    elif opsi == "BOD":
        DO_awal = st.number_input("DO Awal (mg/L)", 0.0, 20.0, 8.0)
        DO_akhir = st.number_input("DO Akhir (mg/L)", 0.0, 20.0, 2.0)
        if st.button("Hitung BOD"):
            BOD = DO_awal - DO_akhir
            st.success(f"Hasil BOD: {BOD:.2f} mg/L")

    elif opsi == "TSS":
        berat_filter_awal = st.number_input("Berat filter awal (mg)", 0.0, 1000.0, 100.0)
        berat_filter_akhir = st.number_input("Berat filter akhir (mg)", 0.0, 1000.0, 120.0)
        volume_air = st.number_input("Volume sampel (L)", 0.1, 10.0, 1.0)
        if st.button("Hitung TSS"):
            TSS = (berat_filter_akhir - berat_filter_awal) / volume_air
            st.success(f"Hasil TSS: {TSS:.2f} mg/L")

    elif opsi == "pH":
        ph_val = st.slider("Masukkan nilai pH", 0.0, 14.0, 7.0)
        st.info(f"Nilai pH sampel adalah {ph_val}")

# Halaman: Simulasi Pengolahan
elif menu == "Simulasi Pengolahan":
    st.markdown('<div class="title">Simulasi Efisiensi Pengolahan</div>', unsafe_allow_html=True)
    jenis_limbah = st.selectbox("Jenis Limbah", ["Organik", "Kimia", "Campuran"])
    konsentrasi_awal = st.number_input("Konsentrasi Awal (mg/L)", 0.0, 10000.0, 500.0)
    efisiensi = 0

    if jenis_limbah == "Organik":
        efisiensi = 0.85
    elif jenis_limbah == "Kimia":
        efisiensi = 0.70
    elif jenis_limbah == "Campuran":
        efisiensi = 0.60

    if st.button("Simulasikan"):
        hasil = konsentrasi_awal * (1 - efisiensi)
        st.success(f"Hasil akhir setelah pengolahan: {hasil:.2f} mg/L (efisiensi {efisiensi*100:.0f}%)")

# Halaman: Tentang Aplikasi
elif menu == "Tentang Aplikasi":
    st.markdown('<div class="title">Tentang Aplikasi</div>', unsafe_allow_html=True)
    st.write("""
    **Aplikasi ini dikembangkan sebagai media edukatif dan simulatif dalam pengolahan limbah industri.**

    - Dibuat dengan: Python + Streamlit  
    - Pengembang: [Nama Kamu]  
    - Versi: 1.0  
    - Sumber data: Modul Teknik Lingkungan, Litbang KLHK  
    """)
