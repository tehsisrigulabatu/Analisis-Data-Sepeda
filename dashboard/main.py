# mengimport library yang dibutuhkan
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# load dataset
day_df = pd.read_csv('day_clean.csv')
hour_df = pd.read_csv('hour_clean.csv')


# judul utama dan sidebar
st.title("Analisis Data Penyewaan Sepeda berdasarkan Jam dan Cuaca")
st.sidebar.header("Analisis Data Sepeda")

# menampilkan sidebar
with st.sidebar:
    st.image("https://png.pngtree.com/png-clipart/20220109/original/pngtree-vector-hand-drawn-bicycle-element-png-image_7030380.png") 
    option = st.selectbox(
        label="Pilih Analisis Data: ",
        options=('Analisis Jumlah Penyewa Berdasarkan Jam', 'Analisis Jumlah Penyewa Berdasarkan Cuaca')
    )
    
 #opsi yang ada pada sidebar beserta logikanya   
if option == 'Analisis Jumlah Penyewa Berdasarkan Jam':
    
    # Mengelompokkan data berdasarkan jam
    hourly_totals = hour_df.groupby('hr')['cnt'].sum()

    # Subjudul di Streamlit
    st.subheader('Visualisasi Penyewaan Sepeda per Jam')

    # Membuat Line Chart menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hourly_totals.index, hourly_totals.values, marker='o', linestyle='-', color='b')

    # Menambahkan detail pada plot
    ax.set_title('Total Penyewaan Sepeda per Jam (Semua Hari)', fontsize=14)
    ax.set_xlabel('Jam', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
    ax.set_xticks(range(0, 24))
    ax.grid(alpha=0.3)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    
    
    # menambah keterangan
    st.write("Dari diagram diatas dapat disimpulkan bahwa jam 17.00 adalah jam di mana penyewaan sepeda meningkat secara signifikan.")
    
elif option == 'Analisis Jumlah Penyewa Berdasarkan Cuaca':
    
    # Mengelompokkan data berdasarkan cuaca
    weather_totals = day_df.groupby(by="weathersit").agg({
    "cnt": "sum"

    }).sort_values(by="cnt", ascending=False)
    
    # Mengelompokkan data berdasarkan kategori cuaca
    weather_totals = day_df.groupby('weathersit')['cnt'].sum()

    # Judul di Streamlit
    st.subheader('Visualisasi Total Penyewaan Sepeda Berdasarkan Cuaca')

    # Membuat Bar Chart menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(weather_totals.index, weather_totals.values, color=['skyblue', 'orange', 'gray', 'red'])

    # Menambahkan detail pada chart
    ax.set_title('Total Penyewaan Sepeda Berdasarkan Cuaca', fontsize=14)
    ax.set_xlabel('Kategori Cuaca', fontsize=12)
    ax.set_ylabel('Total Penyewaan', fontsize=12)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(['Cerah', 'Mendung', 'Hujan Ringan/Salju'])

    # Menampilkan chart di Streamlit
    st.pyplot(fig)
    
    # menambah keterangan
    st.write("Dari diagram diatas dapat disimpulkan bahwa penyewaan sepeda paling banyak terjadi pada cuaca cerah.")
    
    
    
            