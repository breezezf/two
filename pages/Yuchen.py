'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区'])
def page_1():
    '''我的兴趣推荐'''
    st.write("电影推荐")
    a = ':purple[电影推荐]'
def page_2():
    '''我的图片处理工具'''
    st.image('bcm.png')

def page_3():
    pass
    '''我的图片处理工具'''
def page_4():
    pass
    '''我的留言区'''
if page == '我的兴趣推荐':
    pass
elif page == '我的图片处理工具':
    pass
elif page == '我的智能词典':
    pass 
elif page == '我的留言区':
    pass
#st.video("")