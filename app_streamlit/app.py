import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Charger le modèle Random Forest entraîné avec SMOTE (à adapter selon votre modèle)

# Supposez que le modèle est sauvegardé sous 'rf_smote_model.pkl'
# Vous devez avoir sauvegardé le modèle avec joblib.dump(rf_smote, 'rf_smote_model.pkl')
model = joblib.load('../model/rf_smote_model.pkl')

st.title("Scoring de Crédit - Prédiction du Risque de Défaut")

st.markdown("""
Entrez les informations du client pour prédire le risque de défaut de paiement grave (**SeriousDlqin2yrs**).
""")

# Liste des variables d'entrée
input_features = [
    'RevolvingUtilizationOfUnsecuredLines',
    'age',
    'NumberOfTime30-59DaysPastDueNotWorse',
    'DebtRatio',
    'MonthlyIncome',
    'NumberOfOpenCreditLinesAndLoans',
    'NumberOfTimes90DaysLate',
    'NumberRealEstateLoansOrLines',
    'NumberOfTime60-89DaysPastDueNotWorse',
    'NumberOfDependents'
]

# Interface utilisateur pour chaque variable
user_input = {}
user_input['RevolvingUtilizationOfUnsecuredLines'] = st.number_input("Taux d'utilisation des crédits renouvelables (0-1)", min_value=0.0, max_value=10.0, value=0.2)
user_input['age'] = st.number_input("Âge", min_value=18, max_value=120, value=40)
user_input['NumberOfTime30-59DaysPastDueNotWorse'] = st.number_input("Nombre de retards 30-59j", min_value=0, max_value=100, value=0)
user_input['DebtRatio'] = st.number_input("Ratio d'endettement", min_value=0.0, max_value=100000.0, value=0.5)
user_input['MonthlyIncome'] = st.number_input("Revenu mensuel", min_value=0.0, max_value=1000000.0, value=3000.0)
user_input['NumberOfOpenCreditLinesAndLoans'] = st.number_input("Nombre de crédits ouverts", min_value=0, max_value=100, value=5)
user_input['NumberOfTimes90DaysLate'] = st.number_input("Nombre de retards 90j+", min_value=0, max_value=100, value=0)
user_input['NumberRealEstateLoansOrLines'] = st.number_input("Nombre de prêts immobiliers", min_value=0, max_value=100, value=1)
user_input['NumberOfTime60-89DaysPastDueNotWorse'] = st.number_input("Nombre de retards 60-89j", min_value=0, max_value=100, value=0)
user_input['NumberOfDependents'] = st.number_input("Nombre de personnes à charge", min_value=0, max_value=20, value=0)

# Préparer les données pour la prédiction
input_df = pd.DataFrame([user_input])

if st.button("Prédire le risque"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]
    if prediction == 1:
        st.error(f"⚠️ Risque élevé de défaut de paiement (probabilité: {proba:.2%})")
    else:
        st.success(f"✅ Faible risque de défaut de paiement (probabilité: {proba:.2%})")