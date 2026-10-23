import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from models import GompertzModel
from translations import TRANSLATIONS

# Configuration de la page
st.set_page_config(page_title="Predictive Food Microbiology", page_icon="🦠")

# Sélecteur de langue dans la barre latérale
st.sidebar.title("🌍 Language / Langue / اللغة")
selected_lang = st.sidebar.selectbox("Select Language", ["Français", "English", "العربية"])

# Charger le dictionnaire de la langue choisie
t = TRANSLATIONS[selected_lang]

# Titre et description dynamiques
st.title(t["title"])
st.write(t["subtitle"])

# Barre latérale avec paramètres dynamiques
st.sidebar.header(t["sidebar_title"])
N0 = st.sidebar.slider(t["n0_label"], 1.0, 5.0, 2.0, 0.1)
Nmax = st.sidebar.slider(t["nmax_label"], 5.0, 10.0, 8.5, 0.1)
mu_max = st.sidebar.slider(t["mumax_label"], 0.05, 1.5, 0.35, 0.05)
lag = st.sidebar.slider(t["lag_label"], 0.0, 20.0, 3.0, 0.5)
hours = st.sidebar.slider(t["hours_label"], 12, 120, 48)

# Calcul
t_time = np.linspace(0, hours, 200)
model = GompertzModel(N0=N0, Nmax=Nmax, mu_max=mu_max, lag=lag)
log_N = model.predict(t_time)

# Graphique avec légendes dynamiques (et correction de ccolor -> color)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(t_time, log_N, color='#2c3e50', linewidth=2.5, label=t["curve_label"])
ax.axhline(y=6.0, color='r', linestyle='--', label=t["threshold_label"])

ax.set_xlabel("Time (h)" if selected_lang == "English" else "Temps (heures)" if selected_lang == "Français" else "الوقت (ساعات)")
ax.set_ylabel("log10 (CFU/g)")
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()

st.pyplot(fig)