# app.py

import streamlit as st
import seaborn as sns
import pandas as pd

st.title("🌸 Aperçu du Dataset Iris")

# Charger les données
df = sns.load_dataset("iris")

# Afficher le dataset
st.write("Voici les 5 premières lignes du dataset Iris :")
st.dataframe(df.head())

# Afficher des stats
st.write("Statistiques descriptives :")
st.write(df.describe())

# Filtrage
species = st.selectbox("Choisir une espèce :", df['species'].unique())
filtered_df = df[df['species'] == species]

st.write(f"Données filtrées pour l'espèce : {species}")
st.dataframe(filtered_df)
