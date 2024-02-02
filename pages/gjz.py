'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页',['分享开心','创造开心','问题反馈','留言区'])

def page_1():
    st.write("hi!")
def page_2():
    a = "hi!"
    st.write(a)
def page_3():
    pass
def page_4():
    pass

if page == '分享开心':
    pass
elif page == '创造开心':
    pass
elif page == '问题反馈':
    pass
elif page == '留言区':
    pass
