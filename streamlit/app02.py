import numpy as np
import streamlit as st
import matplotlib.pylab as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

n = 1000
np.random.seed(42)
x = np.linspace(0, 6, n)
X = np.linspace(0, 6, n)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + np.random.random(n) * 0.3

st.sidebar.markdown("## Controls")
st.sidebar.markdown("You can **change** the number of *estimators* and see it's impact on **AdaBoost's** performance")
n_est = st.sidebar.slider("n_est", min_value=1, max_value=5000, step=1)

@st.cache
def make_predictions(n_est):
    mod1 = DecisionTreeRegressor(max_depth=4)
    y1 = mod1.fit(X, y).predict(X)
    y2 = AdaBoostRegressor(mod1, n_estimators=n_est).fit(X, y).predict(X)
    return y1, y2

y1, y2 = make_predictions(n_est=n_est)

fig, ax = plt.subplots()
if st.sidebar.checkbox("Toggle ScatterChart"):
    ax = plt.scatter(x, y, alpha=0.1)
ax = plt.plot(x, y1, label="Just a tree")
ax = plt.plot(x, y2, label=f"AdaBoost-{n_est}")
plt.legend()

st.pyplot(fig)