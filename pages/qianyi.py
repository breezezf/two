'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['兴趣推荐', '图片处理工具', '智慧词典', '留言区', '英语语法', '解一元一次方程组'])


def page_1():
    '''兴趣推荐'''
    st.write(':red[游戏推荐]：Rolling Sky')
    st.video('qianyi_RS.mp4')
    st.write(':red[音乐推荐]：周杰伦《本草纲目》')
    with open('qianyi_本草纲目.MP3', 'rb') as f:
        sound = f.read()
        st.audio(sound)
    st.write(':red[影片推荐]：《流浪地球2》')
    st.image('qianyi_WE2.jpg')


def page_2():
    '''图片处理工具'''
    pass

    
def page_3():
    '''智慧词典'''
    pass


def page_4():
    '''留言区'''
    pass
    

def page_5():
    '''英语语法'''
    pass
    

def page_6():
    '''解一元一次方程组'''
    pass


if page == '兴趣推荐':
    page_1()
elif page == '图片处理工具':
    pass
elif page == '智慧词典':
    pass
elif page == '留言区':
    pass
elif page == '英语语法':
    pass
elif page == '解一元一次方程组':
    pass
