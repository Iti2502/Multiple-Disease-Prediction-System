import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open('heartdisease.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons.sav', 'rb'))


# sidebar for navigation
with st.sidebar:

    # option_menu parameters:
    # 1. Title of sidebar
    # 2. list of options to select from
    # default_index: the index of option you want to be selected by default when you open the page
    # here default_index=0 means when you run this code, then by default index=0 option i.e.
    # Diabetes Prediction would be selected
    # for default=1, Heart Disease Prediction would be selected by default
    # you can add bootstrap icons to these option titles
    # for icons you have to search bootstrap icons on browser and then mention the names of the icons you want as follows
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons = ['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction')

    # take inputs in the same order as you provide features to the predict function of model
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age')

    # code for prediction
    diab_diagnosis = ''

    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if(diab_prediction[0] == 1):
            diab_diagnosis = 'Person is diabetic'
        else:
            diab_diagnosis = 'Person is not diabetic'

    st.success(diab_diagnosis)

if(selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('sex')

    with col3:
        cp = st.text_input('cp')

    with col1:
        trestbps = st.text_input('trestbps')

    with col2:
        chol = st.text_input('chol')

    with col3:
        fbs = st.text_input('fbs')

    with col1:
        restecg = st.text_input('restecg')

    with col2:
        thalach = st.text_input('thalach')

    with col3:
        exang = st.text_input('exang')

    with col1:
        oldpeak = st.text_input('oldpeak')

    with col2:
        slope = st.text_input('slope')

    with col3:
        ca = st.text_input('ca')

    with col1:
        thal = st.text_input('thal')


    # code for prediction
    heart_diagnosis = ''

    # creating a button for prediction
    if st.button('Heart Diagnose Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            diab_diagnosis = 'Person is diabetic'
        else:
            diab_diagnosis = 'Person is not diabetic'

    st.success(heart_diagnosis)



if(selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Prediction')

    col1, col2, col3 = st.columns(3)

    # with col1:
    #     name = st.text_input('name')

    with col1:
        MDVP_FO = st.text_input('MDVP Fo(Hz)')

    with col2:
        MDVP_Fhi = st.text_input('MDVP Fhi(Hz)')

    with col3:
        MDVP_Flo = st.text_input('MDVP Flo(Hz)')

    with col1:
        MDVP_Jitter = st.text_input('MDVP Jitter(%)')

    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP Jitter(Abs)')

    with col3:
        MDVP_RAP = st.text_input('MDVP RAP')

    with col1:
        MDVP_PPQ = st.text_input('MDVP PPQ')

    with col2:
        Jitter_DDP = st.text_input('Jitter DDP')

    with col3:
        MDVP_Shimmer = st.text_input('MDVP Shimmer')

    with col1:
        MDVP_Shimmer_db = st.text_input('MDVP Shimmer(db)')

    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer APQ3')

    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer APQ5')

    with col1:
        MDVP_APQ = st.text_input('MDVP APQ')

    with col2:
        Shimmer_DDA = st.text_input('Shimmer DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    # with col3:
    #     status = st.text_input('status')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

    # code for prediction
    parkinsons_diagnosis = ''

    # creating a button for prediction
    if st.button('Parkinsons Diagnose Result'):
        parkinsons_prediction = parkinsons_model.predict(
            [[MDVP_FO, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_db, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = 'Person has parkinsons disease'
        else:
            parkinsons_diagnosis = 'Person does not have parkinsons disease'

    st.success(parkinsons_diagnosis)


















