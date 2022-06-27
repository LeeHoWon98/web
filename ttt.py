import pandas as pd
import streamlit as st

st.title('배포 연습을 위한 데이터 시각화')
st.write('해당 데이터는 캐글에 있는 프리미엄 리그 데이터 입니다.')
st.write('https://www.kaggle.com/datasets/omkargowda/football-players-stats-premier-league-20212022')

df = pd.read_csv('data/12.csv', encoding='cp1252')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)