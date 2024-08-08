
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer datos
st.header('Análisis de Datos de Vehículos en Venta en EE.UU.')

# Crear botón para construir un histograma
hist_button = st.button('Construir histograma')

# Al hacer clic en el botón del histograma
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico de histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear segundo botón para construir  gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Al hacer clic en el botón del gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", kind="scatter")
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)

    # crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    # Crear un histograma
    fig_hist1 = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico de histograma
    st.plotly_chart(fig_hist1, use_container_width=True)
