import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data():
    df = pd.read_excel('Telco_customer_churn.xlsx')
    df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors = 'coerce')
    df['Total Charges'].fillna(df['Tenure Months'] * df['Monthly Charges'], inplace = True)
    df["Churn Reason"].fillna("Not Churn", inplace = True)

    labels = ["{0}-{1}".format(i,i+11) for i in range(1,72,12)]
    df['Tenure Group'] = pd.cut(df['Tenure Months'], range(1,80,12), right = False, labels = labels)
    df['Tenure Group'].value_counts()
    df.drop(['CustomerID','Count','Country','State','Lat Long','Tenure Months','Churn Score', 'CLTV'], axis = 1, inplace = True)
    return df

df = load_data()

def show_pie_chart(df, groupby_column, chart_title):
    group_data = df.groupby([groupby_column, 'Churn Label'])['Churn Value'].count().reset_index()
    fig = px.pie(group_data, values='Churn Value', names=groupby_column, facet_col='Churn Label', 
                 title=chart_title)
    fig.update_traces(textfont_size=7)
    st.plotly_chart(fig)

def show_explore_page():
    st.image('Exploratory-Data-Analysis.png')
    st.title('Explore Churning Reasons')

    text = """
    <div style='text-align: justify; font-family: "Times New Roman"'>
    Here we present the key churn factors, primarily stemming from service-related aspects such as internet service, online security, online backup, and more. Analyzing the correlation using dummy variables reveals insightful patterns: shorter tenure months coupled with limited services tend to yield higher churn rates, whereas longer tenure without subscribing to internet services correlates with lower churn rates。
    </div>
    """
    st.markdown(text, unsafe_allow_html=True)

def show_churn_reasons():
    text = """
    <div style='text-align: justify; font-family: "Times New Roman", sans-serif; font-weight: bold; font-size: 25px;'>
    Main Churning Reasons
    </div>
    """
    st.markdown(text, unsafe_allow_html=True)

    df_filtered = df[df['Churn Reason'] != 'Not Churn']
    reason_count = df_filtered['Churn Reason'].value_counts()

    sns.set(style = 'white')
    st.plotly_chart(px.bar(x = reason_count.keys(), y = reason_count, color = reason_count, text = reason_count,
                title = 'Number of Churn Reason', width = 1000, height = 600).update_layout(
        yaxis_title = 'Churn Reason',
        xaxis_title = 'Count',
    ))

    # st.divider()
def show_service_factors():
    text = """
    <div style='text-align: justify; font-family: "Times New Roman", sans-serif; font-weight: bold; font-size: 25px;'>
    Service Factors
    </div>
    """
    st.markdown(text, unsafe_allow_html=True)
    # col1, col2 = st.columns(2)
    show_pie_chart(df, 'Internet Service', 'Internet Service Distribution')
    show_pie_chart(df, 'Online Security', 'Online Security Distribution')
    show_pie_chart(df, 'Online Backup', 'Online Backup Distribution')
    show_pie_chart(df, 'Device Protection', 'Device Protection Distribution')
    show_pie_chart(df, 'Tech Support', 'Tech Support Distribution')
    show_pie_chart(df, 'Streaming TV', 'Streaming TV Distribution')
    show_pie_chart(df, 'Streaming Movies', 'Streaming Movies Distribution')

    # st.divider()
def show_high_corr():
    text = """
    <div style='text-align: justify; font-family: "Times New Roman", sans-serif; font-weight: bold; font-size: 25px;'>
    High Correlation Dummy Variables
    </div>
    """
    st.markdown(text, unsafe_allow_html=True)
    df_copy = df.copy()
    df_copy.drop(['City','Zip Code','Latitude','Longitude','Churn Label','Churn Reason'], axis = 1, inplace = True)
    df_dummies = pd.get_dummies(df_copy)
    correlation = df_dummies.corr()['Churn Value'].sort_values(ascending=False)
    
    fig = px.bar(x=correlation.index, y=correlation.values, 
                 labels={'x': 'Feature', 'y': 'Correlation with Churn Value'}, 
                 title='Correlation with Churn Value', width=800, height=700)
    
    st.plotly_chart(fig)
    
