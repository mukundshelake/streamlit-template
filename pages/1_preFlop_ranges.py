import streamlit as st
import random, json
import numpy as np
st.markdown(
    """
    <style>
    .stButton > button {
        font-size: 12px;
        padding: 0px 0px;
    }
    </style>
    """,
    unsafe_allow_html= True
)

def action(lst, rn):
    """
    This function gets a list of percentages i.e. [p1, p2, p3, p4] for the three choices [raise, call, fold]. It generates a random number between 0-100.
    Then based on where the number lies between 0-p1, p1-(p1+p2), (p1+p2)-(p1+p2+p3), (p1+p2+p3)-(p1+p2+p3+p4); it replies with R,C,F or NA.
    """
    cum_sum = np.cumsum(lst)
    index = np.searchsorted(cum_sum, rn)
    ActionList = ['Raise', 'Call', 'Fold', 'NA']
    #print(cum_sum)
    return ActionList[index]


with open("rangeMaster.json", "r") as f:
    rangeMaster = json.load(f)
    



ranges = {
'LJ':['2X_vsBB','4X_vsHJ','4X_vsCO','4X_vsBN','4X_vsSB','4X_vsBB'],
'HJ':['2X_vsBB','3X_vsLJ','4X_vsCO','4X_vsBN','4X_vsSB','4X_vsBB','5X_vsLJ'],
'CO':['2X_vsBB','3X_vsLJ','3X_vsHJ','4X_vsBN','4X_vsSB','4X_vsBB','5X_vsLJ','5X_vsHJ'],
'BN':['2X_vsBB','3X_vsLJ','3X_vsHJ','3X_vsCO','4X_vsSB','4X_vsBB','5X_vsLJ','5X_vsHJ','5X_vsCO'],
'SB':['2X_vsBB','3X_vsLJ','3X_vsHJ','3X_vsCO','3X_vsBN','3X_vsBB','4X_vsBB','5X_vsLJ','5X_vsHJ','5X_vsCO','5X_vsBN' ,'5X_vsBB'],
'BB':['2X_vsSB','3X_vsLJ','3X_vsHJ','3X_vsCO','3X_vsBN','3X_vsSB','5X_vsLJ','5X_vsHJ','5X_vsCO','5X_vsBN' ,'5X_vsSB'],
}
rankOrder = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
reverse_rankOrder = {value: key for key, value in rankOrder.items()}
st.title("Poker Hand Selector")

posCol, spotCol = st.sidebar.columns(2)
if 'pos' not in st.session_state:
    st.session_state['pos']='BB'
st.session_state.pos=posCol.radio("Select the position", ['LJ', 'HJ', 'CO', 'BN', 'SB', 'BB'])
if 'spot' not in st.session_state:
    st.session_state['spot']='3X'
st.session_state.spot=spotCol.radio("Select the spot", ranges[st.session_state.pos])
rn = random.randint(0,100)

# # Rest of your code
cols = st.columns(13, gap="small")
selHand = ''
for i in range(2,15):
    for j in range(2,15):
        SorO = ''
        ranks = [i, j]
        ranks = sorted(ranks, reverse=True)
        if i == j:
            hand = str(reverse_rankOrder[16-i])+str(reverse_rankOrder[16-j])
        elif i > j:
            hand = str(reverse_rankOrder[16-j])+str(reverse_rankOrder[16-i])+'o'
        else:
            hand = str(reverse_rankOrder[16-i])+str(reverse_rankOrder[16-j])+'s'
        state = cols[j-2].button(hand, key = hand, use_container_width=True)
        if state:
            selHand = hand
            # st.write(f"You selected {selHand}")
spot = f"{st.session_state['pos']}_{st.session_state.spot}" 
st.write(f"You selected for {spot} for {selHand} with random number {rn}")
freqRange = rangeMaster[st.session_state['pos']][spot][selHand]
todo = action(freqRange, rn)
st.info(todo)