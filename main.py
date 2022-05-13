import streamlit as st
import pickle
import pandas as pd

PAGE_CONFIG = {"page_title": "Prediction of Medical Charges Billed by Insurance", "page_icon": "icon.png",
               "layout": "centered"}
st.set_page_config(**PAGE_CONFIG)
# st.title("Predict Medical charges billed by Insurance ")
from keras.models import load_model
model = load_model('my_model.h5')


def pred(src, dest, dayni):
    prediction = placed.predict([[src, dest, dayni]])
    prediction = float((prediction * (500-10)+10))
    return prediction


def binary_map(x):
    return x.map({'MGM': 0, 'Pochammaidan': 1, 'Kashibugga': 2, 'WGL BUS STAND': 3,
                  'WGL busstand': 4, 'WGL bus stop': 5, 'HNK petrol pump': 6,
                  'HNK Petrol pump': 7, 'HNK subedari': 8, 'Fathima': 9, 'K U X Road': 10,
                  'Kazipet': 11, 'Adalath': 12, 'Subedari': 13, 'H N K Chowrastha': 14,
                  'H N K busstand': 15, 'H N K subedari': 16, 'H N K Asubedari': 17,
                  'Muluguroad': 18, 'Warangal': 19, 'HNK': 20, 'Warangal frot road': 21,
                  'Hanamkonda': 22, 'HNK petrolpump': 23, 'Warangal busstand': 24,
                  'Warangal postoﬃce': 25, 'ku': 26, 'Shyamal gardens': 27, 'Jawaher cross': 28,
                  'Ku': 29, 'Church ': 30, 'Fatima ': 31, 'Shyamala gardens': 32, 'Deshaipet': 33,
                  'Market': 34, 'Gorrekunta': 35, 'Narsampet': 36, 'Bollikunta': 37, 'Shambunipet': 38,
                  'Geesugonda': 39, 'K U X road': 40, 'Madikonda': 41, 'H N K Busstand': 42,
                  'H N K Head postoﬃc e': 43, 'H N K busdepot': 44, 'Balasamudram': 45,
                  'WGL chowrastha': 46, 'Karimabad': 47, 'Wardhannapet': 48, 'Panthini': 49,
                  'Mogilicharla': 50, 'Koreekunta': 51, 'WGL fort road': 52, 'Naidupetrol pump': 53,
                  'Chinthagattu camp': 54, 'Peddamagadda': 55, 'Parkal': 56, 'Mulugu': 57,
                  'Mahabubabad': 58, 'Darmaram': 59, 'Vadeepalli': 60, 'Battalabajar': 61,
                  'Nagamaiah temple': 62, 'Under Bridge': 63, 'Gate': 64, 'Water Tank': 65,
                  'Greenwood': 66, 'Greenwood ': 67, 'CSR': 68, 'Sathyam convention': 69,
                  'Alluri Engineering': 70, 'Church': 71, 'Orugallu petrol pump': 72, 'Shyampet': 73,
                  'JSM': 74, 'Zoo': 75,
                  'Day': 0, 'Night': 1, 'Day ': 0})


