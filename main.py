import streamlit as st
import numpy as np

st.title("🎉 Hello Amazing App!")
st.write("Ceci est une app Streamlit simple.")
st.line_chart(np.random.randn(20, 3), use_container_width=True)
