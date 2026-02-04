
# Imports
import streamlit as st
import polars as pl
import numpy as np
from streamlit_agraph import agraph, Node, Edge, Config 

# Streamlit UI Config
st.title('AlgoStudy')
st.write('Visualize sorting algorithms for studying, interview prep, and just for fun!')
st.sidebar.title('Graphical Comparisons')

# Data Generation
@st.cache_data
def load_data():
    # Create a Polars DataFrame from alg-data.CSV
    df = pl.read_csv('data/alg-data.csv')
    return df
df = load_data()
st.dataframe(df)

# Flowchart Visualization
st.header('Algorithm Selection Flowchart')
dot = graphviz.Digraph(comment='Sorting Algorithm Selection')
dot.node('A', 'Stable?')
dot.node('B', 'In-place?')
dot.node('C', 'Stable & In-place\n• Bubble Sort\n• Insertion Sort')
dot.node('D', 'Stable & Not In-place\n• Mergesort\n• Timsort\n• Tree Sort\n• Bucket Sort\n• Radix Sort\n• Counting Sort\n• Cubesort')
dot.node('E', 'Not Stable & In-place\n• Quicksort\n• Heapsort\n• Selection Sort\n• Shell Sort')
dot.edge('A', 'B', label='Yes')
dot.edge('A', 'C', label='No')
dot.edge('B', 'D', label='Yes')
dot.edge('B', 'E', label='No')
st.graphviz_chart(dot)

# Credits
st.markdown("---")
st.markdown("Graph visualization powered by [streamlit-agraph](https://github.com/ChrisChross/streamlit-agraph) by Christian Klose")

# UI Configuration