def mainn():
    html_temp = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap" rel="stylesheet">
    <div style="background-color:rgb(108, 207, 133);opacity:0.9;padding:10px;border-radius:10px;font-family: 'Josefin Sans', sans-serif;">
    <h2 style="color:#fff;text-align:center;">Prediction of Medical Charges billed by Insurance</h2>
    </div>
    """

    html_temp1 = """
    <div style="background-color:black;opacity:0.8;padding:10px;border-radius:10px;font-family: 'Josefin Sans', sans-serif;">
    <h3 style="color:#fff;text-align:center;">Data Set of our M L Model</h3>
    </div>
    """

    html_temp2 = """
    <div style="background-color:black;border-radius:10px;opacity:0.7;font-family: 'Josefin Sans', sans-serif;">
    <h3 style="color:#fff;text-align:center;">Exploring the Dataset of our Problem Statement:</h3>
    </div>
    """
    details = st.sidebar.selectbox(label="HOME", options=['Web-App', 'Data'])
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.image('ii.png')
    if details == 'Web-App':
        st.markdown(html_temp, unsafe_allow_html=True)
        st.write("")
        st.write("This is an application to predict charges billed based on few parameters")
        st.write("")
        src = st.selectbox("Enter your Gender", options=['MGM', 'Pochammaidan', 'Kashibugga', 'WGL BUS STAND',
                                                         'WGL busstand', 'WGL bus stop', 'HNK petrol pump',
                                                         'HNK Petrol pump', 'HNK subedari', 'Fathima', 'K U X Road',
                                                         'Kazipet', 'Adalath', 'Subedari', 'H N K Chowrastha',
                                                         'H N K busstand', 'H N K subedari', 'H N K Asubedari',
                                                         'Muluguroad', 'Warangal', 'HNK', 'Warangal frot road',
                                                         'Hanamkonda', 'HNK petrolpump', 'Warangal busstand',
                                                         'Warangal postoﬃce', 'ku', 'Shyamal gardens', 'Jawaher cross',
                                                         'Ku', 'Church ', 'Fatima ', 'Shyamala gardens', 'Deshaipet',
                                                         'Market', 'Gorrekunta', 'Narsampet', 'Bollikunta',
                                                         'Shambunipet',
                                                         'Geesugonda', 'K U X road', 'Madikonda', 'H N K Busstand',
                                                         'H N K Head postoﬃc e', 'H N K busdepot', 'Balasamudram',
                                                         'WGL chowrastha', 'Karimabad', 'Wardhannapet', 'Panthini',
                                                         'Mogilicharla', 'Koreekunta', 'WGL fort road',
                                                         'Naidupetrol pump',
                                                         'Chinthagattu camp', 'Peddamagadda', 'Parkal', 'Mulugu',
                                                         'Mahabubabad', 'Darmaram', 'Vadeepalli', 'Battalabajar',
                                                         'Nagamaiah temple', 'Under Bridge', 'Gate', 'Water Tank',
                                                         'Greenwood', 'Greenwood ', 'CSR', 'Sathyam convention',
                                                         'Alluri Engineering', 'Church', 'Orugallu petrol pump',
                                                         'Shyampet',
                                                         'JSM', 'Zoo'])
        src = binary_map(src)
        dest = st.selectbox("Enter your Gender", options=['MGM', 'Pochammaidan', 'Kashibugga', 'WGL BUS STAND',
                                                         'WGL busstand', 'WGL bus stop', 'HNK petrol pump',
                                                         'HNK Petrol pump', 'HNK subedari', 'Fathima', 'K U X Road',
                                                         'Kazipet', 'Adalath', 'Subedari', 'H N K Chowrastha',
                                                         'H N K busstand', 'H N K subedari', 'H N K Asubedari',
                                                         'Muluguroad', 'Warangal', 'HNK', 'Warangal frot road',
                                                         'Hanamkonda', 'HNK petrolpump', 'Warangal busstand',
                                                         'Warangal postoﬃce', 'ku', 'Shyamal gardens', 'Jawaher cross',
                                                         'Ku', 'Church ', 'Fatima ', 'Shyamala gardens', 'Deshaipet',
                                                         'Market', 'Gorrekunta', 'Narsampet', 'Bollikunta',
                                                         'Shambunipet',
                                                         'Geesugonda', 'K U X road', 'Madikonda', 'H N K Busstand',
                                                         'H N K Head postoﬃc e', 'H N K busdepot', 'Balasamudram',
                                                         'WGL chowrastha', 'Karimabad', 'Wardhannapet', 'Panthini',
                                                         'Mogilicharla', 'Koreekunta', 'WGL fort road',
                                                         'Naidupetrol pump',
                                                         'Chinthagattu camp', 'Peddamagadda', 'Parkal', 'Mulugu',
                                                         'Mahabubabad', 'Darmaram', 'Vadeepalli', 'Battalabajar',
                                                         'Nagamaiah temple', 'Under Bridge', 'Gate', 'Water Tank',
                                                         'Greenwood', 'Greenwood ', 'CSR', 'Sathyam convention',
                                                         'Alluri Engineering', 'Church', 'Orugallu petrol pump',
                                                         'Shyampet',
                                                         'JSM', 'Zoo'])
        dest = binary_map(dest)
        smoke = st.selectbox("Do You Smoke: ", options=['Day', 'Night'])
        if smoke == 'Day':
            smoke = 0
        elif smoke == 'Night':
            smoke = 1
        result = ""
        if st.button("Predict"):
            result = pred(src, dest, smoke)
            st.write("Medical charge billed by insurance is {}".format(result))


if __name__ == '__main__':
    mainn()
