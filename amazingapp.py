# amazing-app
import numpy as np
import streamlit as st

st.title("🎉 Hello Amazing App!")
st.write("Ceci est une app Streamlit simple.")
st.line_chart(np.random.randn(20, 3), use_container_width=True)
