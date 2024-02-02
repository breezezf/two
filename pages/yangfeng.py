#我的主页
import streamlit as st

page = st.sidebar.radio("我的主页", ["我的兴趣推荐", "我的图片处理工具", "我的智能词典", "留言区", "蛋仔派对专区"])

def page_1():
    #我的兴趣推荐
    st.write(":blue[电影推荐]")
def page_2():
    #我的图片处理工具
    pass
def page_3():
    #我的智能词典
    pass
def page_4():
    #留言区
    pass
def page_5():
    #蛋仔派对专区
    st.write(":blue[1.蛋仔道具技巧]")

if page == "我的兴趣推荐":
    page_1()
elif page == "我的图片处理工具":
    pass
elif page == "我的智能词典":
    pass
elif page == "留言区":
    pass
elif page == "蛋仔派对专区":
    page_5()
