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
## Check Your Android App,Is It Malacious!
""")


model = keras.models.load_model('model.h5',compile=False)

st.write("Fill the Following Form with values 1 or 0 according to your Choice")
test_data=[]
labels=['android.permission.INTERNET', 'android.permission.READ_PHONE_STATE', 'android.permission.ACCESS_NETWORK_STATE', 'android.permission.WRITE_EXTERNAL_STORAGE', 'android.permission.ACCESS_WIFI_STATE', 'android.permission.READ_SMS', 'android.permission.WRITE_SMS', 'android.permission.RECEIVE_BOOT_COMPLETED', 'android.permission.ACCESS_COARSE_LOCATION', 'android.permission.CHANGE_WIFI_STATE']

    # if(val1==1 or val1==0):
    #     input.append(val1)
    # else:
    #     st.write("Enter Correct Value")
    #     break;
# print(test_data)
# def find_output(test_data):
#     res=model.predict(test_data)
#     return res


# if(len(test_data)==10):
#     print(find_output(test_data))    
# if(len(test_data)==10):    
#     res=model.predict(test_data)
#     print(res)

with st.form(key='my_form'):
    for j in labels:
        text_input = st.text_input(label=j)
        if(text_input!=""):
            test_data.append(int(text_input))
    submit_button = st.form_submit_button(label='Submit')
    # print(test_data)
    if(submit_button):
        # print(test_data)
        test_data=np.array(test_data)
        test_data=test_data.reshape((1,10))
        print(test_data.shape)
        # test_data=np.array(test_data)
        # print(test_data)
        val=model.predict(test_data)
        if(val>=0.5):
            st.write("This app may be malicious")
        else:
            st.write("App is Safe")
        # st.write(model.predict(test_data))
    