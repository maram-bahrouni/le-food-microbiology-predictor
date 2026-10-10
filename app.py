import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from models import GompertzModel

st.set_page_config(page_title="Predictive Food Microbiology", page_icon="🦠")

st.title("🦠 Simulateur de Croissance Microbienne")
st.write("Cet outil prédit la cinétique de croissance bactérienne dans les aliments à l'aide du modèle de Gompertz.")

# Barre latérale
st.sidebar.header("Paramètres de simulation")
N0 = st.sidebar.slider("Population initiale (log10 CFU/g)", 1.0, 5.0, 2.0, 0.1)
Nmax = st.sidebar.slider("Population maximale (log10 CFU/g)", 5.0, 10.0, 8.5, 0.1)
mu_max = st.sidebar.slider("Taux de croissance max µ_max (1/h)", 0.05, 1.5, 0.35, 0.05)
lag = st.sidebar.slider("Phase de latence λ (heures)", 0.0, 20.0, 3.0, 0.5)
hours = st.sidebar.slider("Durée de la simulation (heures)", 12, 120, 48)

# Calcul
t = np.linspace(0, hours, 200)
model = GompertzModel(N0=N0, Nmax=Nmax, mu_max=mu_max, lag=lag)
log_N = model.predict(t)

# Graphique
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(t, log_N, color='#2c3e50', linewidth=2.5, label='Modèle de Gompertz')
ax.axhline(y=6.0, color='r', linestyle='--', label='Seuil de sécurité (6 log10)')

ax.set_xlabel("Temps (heures)")
ax.set_ylabel("Population microbienne (log10 CFU/g)")
ax.set_title("Courbe de croissance microbienne prédictive")
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()

st.pyplot(fig)