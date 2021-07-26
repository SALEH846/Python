import streamlit as st
import numpy as np
import matplotlib.pylab as plt

st.title("Simulation[tm]")
st.write("This is our most important Simulation!")

st.sidebar.markdown("## Controls")
st.sidebar.markdown("You can **change** the values to change the *chart*")
x = st.sidebar.slider("Slope", min_value=0.01, max_value=0.10, step=0.01)
y = st.sidebar.slider("Noise", min_value=0.01, max_value=0.10, step=0.01)

st.write(f"Slope = {x}  Noise = {y}")

values = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)

# Plotting using streamlit's line_chart method
# st.line_chart(values)

# Plotting using matplotlib
fig, ax = plt.subplots()
for i in range(values.shape[1]):
    ax = plt.plot(values[:, i])
plt.title(f"Slope = {x}  Noise = {y}")
st.pyplot(fig)

# To run this app type "streamlit run <path to Application>" in terminal