import streamlit as st
import matplotlib.pyplot as plt

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('some numbers')
plt.show()