# 🦠 Predictive Food Microbiology Simulator

Un simulateur interactif développé en Python pour modéliser la cinétique de croissance microbienne dans les aliments à l'aide du **modèle de Gompertz**.

## 📌 Description du Projet
Cette application permet aux microbiologistes et chercheurs en sécurité alimentaire de prédire la croissance bactérienne en fonction de plusieurs paramètres clés :
- **N₀** : Population bactérienne initiale ($\log_{10} \text{CFU/g}$)
- **Nₘₐₓ** : Population maximale atteinte
- **µₘₐₓ** : Taux de croissance spécifique maximal ($\text{h}^{-1}$)
- **λ** : Phase de latence ($\text{heures}$)

Le simulateur intègre également une ligne d'alerte pour le **seuil de sécurité microbiologique** ($6 \log_{10} \text{CFU/g}$).

---

## 🛠️ Technologies Utilisées
- **Python 3.10+**
- **Streamlit** : Interface utilisateur interactive
- **NumPy** : Calculs mathématiques
- **Matplotlib** : Génération de la courbe de croissance

---

## 🚀 Installation et Exécution Locale

1. **Cloner le dépôt :**

git clone https://github.com/maram-bahrouni/le-food-microbiology-predictor.git
cd le-food-microbiology-predictor
