
import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos en Venta en EE.UU.')
st.header('Esta es una aplicación web interactiva construida con Streamlit que permite analizar un conjunto de datos de vehículos en venta en los Estados Unidos. La aplicación ofrece herramientas para visualizar datos a través de histogramas y gráficos de dispersión.')

# Crear casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla de verificación está seleccionada
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico de histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # Si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)




