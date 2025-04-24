import streamlit as st

st.set_page_config(page_title="Bilan TDAH & Addictions", layout="centered")

st.title("Bienvenue dans l'application Bilan TDAH & Addictions 🧠")

st.markdown("""
Cette application propose :
- Un bilan clinique TDAH adulte
- Une évaluation des addictions (substances et comportementales)
- Un repérage des comorbidités psychiatriques fréquentes

👉 Utilisez le menu à gauche pour accéder aux modules :
1. **Bilan initial**
2. **Module TDAH complémentaire**
3. **Synthèse automatique**

⚠️ Toutes les données sont pseudonymisées et non stockées.
""")

if st.button("Commencer le bilan"):
    st.switch_page("pages/1_home.py")  # Redirige vers la première page
