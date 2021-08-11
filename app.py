import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
from plotly.subplots import make_subplots

DATA_URL=('androidlogin.xlsx')
def load_data():
	data=pd.read_excel(DATA_URL)

	return data 

data = load_data()
date=data['Date']
st.set_page_config(layout="wide")
st.title('Login Data Analysis %s'%(date[0]))
st.write("### This analysis is done on the data extracted from the outlook servers###")
st.write("\n### Login Data: Phone Logins Vs Total Number of Logins###\n The graph shows the number of times the Employee has logged in from a phone and the total number of times the Employee Logged in for the entire week.")


names=data['Username']
names1=data['Username'].to_list()


options=st.multiselect("Employee Name",names1)

AndroidLogin=data['Android Login']
TotalLogin=data['Total Login']
df=pd.DataFrame({'Names':data['User'].isin(options),'Android Logins':data['Android Login'].values,'Total Logins':data['Total Login'].values})
#if st.sidebar.checkbox('Log In Data', True, key=1):
	#st.write(df)

fig = go.Figure(data=[go.Bar(name='Phone Logins',x=options,y=AndroidLogin,marker_color='indianred',hovertext=AndroidLogin,text=AndroidLogin),go.Bar(name='Total Login',x=options,y=TotalLogin,marker_color='mediumorchid',hovertext=TotalLogin,text=TotalLogin)])

	#fig=go.Figure()
	#fig.add_trace(go.Bar(x='Names',y='Android Logins',name='Android Logins',marker_color='indianred',text=AndroidLogin))
	#fig.add_trace(go.Bar(x='Names',y='Total Logins',name='Total Logins', marker_color='darkviolet',text=TotalLogin))
	#fig.add_trace(go.Bar(x=team1,y=interview,name='Interviews',marker_color='darkolivegreen',text=interview))
fig.update_traces(texttemplate='%{text:.3 bs}', textposition='outside',width=0.4)
	#fig.update_layout(hovertemplate = "%{options}: <br>Android Logins: %{AndroidLogin} </br>Total Logins: %{TotalLogin}")
fig.update_layout(barmode='group',height=600,width=800)
st.plotly_chart(fig)


st.markdown('### Outlook Activity Analysis %s'%(date[0]))
st.write('This is an analysis of the outlook activity of each employee.\n Mapping the earliest and the latest Login in outlook from a Laptop or Phone.\n The number of dots against your name shows your login activity for that day.')
st.write('The Graph has been split into to the first graph is for alphabet A-K, The second graphis for L-Z')
DATA_URL1=('logindetails.xlsx')
def load_data():
	data1=pd.read_excel(DATA_URL1)

	return data1 

data1 = load_data()

#st.write(data1)




windows_login=data1['Earliest_Login_windows']
operating_system=data1['Operating System']
date=data1['DateInLocalTime']
time=data1['TIME_']
Names=data1['User']
Names1=Names.drop_duplicates()
Names12=Names1.to_list()
#options1=st.multiselect("Employee Names",Names12)
df=pd.DataFrame({'Names':Names.values,'Logins':windows_login.values,'Time':time.values,'Date':date.values,'Operating System':operating_system.values})
#st.write(windows_login)
#st.write(Names1)
#st.write(df)
fig2=px.scatter(df,x='Names',y='Logins',height=1000,width=800,color='Operating System')
st.plotly_chart(fig2)


DATA_URL2=('logindetailspart2.xlsx')
def load_data():
	data2=pd.read_excel(DATA_URL2)

	return data2 

data2 = load_data()



windows_login1=data2['Earliest_Login_windows']
date1=data2['DateInLocalTime']
time1=data2['TIME_']
Name=data2['User']
operating_system1=data2['Operating System']
Names1=Names.drop_duplicates()
Names12=Names1.to_list()
#options2=st.multiselect("Employee Name",Names12)
df=pd.DataFrame({'Names':Name.values,'Logins':windows_login1.values,'Time':time1.values,'Date':date1.values,'Operating System':operating_system1.values})
#st.write(windows_login)
#st.write(Names1)
#st.write(df)
fig3=px.scatter(df,x='Names',y='Logins',height=1000,width=800,color='Operating System')
st.plotly_chart(fig3)
