
import streamlit as st
import numpy as np
import pickle
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

iris = load_iris()

st.set_page_config(page_title="Iris Classifier", layout="centered")
st.title("🌸 Iris Flower Predictor")

# Inputs
sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 0.2)

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    class_name = iris.target_names[prediction]
    st.success(f"🌼 Predicted Iris class: **{class_name}**")

    # Plotting
    fig, ax = plt.subplots()
    for i, target_name in enumerate(iris.target_names):
        ax.scatter(
            iris.data[iris.target == i, 2],
            iris.data[iris.target == i, 3],
            label=target_name
        )
    ax.scatter(petal_length, petal_width, color="black", label="Your Input", s=100, edgecolors="white")
    ax.set_xlabel("Petal Length")
    ax.set_ylabel("Petal Width")
    ax.legend()
    st.pyplot(fig)
