import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open ('saved_model.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model_loaded = data['model']
preprocessor_loaded = data['preprocess']

def show_predict_page():
    st.image("0_vz_yu4mZ6Y69XSZg.png")
    st.title('Customer Churning Prediction')
    
    text = """
    <div style='text-align: justify; font-family: "Times New Roman"'>
    The chosen model is constructed using a random forest algorithm, a powerful machine learning technique known for its generalization. This model is specifically designed to predict the likelihood of customer churn, which refers to the probability of customers discontinuing their services or subscriptions. By accurately forecasting which customers are at risk of churning, businesses can implement targeted retention strategies to proactively address potential issues, enhance customer satisfaction, and ultimately reduce churn rates.
    </div>
    """

    st.markdown(text, unsafe_allow_html=True)

    Senior_Citizen = (
        'Yes',
        'No'
    )
    
    Partner = (
        'Yes',
        'No'
    )

    Dependents = (
        'Yes',
        'No'
    )

    Internet_Service = (
        'Fiber optic',
        'DSL',
        'No'
    )

    Online_Security = (
        'Yes',
        'No',
        'No internet serice'
    )

    Online_Backup = (
        'Yes',
        'No',
        'No internet serice'
    )

    Device_Protection = (
        'Yes',
        'No',
        'No internet serice'
    )

    Tech_Support = (
        'Yes',
        'No',
        'No internet serice'
    )

    Streaming_TV = (
        'Yes',
        'No',
        'No internet serice'
    )

    Streaming_Movies = (
        'Yes',
        'No',
        'No internet serice'
    )

    Contract = (
        'Month-to-month',
        'One year',
        'Two year'
    )

    Paperless_Billing = (
        'Yes',
        'No'
    )

    Payment_Method = (
        'Bank transfer (automatic)',
        'Credit card (automatic)',
        'Electronic check',
        'Mailed check'
    )

    Tenure_Group = (
        '1-12',
        '13-24',
        '25-36',
        '37-48',
        '49-60',
        '61-72'
    )

    text = '''
    <div style='text-align: justify; font-family: "Times New Roman", sans-serif; font-weight: bold; font-size: 25px;'>
    Demographic Factors
    </div>
    '''
    st.markdown(text, unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    # col1.subheader('Senior Citizen')
    sc = col1.radio('Senior Citizen', Senior_Citizen, horizontal = True)
    part = col2.radio('Partner', Partner, horizontal = True)
    depens = col3.radio('Dependents', Dependents, horizontal = True)
    st.divider()

    text = '''
    <div style='text-align: justify; font-family: "Times New Roman", sans-serif; font-weight: bold; font-size: 25px;'>
    Service Factors
    </div>
    '''
    st.markdown(text, unsafe_allow_html=True)
    intser = st.radio('Internet Service', Internet_Service, horizontal = True)
    col1, col2= st.columns(2)
    onlsec = col1.radio('Online Security', Online_Security, horizontal = True)
    onlbackup = col2.radio('Online Backup', Online_Backup, horizontal = True)
    col1, col2 = st.columns(2)
    devprot = col1.radio('Device Protection', Device_Protection, horizontal = True)
    techsup = col2.radio('Tech Support', Tech_Support, horizontal = True)
    col1, col2 = st.columns(2)
    strTV = col1.radio('Streaming TV', Streaming_TV, horizontal = True)
    strMov = col2.radio('Streaming Movies', Streaming_Movies, horizontal = True)
    st.divider()

    text = '''
    <div style='text-align: justify; font-family: "Times New Roman", sans-serif; font-weight: bold; font-size: 25px;'>
    Payment Factors
    </div>
    '''
    st.markdown(text, unsafe_allow_html=True)
    col1, col2 = st.columns([2,1])
    ctrc = col1.radio('Contract', Contract, horizontal = True)
    pbill = col2.radio('Paperless Billing', Paperless_Billing, horizontal = True)
    paymtd = st.radio('Payment Methods', Payment_Method, horizontal = True)
    mthchg = st.slider('Monthly Charges', 0.00, 250.00, step = 0.01)
    totalchg = st.number_input('Total Charges', 0.00, step = 0.01)
    tenure_group = st.radio('Tenure Group', Tenure_Group, horizontal = True)

    ok = st.button('Predict')

    if ok:
        x_input = np.array([[sc, part, depens, intser, onlsec, onlbackup, devprot, techsup, strTV, strMov, ctrc, pbill, paymtd, mthchg, totalchg, tenure_group]])
        columns = ['Senior Citizen', 'Partner', 'Dependents', 'Internet Service', 'Online Security', 'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 'Contract', 'Paperless Billing', 'Payment Method', 'Monthly Charges', 'Total Charges', 'Tenure Group']
        new_x = pd.DataFrame(x_input, columns=columns)

        x_input_preprocessed = preprocessor_loaded.transform(new_x)

        y_predict = model_loaded.predict(x_input_preprocessed)

        if y_predict == 1:
            st.error(f'The customer is predicted to be churned \U0001F641\U0001F641\U0001F641')
        else:
            st.success(f'The customer is predicted not to be churned \U0001F60A\U0001F60A\U0001F60A')
        