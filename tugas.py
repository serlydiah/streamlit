import streamlit as st
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt


def main():
    st.title("Aplikasi Uji T dan Uji Regresi")
    st.write("Selamat datang di aplikasi Uji T dan Uji Regresi Teman-Teman LOVE<3!")

    # Sidebar untuk memilih uji statistik
    st.sidebar.title("Pilih Uji Statistik")
    uji_statistik = st.sidebar.selectbox("Uji Statistik", ("Uji T", "Uji Regresi"))

    if uji_statistik == "Uji T":
        st.header("Uji T")
        st.write("Masukkan data dua kelompok yang akan diuji.")

        # Input data kelompok 1
        st.subheader("Kelompok 1")
        data1 = st.text_input("Masukkan data kelompok 1, dipisahkan oleh koma")

        # Input data kelompok 2
        st.subheader("Kelompok 2")
        data2 = st.text_input("Masukkan data kelompok 2, dipisahkan oleh koma")

        # Tombol untuk menjalankan uji T
        if st.button("Jalankan Uji T"):
            data1 = [float(x.strip()) for x in data1.split(",")]
            data2 = [float(x.strip()) for x in data2.split(",")]

            t_statistic, p_value = stats.ttest_ind(data1, data2)

            st.write("Hasil:")
            st.write(f"T-Statistic: {t_statistic}")
            st.write(f"P-Value: {p_value}")

    elif uji_statistik == "Uji Regresi":
        st.header("Uji Regresi")
        st.write("Masukkan data variabel X dan Y untuk analisis regresi.")

        # Input data X
        st.subheader("Variabel X")
        data_x = st.text_input("Masukkan data variabel X, dipisahkan oleh koma")

        # Input data Y
        st.subheader("Variabel Y")
        data_y = st.text_input("Masukkan data variabel Y, dipisahkan oleh koma")

        # Tombol untuk menjalankan analisis regresi
        if st.button("Jalankan Analisis Regresi"):
            data_x = [float(x.strip()) for x in data_x.split(",")]
            data_y = [float(x.strip()) for x in data_y.split(",")]

            slope, intercept, r_value, p_value, std_err = stats.linregress(data_x, data_y)

            st.write("Hasil:")
            st.write(f"Slope: {slope}")
            st.write(f"Intercept: {intercept}")
            st.write(f"R-Value: {r_value}")
            st.write(f"P-Value: {p_value}")
            st.write(f"Standard Error: {std_err}")

            # Plot data dan garis regresi
            plt.scatter(data_x, data_y)
            plt.plot(data_x, intercept + slope * np.array(data_x), 'r')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Analisis Regresi')
            st.pyplot(plt)


if __name__ == '__main__':
    main()
