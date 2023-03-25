import streamlit as st
import pandas as pd
import streamlit as st
from datetime import date,timedelta
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from keras.models import load_model
import tensorflow
from streamlit_option_menu import option_menu
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import pickle as pkl
st.write("""
# Do You Know How Secure Your Network Is!
""")

model = keras.models.load_model('model.h5',compile=False)
# st.balloons()
protocol_type_le = LabelEncoder()
service_le = LabelEncoder()
flag_le = LabelEncoder()

std_scaler = StandardScaler()
def standardization(df,col):
    for i in col:
        arr = df[i]
        arr = np.array(arr)
        df[i] = std_scaler.fit_transform(arr.reshape(len(arr),1))
    return df
url = "https://github.com/ahlashkari/CICFlowMeter"
st.write("Get CSV file from Network traffic flow generator Genereated By CICFlowMeter [link]({url})".format(url=url))


from selenium import webdriver
from bs4 import BeautifulSoup

# def get_data(search_input):
#     search_input = search_input.replace(" ","+")
#     webdriver.get("https://www.google.com/search?q=" + search_input)
#     soup = BeautifulSoup(webdriver.page_source,'lxml')
#     for result in soup.select('h3.r'):
#         item = result.select("a")[0].text
#         link = result.select("a")[0]['href']
#         print("item_text: {}\nitem_link: {}".format(item,link))
#         break

def search_on_google(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    return url
uploaded_file = st.file_uploader("Upload CSV File From CICFlowMeter", type=["csv"])
def predict_class():
    if uploaded_file is not None:
        data1 = pd.read_csv(uploaded_file)
        data1.drop(['Unnamed: 0'],axis=1,inplace=True)
        
        data1.drop(['difficulty'],axis=1,inplace=True)
        
        data1.drop(['label'], axis=1, inplace=True)

        numeric_col = data1.select_dtypes(include='number').columns
        data1 = standardization(data1,numeric_col)
        data1['protocol_type'] = protocol_type_le.fit_transform(data1['protocol_type'])
        data1['service'] = service_le.fit_transform(data1['service'])
        data1['flag'] = flag_le.fit_transform(data1['flag'])
        data1=np.array(data1)
        data1 = np.reshape(data1, ( data1.shape[0], 1 , data1.shape[1] ))
        data1 = np.asarray(data1).astype(np.float32)
        class_names=["DOS","Normal","Probe","R2L","U2R"]
        pred=model.predict(data1)
        output_class=class_names[np.argmax(pred)]
        
        d={"DOS":"Denial of service or DoS describes the ultimate goal of a class of cyber attacks designed to render a service inaccessible. The DoS attacks that most people have heard about are those launched against high profile websites, since these are frequently reported by the media.",
           "R2L":"Remote to user (R2L) is one type of computer network attacks, in which an intruder sends set of packets to another computer or server over a network where he/she does not have permission to access as a local user.",
           "U2R":"User to root attacks (U2R) is a second type of attack where the intruder tries to access the network resources as a normal user."}
        st.subheader(" Predicted Attack Class is: "+output_class)
        st.write(d[output_class])
        
        attacks={"DOS":['apache2','back','land','neptune','mailbomb','pod','processtable','smurf','teardrop','udpstorm','worm'],
                "R2L":['ftp_write','guess_passwd','httptunnel','imap','multihop','named','phf','sendmail','snmpgetattack','snmpguess','spy','warezclient','warezmaster','xlock','xsnoop'],
                "Probe":['ipsweep','mscan','nmap','portsweep','saint','satan'],
                "U2R":['buffer_overflow','loadmodule','perl','ps','rootkit','sqlattack','xterm']                
                }
        st.write("## Following are Possiblities of Attack Type ##")
        for j in attacks[output_class]:
            # st.markdown("- " +j)
            url=search_on_google(j)
            st.write("- "+j+ " [link]({url})".format(url=url))
            # st.write(get_data(j))
if st.button("Predict"):
    predict_class()
