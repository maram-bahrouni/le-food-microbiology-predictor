# 🧫 Predictive Food Microbiology Simulator

An interactive web application developed in Python to model microbial growth kinetics in food using the **Gompertz model**.

---

## 📌 Project Description
This application allows microbiologists and food safety researchers to predict bacterial growth based on several key parameters:
- **$N_0$** : Initial bacterial population ($\log_{10} \text{CFU/g}$)
- **$N_{\max}$** : Maximum population reached
- **$\mu_{\max}$** : Maximum specific growth rate ($\text{h}^{-1}$)
- **$\lambda$** : Lag phase ($\text{hours}$)

The simulator also includes an alert line for the **microbiological safety threshold** ($6 \log_{10} \text{CFU/g}$).

---

## 🛠️ Technologies Used
- **Python 3.10+**
- **Streamlit** : Interactive user interface
- **NumPy** : Mathematical calculations
- **Matplotlib** : Growth curve generation

---

## 🚀 Installation and Local Execution

1. **Clone the repository:**
```bash
git clone [https://github.com/maram-bahrouni/le-food-microbiology-predictor.git](https://github.com/maram-bahrouni/le-food-microbiology-predictor.git)
cd le-food-microbiology-predictor
