import streamlit as st
import pickle
import pandas as pd

PAGE_CONFIG = {"page_title": "Auto Charges", "page_icon": "icon.png",
               "layout": "centered"}
st.set_page_config(**PAGE_CONFIG)
# st.title("Predict Medical charges billed by Insurance ")
from keras.models import load_model
model = load_model('my_model.h5')


def pred(src, dest, dayni):
    list_of_columns = ['Source','Destination','Dayornight']
    input_data=pd.DataFrame(columns=list_of_columns)
    input_data.at[0,'Source']=src
    input_data.at[0, 'Destination'] = dest
    input_data.at[0, 'Dayornight'] = dayni
    prediction = model.predict(input_data)
    prediction = float((prediction * (500-10)+10))
    return input_data['Source']


def binary_map(x):
    if x=='MGM':
      x=0 
    elif x=='Pochammaidan': 
      x=1
    elif x=='Kashibugga': 
      x=2 
    elif x=='WGL BUS STAND': 
      x=3
    elif x=='WGL busstand': 
      x=4
    elif x=='WGL bus stop': 
      x=5
    elif x=='HNK petrol pump': 
      x=6
    elif x=='HNK Petrol pump': 
      x=7 
    elif x=='HNK subedari': 
      x=8
    elif x=='Fathima': 
      x=9
    elif x=='K U X Road': 
      x=10
    elif x=='Kazipet': 
      x=11 
    elif x=='Adalath': 
      x=12
    elif x=='Subedari': 
      x=13
    elif x=='H N K Chowrastha': 
      x=14
    elif x=='H N K busstand': 
      x=15
    elif x=='H N K subedari': 
      x=16
    elif x=='H N K Asubedari': 
      x=17
    elif x=='Muluguroad': 
      x=18
    elif x=='Warangal': 
      x=19
    elif x=='HNK': 
      x=20
    elif x=='Warangal frot road': 
      x=21
    elif x=='Hanamkonda': 
      x=22
    elif x=='HNK petrolpump': 
      x=23
    elif x=='Warangal busstand': 
      x=24
    elif x=='Warangal postoﬃce': 
      x=25 
    elif x=='ku': 
      x=26
    elif x=='Shyamal gardens': 
      x=27
    elif x=='Jawaher cross': 
      x=28
    elif x=='Ku': 
      x=29
    elif x=='Church ': 
      x=30
    elif x=='Fatima ': 
      x=31
    elif x=='Shyamala gardens': 
      x=32 
    elif x=='Deshaipet': 
      x=33
    elif x=='Market': 
      x=34 
    elif x=='Gorrekunta': 
      x=35 
    elif x=='Narsampet': 
      x=36 
    elif x=='Bollikunta': 
      x=37 
    elif x=='Shambunipet': 
      x=38
    elif x=='Geesugonda': 
      x=39
    elif x=='K U X road': 
      x=40
    elif x=='Madikonda': 
      x=41
    elif x=='H N K Busstand': 
      x=42
    elif x=='H N K Head postoﬃc e': 
      x=43
    elif x=='H N K busdepot': 
      x=44
    elif x=='Balasamudram': 
      x=45
    elif x=='WGL chowrastha': 
      x=46
    elif x=='Karimabad': 
      x=47
    elif x=='Wardhannapet': 
      x=48
    elif x=='Panthini': 
      x=49
    elif x=='Mogilicharla': 
      x=50 
    elif x=='Koreekunta': 
      x=51
    elif x=='WGL fort road': 
      x=52 
    elif x=='Naidupetrol pump': 
      x=53
    elif x=='Chinthagattu camp': 
      x=54
    elif x=='Peddamagadda': 
      x=55
    elif x=='Parkal': 
      x=56
    elif x=='Mulugu': 
      x=57
    elif x=='Mahabubabad': 
      x=58
    elif x=='Darmaram': 
      x=59
    elif x=='Vadeepalli': 
      x=60
    elif x=='Battalabajar': 
      x=61
    elif x=='Nagamaiah temple': 
      x=62 
    elif x=='Under Bridge': 
      x=63
    elif x=='Gate': 
      x=64 
    elif x=='Water Tank': 
      x=65
    elif x=='Greenwood': 
      x=66 
    elif x=='Greenwood ': 
      x=67
    elif x=='CSR': 
      x=68
    elif x=='Sathyam convention': 
      x=69
    elif x=='Alluri Engineering': 
      x=70
    elif x=='Church': 
      x=71
    elif x=='Orugallu petrol pump': 
      x=72
    elif x=='Shyampet': 
      x=73
    elif x=='JSM': 
      x=74 
    elif x=='Zoo': 
      x=75
    elif x=='Day': 
      x=0 
    elif x=='Night': 
      x==1 
    elif x=='Day ': 
      x==0
    return x

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
                                                         'Naidupetrol pump','Alluri Engineering', 'Church', 'Orugallu petrol pump',
                                                         'Shyampet',
                                                         'JSM', 
                                                         'Chinthagattu camp', 'Peddamagadda', 'Parkal', 'Mulugu',
                                                         'Mahabubabad', 'Darmaram', 'Vadeepalli', 'Battalabajar',
                                                         'Nagamaiah temple', 'Under Bridge', 'Gate', 'Water Tank',
                                                         'Greenwood', 'Greenwood ', 'CSR', 'Sathyam convention',
                                                         'Zoo'])
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
