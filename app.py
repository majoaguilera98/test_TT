import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Resultados de cierres de ventas 2025")

up_data = pd.read_csv('Apalabrado_2025_06_10.csv', skiprows=1) # leer los datos se puso .. para buscar el documento en una carpeta arriba
 

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    st.write('Creación de un histograma de distribución de importe de las ventas que van en el 2025')

    # crear un histograma
    fig = px.histogram(up_data, x="Importe", nbins=10, title="Distribución del Importe")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_lineplot = st.checkbox('Grafico de dispersión importe vs m2 up')

if build_lineplot:
    st.write('Creacion de grafico de dispresión del importe vs m2 de las unidades')
    fig2 = px.scatter(up_data, x="M2 de Unidad.", y="Importe", title="Importe vs. M2 de Unidad")
    st.plotly_chart(fig2, use_container_width=True)