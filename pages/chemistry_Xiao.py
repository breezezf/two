import streamlit as st

##添加侧边栏
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区'])

# with open('misic.wav','rb') as f:             #添加声音
#     music = f.read()
#     st.audio(music)

# a = 'green['电影推荐']'                         #添加文字（带颜色）
# st.write(a)
# st.image('黑幕.jpg')                          #添加图片
# st.video('视频.mp4')                          #添加视频

if page == '我的兴趣推荐':
    a = ":green[电影推荐]"
    st.write(a)
    # st.image('黑幕.jpg') 
    
elif page == '我的图片处理工具':
    pass
elif page == '我的智能词典':
    pass
elif page == '我的留言区':
    pass
