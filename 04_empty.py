import streamlit as st
import time

st.title("Cats!!!")

row1 = st.columns(3)
row2 = st.columns(3)

grid = [col.container(height=200) for col in row1 + row2]
# > Let all col be containers with height 200.
safe_grid = [card.empty() for card in grid]
# > Let all cards in this grid be the empty.

def black_cats():
    time.sleep(1)
    st.title("🐈‍⬛🐈‍⬛")
    st.markdown("🐾🐾🐾")

def orange_cats()
    time.sleep(1)
    st.title("🐈🐈")
    st.markdown("🐾🐾🐾")


@st.fragment
def herd_black_cats(card_a, card_b, card_c):
    st.button("一群小黑貓")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()

@st.fragment
def herd_orange_cats(card_a, card_b, card_c):
    st.button("一群小橘貓")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()

with st.sidebar:
    herd_black_cats(grid[0].empty(), grid[1].empty(), grid[2].empty())
    herd_orange_cats(grid[3].empty(), grid[4].empty(), grid[5].empty())
    st.button("ㄧ群小貓貓們") 