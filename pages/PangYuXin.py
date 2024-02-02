import streamlit as st
page=st.sidebar.radio("我的首页",["我的兴趣爱好","我的图片处理工具","我的智慧词典","我的留言区","教材背后不为人知的秘密"])
def page_1():
    st.write("")
def page_2():
    st.image()
def page_3():
    with open("","")as f:
        music=f.read()
        st.audio(music)
def page_4():
    pass
def pass_5():
    st.write("每日一更新栏")
    st.write("暂无")
if page=="我的叙述":
    page_1()
elif page=="我的图片处理工具":
    pass
elif page=="我的智能词典":
    pass
elif page=="我的留言区":
    pass
elif page=="教材背后不为人知的秘密"
    pass_5()