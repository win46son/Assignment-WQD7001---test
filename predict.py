import streamlit as st
from model import show_predict_page
from explore import show_explore_page, show_churn_reasons, show_service_factors, show_high_corr

text = """
    <div style='text-align: justify; font-family: "Amasis MT Pro Black", sans-serif; font-weight: bold; font-size: 25px;'>
    CHURN SHIELD
    </div>
"""
st.sidebar.markdown(text, unsafe_allow_html=True)
page = st.sidebar.selectbox('Prediction or Exploration', ('Prediction','Exploration'))

if page == 'Prediction':
    show_predict_page()
elif page == 'Exploration':
    show_explore_page()
    choice = st.sidebar.selectbox('Sector:',('All','Main Churn Reasons', 'Service Factors','Dummy Correlation'))
    if choice == 'All':
        show_churn_reasons()
        st.divider()
        show_service_factors()
        st.divider()
        show_high_corr()
    elif choice == 'Main Churn Reasons':
        show_churn_reasons()
    elif choice == 'Service Factors':
        show_service_factors()
    else:
        show_high_corr()