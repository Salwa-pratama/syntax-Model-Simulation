import streamlit as st
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from components.text import text
from utils.run_simulation2 import run_simulation2
from utils.load_model import load_model
import numpy as np
import pandas as pd
# Simulasi kebijakan 3 variabel
def halaman2()  :

    # Custom text untuk mempermudah styling
    text('Simulasi kebijakan keuntungan toko 3 variabel', '#4ceb34', "50px")
    st.write("Gunakan slider untuk menguji skenario 'What-if'. ")
    text("Gunakan slider untuk menguji skenario 'What-if'", '#ffffff', "14px")

    # Definisi nilai baseline (Kondisi awal toko)
    baseline_iklan = 10
    baseline_diskon = 10
    baseline_cabang = 2

    st.markdown("### 🎛️ Variabel Kontrol (Intervensi)")
    col_slider1, col_slider2, col_slider3 = st.columns(3)
    with col_slider1:
        iklan_slider = st.slider("Anggaran Iklan (Juta)", 0, 50, value=baseline_iklan)
    with col_slider2:
        diskon_slider = st.slider("Besaran Diskon (%)", 0, 50, value=baseline_diskon)
    with col_slider3:
        jumlah_cabang = st.slider("Jumlah Cabang (0 - 10)", 0, 10, value=baseline_cabang)
    # load model
    model = load_model("./models/model2.pkl")
    baseline_input = np.array([[baseline_iklan, baseline_diskon, baseline_cabang]])
    baseline_pred = model.predict(baseline_input)[0]

    hasil_pred, delta = run_simulation2(iklan_slider, diskon_slider, jumlah_cabang, model, baseline_pred)




    st.divider()
    st.markdown("### 📊 Ringkasan Hasil Prediksi")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Kondisi Baseline", value=f"Rp {baseline_pred:.2f} Jt")
        
    with col2:
        st.metric(label="Prediksi Keuntungan (Intervensi)", value=f"Rp {hasil_pred:.2f} Jt", delta=f"{delta:.2f} Jt")
        
    with col3:
        if delta < 0:
            st.error(f"⚠️ Skenario ini menghasilkan kerugian sebesar Rp {abs(delta):.2f} Jt dari baseline.")
        elif delta > 0:
            st.success(f"✅ Skenario ini menghasilkan keuntungan ekstra sebesar Rp {delta:.2f} Jt dari baseline!")
        else:
            st.info("⚖️ Skenario ini tidak mengubah keuntungan (sama dengan baseline).")

    st.divider()
    st.markdown("### 📈 Visualisasi Perbandingan")
    data_plot = pd.DataFrame({
        'Skenario' : ['Baseline', "Intervensi"],
        'Keuntungan' : [baseline_pred, hasil_pred],
        "Warna" : ['#4ceb34', '#0068c9']
    })

    st.bar_chart(data=data_plot, x='Skenario', y='Keuntungan', color="Warna")
