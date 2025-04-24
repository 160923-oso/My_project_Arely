import pandas as pd
import plotly.express as px
import streamlit as st

st.header('datos de anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión') # crear otro botón
build_histogram = st.checkbox('Mostrar histograma')
build_scatter = st.checkbox('Mostrar gráfico de dispersión')
        
if hist_button: # al hacer clic en el botón

 st.header('Histograma de anuncios de venta de coches')

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: 
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # al hacer clic en el botón del gráfico de dispersión
    # escribir un mensaje
 st.header('Grafica de dispersion de anuncios de venta de coches')

build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_scatter: 
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True) #aqui va la otra grafica
