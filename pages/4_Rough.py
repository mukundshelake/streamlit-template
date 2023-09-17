import streamlit as st



def show():
    ranges = {
    'LJ':['2X_vsBB','4X_vsHJ','4X_vsCO','4X_vsBN','4X_vsSB','4X_vsBB'],
    'HJ':['2X_vsBB','3X_vsLJ','4X_vsCO','4X_vsBN','4X_vsSB','4X_vsBB','5X_vsLJ'],
    'CO':['2X_vsBB','3X_vsLJ','3X_vsHJ','4X_vsBN','4X_vsSB','4X_vsBB','5X_vsLJ','5X_vsHJ'],
    'BN':['2X_vsBB','3X_vsLJ','3X_vsHJ','3X_vsCO','4X_vsSB','4X_vsBB','5X_vsLJ','5X_vsHJ','5X_vsCO'],
    'SB':['2X_vsBB','3X_vsLJ','3X_vsHJ','3X_vsCO','3X_vsBN','3X_vsBB','4X_vsBB','5X_vsLJ','5X_vsHJ','5X_vsCO','5X_vsBN' ,'5X_vsBB'],
    'BB':['2X_vsSB','3X_vsLJ','3X_vsHJ','3X_vsCO','3X_vsBN','3X_vsSB','5X_vsLJ','5X_vsHJ','5X_vsCO','5X_vsBN' ,'5X_vsSB'],
    }

    if 'pos' not in st.session_state:
        st.session_state['pos']='BB'
    st.session_state.pos=st.sidebar.radio("Select the position", ['LJ', 'HJ', 'CO', 'BN', 'SB', 'BB'])
    if 'spot' not in st.session_state:
        st.session_state['spot']='3X'
    st.session_state.spot=st.sidebar.radio("Select the spot", ranges[st.session_state.pos])
    if 'img' not in st.session_state:
        st.session_state['img']='RangeImages/BB_2X_vsSB.png'
    imgAddress = f'RangeImages/{st.session_state.pos}_{st.session_state.spot}.png'
    st.session_state['img'] = imgAddress
    st.write(st.session_state.pos)
    st.write(st.session_state.spot)
    st.write(imgAddress)
    st.image(st.session_state.img)


show()