import streamlit as st

st.image("Zeanwei_截屏2024-02-01 13.21.03.png")

#with open ("music.wav", "rb") as f:
#music = f.read()
#    st.audio(music)

st.write("最拿手的技能是数学和排球；最想分享的喜悦是单发出草神；最爱的电影是Fate三部曲；这是我认为最难忘的旅行和难得的景色")
st.image("Zeanwei_111.tiff")

#st.video("视频名称")








page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

if page =='我的兴趣推荐':
    a = ":red[ddddd]"
    st.write(a)

elif page =='我的图片处理工具':
    pass
elif page =='我的智能词典':
    pass
elif page =='我的留言区':
    pass
