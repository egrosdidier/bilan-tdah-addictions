# Bilan TDAH & Addictions - Application Streamlit

Cette application permet de réaliser un **bilan clinique anonyme et automatisé** à destination des patients présentant des troubles du spectre TDAH, des addictions (substances, jeux, jeux vidéo), et des comorbidités psychiatriques fréquentes.

## 🧩 Structure multipage

- `home.py` : saisie des questionnaires validés (WURS-25, ASRS-6, DAST-10, HADS, ICJE, IGD, MINI-S)
- `synthese.py` : synthèse clinique automatique avec feux tricolores et recommandations
- `.streamlit/config.toml` : thème clair + options serveur

## 🚀 Installation

1. Clonez ou téléchargez ce dépôt :
```bash
git clone <URL> bilan_app && cd bilan_app
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez l'application :
```bash
streamlit run home.py
```

## 🔐 Confidentialité

- Aucune donnée nominative stockée
- Pseudonymisation locale par identifiant
- Export optionnel chiffré (ZIP protégé par mot de passe)

## 🧠 Questionnaires intégrés

- **TDAH enfance** : WURS-25
- **TDAH adulte** : ASRS-6
- **Addictions** : DAST-10, ASSIST (simplifié), ICJE (jeu), IGD (jeu vidéo)
- **Comorbidités psy** : HADS, MINI-S (version courte)

## 📚 Références

- HAS : [Repérage du TDAH adulte](https://www.has-sante.fr/jcms/c_2847166/fr/tdah-de-l-adulte)
- ANSM : [Addictions et bon usage](https://www.ansm.sante.fr)
- Psycom : [Guide santé mentale](https://www.psycom.org)

---

Projet développé avec Streamlit pour les professionnels de santé et structures d’addictologie.
