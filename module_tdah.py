
import streamlit as st

st.title("🧩 Module Complémentaire TDAH")

if 'bilan_data' not in st.session_state:
    st.session_state['bilan_data'] = {}

# -----------------------------
# UPPS-P
# -----------------------------
st.header("🧠 UPPS-P (Impulsivité)")
st.markdown("Évalue cinq dimensions de l’impulsivité. Cotation : 1 (Pas du tout d’accord) à 4 (Tout à fait d’accord).")

upps_domains = ["Urgence négative", "Manque de préméditation", "Manque de persévérance", "Recherche de sensations", "Urgence positive"]
upps_scores = {domain: 0 for domain in upps_domains}
upps_counts = {domain: 0 for domain in upps_domains}

# Exemple abrégé (5 items par dimension)
for i, domain in enumerate(upps_domains):
    st.subheader(f"Dimension : {domain}")
    for j in range(5):
        val = st.slider(f"{domain} - item {j+1}", 1, 4, 1, key=f"upps_{i}_{j}")
        upps_scores[domain] += val
        upps_counts[domain] += 1

# Calcul score moyen
upps_averages = {k: round(v/upps_counts[k], 2) for k, v in upps_scores.items()}
st.session_state['bilan_data']['upps_scores'] = upps_averages
st.write("**Scores UPPS-P moyens par dimension :**", upps_averages)

# -----------------------------
# BRIEF-A
# -----------------------------
st.header("🧠 BRIEF-A (Fonctions exécutives perçues)")
st.markdown("Cotation : 1 (Jamais) à 3 (Souvent).")

brief_domains = ["Inhibition", "Flexibilité", "Contrôle émotionnel", "Initiative", "Mémoire de travail", "Planification", "Organisation", "Surveillance"]

brief_scores = {domain: 0 for domain in brief_domains}
brief_counts = {domain: 0 for domain in brief_domains}

# Exemple abrégé (3 items par domaine)
for i, domain in enumerate(brief_domains):
    st.subheader(f"Fonction : {domain}")
    for j in range(3):
        val = st.slider(f"{domain} - item {j+1}", 1, 3, 1, key=f"brief_{i}_{j}")
        brief_scores[domain] += val
        brief_counts[domain] += 1

brief_averages = {k: round(v/brief_counts[k], 2) for k, v in brief_scores.items()}
st.session_state['bilan_data']['brief_scores'] = brief_averages
st.write("**Scores BRIEF-A moyens par fonction :**", brief_averages)

# -----------------------------
# WFIRS
# -----------------------------
st.header("🧠 WFIRS (Retentissement fonctionnel)")
st.markdown("Évalue le retentissement du TDAH dans différents domaines. Cotation : 0 (Pas du tout) à 3 (Sévère).")

wfirs_domains = ["Vie familiale", "Travail / études", "Vie sociale", "Estime de soi", "Activités à risque", "Fonctionnement quotidien"]
wfirs_scores = {domain: 0 for domain in wfirs_domains}
wfirs_counts = {domain: 0 for domain in wfirs_domains}

# Exemple abrégé (4 items par domaine)
for i, domain in enumerate(wfirs_domains):
    st.subheader(f"Domaine : {domain}")
    for j in range(4):
        val = st.slider(f"{domain} - item {j+1}", 0, 3, 0, key=f"wfirs_{i}_{j}")
        wfirs_scores[domain] += val
        wfirs_counts[domain] += 1

wfirs_averages = {k: round(v/wfirs_counts[k], 2) for k, v in wfirs_scores.items()}
st.session_state['bilan_data']['wfirs_scores'] = wfirs_averages
st.write("**Scores WFIRS moyens par domaine :**", wfirs_averages)
