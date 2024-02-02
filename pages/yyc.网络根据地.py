'''我的主页'''
import streamlit as st
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    pass
def page_2():
    pass
def page_3():
    pass
def page_4():
    pass
if page=='我的兴趣推荐':
    a=':blue[名著推荐]'
    st.write(a)
    st.image('西游记.png')
elif page=='我的图片处理':
    pass
elif page=='我的智慧词典':
    pass
elif page=='我的留言区':
    pass