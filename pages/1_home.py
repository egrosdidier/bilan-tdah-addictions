
import streamlit as st

# Initialisation des données en session
if 'bilan_data' not in st.session_state:
    st.session_state['bilan_data'] = {}

st.title("📝 Saisie des questionnaires - Bilan TDAH & Addictions")

# Identifiant pseudonyme
pseudo = st.text_input("Entrez un pseudonyme :", value=st.session_state['bilan_data'].get("pseudo", ""))
st.session_state['bilan_data']['pseudo'] = pseudo

# WURS-25
st.header("🧠 WURS-25")
wurs_score = 0
for i in range(25):
    item = f"Item WURS {i+1}"
    score = st.slider(item, 0, 4, 0, key=f"wurs_{i}")
    wurs_score += score
st.session_state['bilan_data']['wurs_score'] = wurs_score
st.write(f"Score total WURS : {wurs_score}")

# ASRS-6
st.header("📋 ASRS-6")
asrs_items = [
    "1. Difficultés à finir les détails d’un projet",
    "2. Difficultés à organiser les tâches",
    "3. Évite les tâches mentales soutenues",
    "4. Perd des choses nécessaires aux activités",
    "5. Est facilement distrait",
    "6. Oublie des rendez-vous, obligations"
]
asrs_score = 0
for i, item in enumerate(asrs_items):
    freq = st.selectbox(item, ["Jamais", "Rarement", "Parfois", "Souvent", "Très souvent"], key=f"asrs_{i}")
    if freq in ["Souvent", "Très souvent"]:
        asrs_score += 1
st.session_state['bilan_data']['asrs_score'] = asrs_score
st.write(f"Items positifs : {asrs_score}")

# DAST-10
st.header("💊 DAST-10")
dast_score = 0
for i in range(10):
    response = st.radio(f"DAST question {i+1}", ["Oui", "Non"], key=f"dast_{i}")
    if response == "Oui":
        dast_score += 1
st.session_state['bilan_data']['dast_score'] = dast_score
st.write(f"Score DAST : {dast_score}")

# HADS
st.header("😟 HADS")
hads_a_score = 0
hads_d_score = 0
for i in range(14):
    label = f"HADS Anxiété {i+1}" if i < 7 else f"HADS Dépression {i-6}"
    val = st.radio(label, ["Pas du tout", "Parfois", "Souvent", "Très souvent"], key=f"hads_{i}")
    score = ["Pas du tout", "Parfois", "Souvent", "Très souvent"].index(val)
    if i < 7:
        hads_a_score += score
    else:
        hads_d_score += score
st.session_state['bilan_data']['hads_a_score'] = hads_a_score
st.session_state['bilan_data']['hads_d_score'] = hads_d_score
st.write(f"Score HADS-A : {hads_a_score} / HADS-D : {hads_d_score}")

# ICJE
st.header("🎰 ICJE")
icje_score = 0
for i in range(8):
    val = st.radio(f"ICJE question {i+1}", ["Oui", "Non"], key=f"icje_{i}")
    if val == "Oui":
        icje_score += 1
st.session_state['bilan_data']['icje_score'] = icje_score
st.write(f"Score ICJE : {icje_score}")

# IGD
st.header("🎮 IGD")
igd_score = 0
for i in range(9):
    val = st.radio(f"IGD critère {i+1}", ["Jamais", "Parfois", "Souvent"], key=f"igd_{i}")
    if val == "Souvent":
        igd_score += 1
st.session_state['bilan_data']['igd_score'] = igd_score
st.write(f"Score IGD : {igd_score}")

# MINI-S (simplifiée)
st.header("🧠 MINI-S")
mini_positive = []
mini_items = ["Épisodes dépressifs", "Trouble panique", "TOC", "Psychose", "TSPT", "Addictions", "Trouble anxieux généralisé"]
for i, item in enumerate(mini_items):
    response = st.radio(f"{item} suspecté ?", ["Oui", "Non"], key=f"mini_{i}")
    if response == "Oui":
        mini_positive.append(item)
st.session_state['bilan_data']['mini_positive'] = mini_positive

st.success("✅ Données enregistrées en session. Rendez-vous sur l'onglet Synthèse.")
