import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Datos de anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión') # crear otro botón
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')
        
if hist_button: # al hacer clic en el botón

  st.header('Histograma de anuncios de venta de coches')

  st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
  fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)

if scatter_button: # al hacer clic en el botón del gráfico de dispersión
    # escribir un mensaje
  st.header('Grafica de dispersion de anuncios de venta de coches')

  st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
  fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig_scatter, use_container_width=True) #aqui va la otra grafica

if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de los modelos de coches')
    fig_hist = px.histogram(car_data, x="model")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de venta de coches segun el modelo')
    fig_scatter = px.scatter(car_data, x="model", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)