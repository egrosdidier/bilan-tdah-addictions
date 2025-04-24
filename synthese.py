
import streamlit as st

st.title("📊 Synthèse clinique - Bilan TDAH & Addictions")

# Vérifier la présence des données
if 'bilan_data' not in st.session_state or not st.session_state['bilan_data']:
    st.warning("Aucune donnée de bilan disponible. Veuillez compléter les questionnaires.")
    st.stop()

data = st.session_state['bilan_data']

def afficher_bloc(titre, score, seuils, commentaires, reco):
    couleur = "🟢"
    for seuil, couleur_test in seuils:
        if score >= seuil:
            couleur = couleur_test
    st.subheader(f"{titre}")
    st.write(f"{couleur} Score : {score}")
    st.markdown(f"➡️ {commentaires.get(couleur, 'Interprétation non disponible')}")
    if couleur in reco:
        st.markdown(f"**Recommandation :** {reco[couleur]}")

# Synthèses classiques
if "wurs_score" in data:
    afficher_bloc(
        "🧠 TDAH enfance - WURS-25", data["wurs_score"],
        seuils=[(46, "🔴"), (30, "🟠")],
        commentaires={
            "🟢": "Peu évocateur.",
            "🟠": "Douteux. Surveiller ou réévaluer.",
            "🔴": "Évocateur d’un TDAH dans l’enfance."
        },
        reco={
            "🔴": "Évaluation TDAH spécialisée recommandée."
        }
    )

if "asrs_score" in data:
    afficher_bloc(
        "🧠 TDAH adulte - ASRS-6", data["asrs_score"],
        seuils=[(4, "🔴")],
        commentaires={
            "🟢": "Peu évocateur.",
            "🔴": "Repérage positif."
        },
        reco={
            "🔴": "Consulter un professionnel formé au TDAH adulte."
        }
    )

if "dast_score" in data:
    afficher_bloc(
        "💊 Usage de substances - DAST-10", data["dast_score"],
        seuils=[(3, "🔴"), (1, "🟠")],
        commentaires={
            "🟢": "Pas de repérage clinique.",
            "🟠": "Usage à risque modéré.",
            "🔴": "Repérage d’usage problématique."
        },
        reco={
            "🔴": "Orientation CSAPA conseillée."
        }
    )

if "hads_a_score" in data and "hads_d_score" in data:
    for type_score, score in zip(["Anxiété", "Dépression"], [data["hads_a_score"], data["hads_d_score"]]):
        couleur = "🔴" if score >= 8 else "🟢"
        st.subheader(f"😟 HADS - {type_score}")
        st.write(f"{couleur} Score : {score}")
        if couleur == "🔴":
            st.markdown("➡️ Présomption clinique. Suivi psychologique recommandé.")

if "icje_score" in data:
    afficher_bloc(
        "🎰 Jeu d'argent - ICJE", data["icje_score"],
        seuils=[(3, "🔴")],
        commentaires={
            "🟢": "Pas de repérage pathologique.",
            "🔴": "Repérage évocateur d’un trouble du jeu."
        },
        reco={
            "🔴": "Consultation spécialisée en addiction comportementale."
        }
    )

if "igd_score" in data:
    afficher_bloc(
        "🎮 Jeu vidéo - IGD", data["igd_score"],
        seuils=[(5, "🔴")],
        commentaires={
            "🟢": "Usage non problématique.",
            "🔴": "Critères remplis pour trouble du jeu vidéo probable."
        },
        reco={
            "🔴": "Orientation vers prise en charge comportementale."
        }
    )

if "mini_positive" in data:
    pos = data["mini_positive"]
    st.subheader("🧠 Troubles psychiatriques suspectés - MINI-S")
    if pos:
        st.write("🔴 Troubles détectés :", ", ".join(pos))
        st.markdown("➡️ Une évaluation psychiatrique spécialisée est recommandée.")
    else:
        st.write("🟢 Aucun trouble suspecté.")

# Synthèse avancée - UPPS-P
if "upps_scores" in data:
    st.header("🧠 Impulsivité - UPPS-P")
    for domaine, score in data["upps_scores"].items():
        st.write(f"🟦 {domaine} : {score}")

# Synthèse avancée - BRIEF-A
if "brief_scores" in data:
    st.header("🧠 Fonctions exécutives - BRIEF-A")
    for fonction, score in data["brief_scores"].items():
        st.write(f"🟪 {fonction} : {score}")

# Synthèse avancée - WFIRS
if "wfirs_scores" in data:
    st.header("🧠 Retentissement fonctionnel - WFIRS")
    for domaine, score in data["wfirs_scores"].items():
        st.write(f"🟨 {domaine} : {score}")

# Liens ressources
st.markdown("""
---
📚 **Ressources utiles** :
- [HAS - TDAH adulte](https://www.has-sante.fr/jcms/c_2847166/fr/tdah-de-l-adulte)
- [ANSM - Addictions](https://www.ansm.sante.fr)
- [Psycom - Orientation santé mentale](https://www.psycom.org)
""")
