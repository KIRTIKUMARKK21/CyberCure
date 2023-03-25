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

import pickle as pkl
st.write("""
# Do You Know How Secure Your Network Is!
""")

model = keras.models.load_model('model.h5',compile=False)
st.balloons()
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
        st.subheader(" Predicted Attack Class is: "+output_class)
        
        attacks={"DOS":['apache2','back','land','neptune','mailbomb','pod','processtable','smurf','teardrop','udpstorm','worm'],
                "R2L":['ftp_write','guess_passwd','httptunnel','imap','multihop','named','phf','sendmail','snmpgetattack','snmpguess','spy','warezclient','warezmaster','xlock','xsnoop'],
                "Probe":['ipsweep','mscan','nmap','portsweep','saint','satan'],
                "U2R":['buffer_overflow','loadmodule','perl','ps','rootkit','sqlattack','xterm']                
                }
        st.write("## Following are Possiblities of Attack Type ##")
        for j in attacks[output_class]:
            st.markdown("- " + j)
if st.button("Predict"):
    predict_class()