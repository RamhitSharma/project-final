import os
import pickle
from re import X
import streamlit as st 
from streamlit_option_menu import option_menu


#set page configuration
st.set_page_config(page_title=" MULTIPLE CANCER DISEASE",layout="wide")

#seting the working directory of the main.py
working_dir=os.path.dirname(os.path.abspath(__file__))

#loading the saved model

lung_cancer_disease_model=pickle.load(open(f'{working_dir}/lung_cancer_disease_model.sav','rb'))
breast_cancer_disease_model=pickle.load(open(f'{working_dir}/breast_cancer_disease_model.sav','rb'))
protest_cancer_disease_model=pickle.load(open(f'{working_dir}/protest_cancer_disease_model.sav','rb'))

#sideabar for navigation
with st.sidebar:
     selected=option_menu('Multiple Cancer Disease Prediction System',['Lung Cancer Prediction','Breast Cancer Prediction','Prostate Cancer Prediction'],menu_icon='hospital-fill',default_index=0)

#Lung cancer Prediction page
# YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC DISEASE,FATIGUE ,ALLERGY ,WHEEZING,ALCOHOL CONSUMING,COUGHING,SWALLOWING DIFFICULTY,CHEST PAIN,LUNG_CANCER

if selected == 'Lung Cancer Prediction':
  #page title
  st.title('Lung Cancer Prediction Using ML')

  #setting up the number of pages
  col1,col2,col3=st.columns(3)

  with col1:
    YELLOW_FINGERS=st.text_input('YELLOW_FINGERS')
  with col2:
    ANXIETY=st.text_input('ANXIETY')
  with col3:
    PEER_PRESSURE=st.text_input('PEER_PRESSURE')
  with col1:
    CHRONIC_DISEASE=st.text_input('CHRONIC_DISEASE')
  with col2:
    FATIGUE =st.text_input('FATIGUE ')
  with col3:
    ALLERGY=st.text_input('ALLERGY')

  with col1:
   WHEEZING=st.text_input('WHEEZING')
  with col2:
    ALCOHOL_CONSUMING=st.text_input('ALCOHOL CONSUMING')
  with col3:
    COUGHING=st.text_input('COUGHING')
  with col1:
    SWALLOWING_DIFFICULTY=st.text_input('SWALLOWING DIFFICULTY')
  with col2:
    CHEST_PAIN=st.text_input('CHEST_PAIN')
  with col3:
    ANXYELFIN=st.text_input('ANXYELFIN')


 #code for Prediction
  diab_diagnosis=[]

  #creation of the button
  if st.button('Lung cancer Test Result'):
      user_input=[YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE ,ALLERGY ,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SWALLOWING_DIFFICULTY,CHEST_PAIN,ANXYELFIN ]
      user_input=[float(x) for x in user_input]
      daib_prediction=lung_cancer_disease_model.predict([user_input])
      if daib_prediction[0]==1:
            diab_diagnosis='the person is positive'
      else:
            diab_diagnosis='the person is negative'
  st.success(diab_diagnosis)

#breast cancer Prediction page
if selected == 'Breast Cancer Prediction':
  #page title
  st.title('Breast Cancer Prediction Using ML')

  #setting up the number of pages
  col1,col2,col3,col4=st.columns(4)

  with col1:
    radius_mean=st.text_input('radius_mean')
  with col2:
    texture_mean=st.text_input('texture_mean')
  with col3:
    perimeter_mean=st.text_input('perimeter_mean')
  with col4:
    area_mean=st.text_input('area_mean')
  with col1:
    smoothness_mean=st.text_input('smoothness_mean')
  with col2:
    compactness_mean=st.text_input('compactness_mean')
  with col3:
    concavity_mean=st.text_input('concavity_mean')
  with col4:
    concave_points_mean=st.text_input('concave_points_mean')
  with col1:
    symmetry_mean=st.text_input('symmetry_mean')
  with col2:
   fractal_dimension_mean=st.text_input('fractal_dimension_mean')
  with col3:
    radius_se=st.text_input('radius_se')
  with col4:
    texture_se=st.text_input('texture_se')
  with col1:
    perimeter_se=st.text_input('perimeter_se')
  with col2:
    area_se=st.text_input('area_se')
  with col3:
   smoothness_se=st.text_input('smoothness_se')
  with col4:
    compactness_se=st.text_input('compactness_se')
  with col1:
   concavity_se=st.text_input('concavity_se')
  with col2:
    concave_points_se=st.text_input('concave_points_se')
  with col3:
    symmetry_se=st.text_input('symmetry_se')
  with col4:
    fractal_dimension_se=st.text_input('fractal_dimension_se')
  with col1:
    radius_worst=st.text_input('radius_worst')
  with col2:
    texture_worst=st.text_input('texture_worst')
  with col3:
    perimeter_worst=st.text_input('perimeter_worst')
  with col4:
   area_worst=st.text_input('area_worst')
  with col1:
   smoothness_worst=st.text_input('smoothness_worst')
  with col2:
    compactness_worst=st.text_input('compactness_worst')
  with col3:
    concavity_worst=st.text_input('concavity_worst')
  with col4:
    concave_points_worst=st.text_input('concave_points_worst')
  with col1:
    symmetry_worst=st.text_input('symmetry_worst')
  with col2:
    fractal_dimension_worst=st.text_input('fractal_dimension_worst')


 #code for Prediction
  diab_diagnosis=[]

  #creation of the button
  if st.button('Breast cancer Test Result'):
      user_input=[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]
      user_input=[float(x) for x in user_input]
      daib_prediction=breast_cancer_disease_model.predict([user_input])
      if daib_prediction[0]==1:
            diab_diagnosis='the person is positive'
      else:
            diab_diagnosis='the person is negative'
  st.success(diab_diagnosis)


if selected == 'Prostate Cancer Prediction':
  # radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension
  #page title
  st.title('Prostate Cancer Prediction Using ML')

  #setting up the number of pages
  col1,col2,col3=st.columns(3)

  # with col1:
  #   diagnosis_result=st.text_input('diagnosis_result')
  with col1:
    radius=st.text_input('radius')
  with col2:
    texture=st.text_input('texture')
  with col3:
    perimeter=st.text_input('perimeter')
  with col1:
    area=st.text_input('area')
  with col2:
    smoothness=st.text_input('smoothness')
  with col3:
    compactness=st.text_input('compactness')
  with col1:
   symmetry=st.text_input('symmetry')
  with col2:
    fractal_dimension=st.text_input('fractal_dimension')


  #code for Prediction
  diab_diagnosis=[]

  #creation of the button
  if st.button('prostate cancer Test Result'):
      user_input=[radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension]
      user_input=[float(x) for x in user_input]
      daib_prediction=protest_cancer_disease_model.predict([user_input])
      if daib_prediction[0]==1:
            diab_diagnosis='the person is positive'
      else:
            diab_diagnosis='the person is negative'
  st.success(diab_diagnosis)