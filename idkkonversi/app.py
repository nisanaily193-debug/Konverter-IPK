import streamlit as st

# Mengatur judul aplikasi
st.title("Grade Checker Sederhana")

# Meminta input nilai dari pengguna
# min_value dan max_value digunakan untuk memandu input, 
# tetapi logika validasi masih dipertahankan
nilai = st.number_input(
    "Masukkan nilai Anda:", 
    min_value=0.0, 
    max_value=100.0, 
    value=50.0, # Nilai default
    step=0.1
)

# Tombol untuk menjalankan pengecekan
if st.button("Cek Nilai"):
    # Cek nilai tidak valid (di luar rentang 0-100)
    if nilai > 100 or nilai < 0:
        st.error("Nilai Anda **tidak valid** (di luar rentang 0-100)")
    # Cek Nilai A (85-100)
    elif nilai >= 85:
        st.success("Nilai Anda: **A** 🏆")
    # Cek Nilai B (70-84.99...)
    elif nilai >= 70:
        st.info("Nilai Anda: **B**")
    # Cek Nilai C (55-69.99...)
    elif nilai >= 55:
        st.warning("Nilai Anda: **C**")
    # Cek Nilai D (40-54.99...)
    elif nilai >= 40:
        st.write("Nilai Anda: **D**")
    # Sisanya adalah Nilai E (0-39.99...)
    else:
        st.error("Nilai Anda: **E** 😔")

st.markdown(
    """
    ---
    *Skema Penilaian: A (≥85), B (≥70), C (≥55), D (≥40), E (<40)*
    """

)
