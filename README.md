# iris-predictor-streamlit
# 🌸 Iris Flower Prediction App

This project is a **machine learning web application** built with **Streamlit** that predicts the species of an Iris flower (Setosa, Versicolor, or Virginica) based on user-input flower measurements.

## 🚀 Features

- Interactive sliders to input flower measurements:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- Predicts the Iris flower species using a trained Random Forest model.
- Displays a bar plot of the input features.

## 📊 Dataset

Uses the classic **Iris dataset** from `scikit-learn` containing:
- 150 samples
- 4 features (sepal & petal length/width)
- 3 target classes (Setosa, Versicolor, Virginica)

## 🧠 Model

- Algorithm: RandomForestClassifier
- Trained using scikit-learn
- Saved as `model.pkl` using pickle

## 📷 App Preview

Here's what the app looks like when you run it locally:

- A clean and interactive Streamlit interface
- Sliders for user input:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- A **Predict** button
- The predicted species of the Iris flower (Setosa, Versicolor, Virginica)
- A feature input **bar plot** showing all four values


## ▶️ How to Run

```bash
streamlit run app.py

After running, you’ll see a message like:

You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501

🔗 Open http://localhost:8501 in your browser to use the app!


