#=======================================================================================================
# IMPORTS
#=======================================================================================================
import streamlit as st
import base64

#=======================================================================================================
# Title
#=======================================================================================================
st.markdown("# Portfolio")

st.markdown("##### by Marcel Pratikto")

for i in range(3):
    st.text(" \n")

#=======================================================================================================
# DS460 - Big Data Programming
#=======================================================================================================
st.markdown("### DS 460 - Big Data Programming")

"""
[App Development Project](https://mp-bigdataprogramming.streamlit.app/)
"""

for i in range(3):
    st.text(" \n")

#=======================================================================================================
# ECEN 260 - Microprocessor Based System Design
#=======================================================================================================
st.markdown("### ECEN 260 - Microprocessor Based System Design")

video_col, _ = st.columns([3, 2])
with video_col:
    st.video("https://youtu.be/7ErvWzjYcJ8")

st.markdown("Lab report with schematics for the project:")

st.markdown(
    "[ECEN 260 Lab Report](https://github.com/MarcelPratikto/Portfolio/blob/f94f30bf986394d08b9b5e7970bc91bf8b820062/data/ECEN260-Microprocessor/ECEN_260_Final_Project_Report.pdf)"
)
