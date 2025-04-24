import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Datos de anuncios de venta de coches')

st.write('En este proyecto, te proporcionamos un conjunto de datos de anuncios de venta de coches.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.dataframe(car_data)
hist_button = st.button('Histograma venta') # crear un botón
scatter_button = st.button('Gráfico de dispersión ventas') # crear otro botón
show_histogram = st.checkbox('Mostrar histograma modelos de coches')
show_scatter = st.checkbox('Mostrar gráfico de dispersión Condiciones de los carros de venta')
# Contar la frecuencia de cada tipo de coche
type_counts = car_data['type'].value_counts().reset_index()
type_counts.columns = ['type', 'count']  # Renombrar las columnas para mayor claridad
show_pie_chart = st.checkbox("Mostrar Gráfica Circular tipos de carros")

if hist_button: # al hacer clic en el botón

  st.header('Histograma de anuncios de venta de coches')

  st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
  fig = px.histogram(car_data, x="odometer", color="model")
        
    # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)

if scatter_button: # al hacer clic en el botón del gráfico de dispersión
    # escribir un mensaje
  st.header('Grafica de dispersion de anuncios de venta de coches MODELO VS PRECIO')

  st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches de acuerdo al modelo y precio')

    # crear un gráfico de dispersión
  fig_scatter = px.scatter(car_data, x="model", y="price", color="model")

    # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig_scatter, use_container_width=True) #aqui va la otra grafica

if show_histogram:
    st.header('Histograma de anuncios de Año del modelos con su condicion')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de los modelos de coches y su condicion')
    fig_hist = px.histogram(car_data, x="model_year", color="condition")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.header('Grafica de dispersion los condiciones de los coches')
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de venta de coches segun el tipo de coche')
    fig_scatter = px.scatter(car_data, x="condition", y="price" , color="condition")
    st.plotly_chart(fig_scatter, use_container_width=True)
    # --- Crear la gráfica circular ---
def create_pie_chart(data):
    """
    Crea una gráfica circular interactiva que muestra la distribución de los tipos de coches.

    Args:
         data (pd.DataFrame): Un DataFrame con columnas 'type' y 'count'.

    Returns:
        plotly.graph_objects.Figure: Una figura de Plotly que representa la gráfica circular.
    """
    fig = px.pie(
        data,
        names='type',       # Columna para los nombres de las porciones
        values='count',     # Columna para los valores de las porciones
        title='Distribución de Tipos de Coche', # Título de la gráfica
        color='type',       # Columna para asignar colores a las porciones
        color_discrete_sequence=px.colors.qualitative.Set1, # Paleta de colores
        hover_data=['count'],  # Información adicional al pasar el mouse
    )
    fig.update_traces(
        textposition='inside',      # Posición de las etiquetas de texto dentro de las porciones
        textinfo='percent+label',  # Mostrar porcentaje y etiqueta en las porciones
    )
    return fig

# Mostrar la gráfica usando Streamlit
st.header('Gráfica Circular de Tipos de Coche')
st.write('Esta gráfica muestra la distribución de los diferentes tipos de coches en el conjunto de datos.')

show_pie_chart = st.checkbox("Mostrar Gráfica Circular tipos de carros")

if show_pie_chart:
    pie_chart = create_pie_chart(type_counts)
    st.plotly_chart(pie_chart, use_container_width=True)
else:
    st.write("Selecciona la casilla para ver la gráfica circular.")
