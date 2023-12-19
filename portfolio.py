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

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

displayPDF("data/ECEN260-Microprocessor/ECEN_260_Final_Project_Report.pdf")