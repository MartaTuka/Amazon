import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#configuracion
st.set_page_config(page_title="App de prueba", page_icon=":smiley:", layout="centered")
st.image("https://th.bing.com/th/id/OIP.7AoR9Fsi36vZUhl9aqx0wAHaEK?rs=1&pid=ImgDetMain", width=100)
st.title("App de prueba")

#contenido de texto
st.write("Hola, esta es una app de prueba para Streamlit")

#contenido de texto con markdown
st.markdown("## Este es un título de nivel 2")

#sidebar
st.sidebar.title("Menú lateral")
st.sidebar.image("https://th.bing.com/th/id/OIP.7AoR9Fsi36vZUhl9aqx0wAHaEK?rs=1&pid=ImgDetMain", width=200)

#ejemplo de carga de un df
df = pd.read_csv('amazon_product.csv')
st.dataframe(df)

#columnas
columna1, columna2, columna3 = st.columns(3)
with columna1:
    st.write("Columna 1")
with columna2:
    st.image("https://th.bing.com/th/id/OIP.7AoR9Fsi36vZUhl9aqx0wAHaEK?rs=1&pid=ImgDetMain", width=100)
with columna3:
    st.write("Columna 3")

#secciones 
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

