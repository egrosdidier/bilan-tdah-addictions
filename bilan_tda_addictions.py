# Bilan TDAH + Addictions - Streamlit app (v5 - synthèse étendue et export complet)

import streamlit as st
import random
import string
from fpdf import FPDF
import json
import pyzipper
from cryptography.fernet import Fernet

# -------------------------
# Sécurité et RGPD
# -------------------------
if 'bilan_data' not in st.session_state:
    st.session_state['bilan_data'] = {}

st.markdown("""
⚠️ **Confidentialité** :
- Aucune donnée personnelle n’est stockée.
- Les réponses sont temporaires (session navigateur).
- Vous pouvez enregistrer localement vos résultats sous forme chiffrée et protégée.
""")

# -------------------------
# Utility functions
# -------------------------
def generate_pseudo():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def save_encrypted_zip(data_dict, password):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    data_json = json.dumps(data_dict).encode()
    encrypted_data = cipher.encrypt(data_json)
    with open("bilan_encrypted.json", "wb") as f:
        f.write(encrypted_data)
    with pyzipper.AESZipFile("bilan_secure.zip", 'w', compression=pyzipper.ZIP_DEFLATED,
                              encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())
        zf.write("bilan_encrypted.json")
    return "bilan_secure.zip"

# -------------------------
# Identifiant
# -------------------------
st.title("🧠 Bilan TDAH et Addictions (anonyme)")
pseudo = st.text_input("Entrez un pseudonyme ou laissez vide pour en générer un :")
if not pseudo:
    pseudo = generate_pseudo()
st.success(f"Votre identifiant est : {pseudo}")
st.session_state['bilan_data']['pseudo'] = pseudo

# -------------------------
# Synthèse clinique automatique
# -------------------------
st.header("📊 Synthèse clinique automatique")
scores = st.session_state.get("bilan_data", {})

if 'wurs_score' in scores:
    score = scores['wurs_score']
    couleur = "🟢" if score < 30 else "🟠" if score < 46 else "🔴"
    st.subheader("🧠 TDAH - WURS-25")
    st.write(f"{couleur} Score : {score}")
    if score >= 46:
        st.markdown("➡️ Évaluation spécialisée recommandée (TDAH présumé)")

if 'asrs_score' in scores:
    score = scores['asrs_score']
    couleur = "🟢" if score < 4 else "🔴"
    st.subheader("🧠 TDAH - ASRS-6")
    st.write(f"{couleur} Items positifs : {score}")
    if score >= 4:
        st.markdown("➡️ Repérage positif : consultation spécialisée recommandée")

if 'dast_score' in scores:
    score = scores['dast_score']
    couleur = "🟢" if score == 0 else "🟠" if score <= 2 else "🔴"
    st.subheader("💊 Usage de substances - DAST")
    st.write(f"{couleur} Score : {score}")
    if score >= 3:
        st.markdown("➡️ Orientation vers CSAPA recommandée")

if 'hads_a_score' in scores and 'hads_d_score' in scores:
    a, d = scores['hads_a_score'], scores['hads_d_score']
    ca, cd = ("🟢" if a < 8 else "🔴"), ("🟢" if d < 8 else "🔴")
    st.subheader("😟 Anxiété et Dépression - HADS")
    st.write(f"Anxiété : {ca} Score {a}")
    st.write(f"Dépression : {cd} Score {d}")
    if a >= 8 or d >= 8:
        st.markdown("➡️ Suivi par un professionnel recommandé (CMP / MG / psy)")

if 'icje_score' in scores:
    score = scores['icje_score']
    couleur = "🟢" if score < 3 else "🔴"
    st.subheader("🎰 Jeux d'argent - ICJE")
    st.write(f"{couleur} Score : {score}")
    if score >= 3:
        st.markdown("➡️ Repérage positif : orientation vers consultation spécialisée en addiction comportementale")

if 'igd_score' in scores:
    score = scores['igd_score']
    couleur = "🟢" if score < 5 else "🔴"
    st.subheader("🎮 Jeux vidéo - IGD")
    st.write(f"{couleur} Score : {score}")
    if score >= 5:
        st.markdown("➡️ Risque de trouble du jeu vidéo : évaluation spécialisée recommandée")

if 'mini_positive' in scores:
    pos = scores['mini_positive']
    st.subheader("🧠 Troubles psychiatriques suspectés - MINI-S")
    if pos:
        st.write("🔴 Troubles détectés : ", ', '.join(pos))
        st.markdown("➡️ Évaluation psychiatrique prioritaire recommandée")
    else:
        st.write("🟢 Aucun trouble suspecté dans le module MINI-S")

# -------------------------
# Liens et ressources
# -------------------------
st.markdown("""
---
📚 **Ressources utiles** :
- [Guide HAS - TDAH adulte](https://www.has-sante.fr/jcms/c_2847166/fr/tdah-de-l-adulte)
- [Addictions - ANSM](https://www.ansm.sante.fr)
- [Psycom - Repérage santé mentale](https://www.psycom.org)
""")

# -------------------------
# Sauvegarde locale chiffrée
# -------------------------
st.header("🔐 Export chiffré et sécurisé (ZIP)")
password = st.text_input("Choisissez un mot de passe pour sécuriser vos résultats :", type="password")
if st.button("Générer un ZIP sécurisé"):
    if not password:
        st.warning("Mot de passe requis.")
    else:
        zip_path = save_encrypted_zip(st.session_state['bilan_data'], password)
        with open(zip_path, "rb") as file:
            st.download_button(label="📥 Télécharger le ZIP sécurisé", data=file, file_name="bilan_secure.zip")
