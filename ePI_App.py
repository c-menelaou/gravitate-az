import streamlit as st
from pathlib import Path
import subprocess
import streamlit.components.v1 as components
import json


st.markdown("<h1 style='text-align: center; color: black;'>Electronic Product Information(ePI) App</h1>", unsafe_allow_html=True)


st.header('AstraZeneca ePI processor', divider='rainbow')

uploaded_file = st.file_uploader("Choose the ePI pdf file")
new_file_path ="data/upload_html"
Submit = st.button(label='Upload')
if Submit :
    st.markdown("**The file is sucessfully Uploaded.**")

    # Save uploaded file to 'F:/tmp' folder.
    save_folder = 'data/upload_pdf'
    save_path = Path(save_folder, uploaded_file.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())

    if save_path.exists():
        st.success(f'File {uploaded_file.name} is successfully saved!')

        #subprocess.call([
        #            "pdftohtml",
        #            "-s",
        #            "-noframes",
        #            "-i",
        #            "-q",
        #            str(save_path),
        #            str(new_file_path)
        #        ]) 
    st.header("Pdf Parsed Output", divider='rainbow')
    HtmlFile = open("data/html/biktarvy-epar-product-information_en.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    #print(source_code)
    components.html(source_code, height=800,width= 800, scrolling= True)

    st.header("ePI Processed Output", divider='rainbow')
    ouput_json = open("data/output/enriched_export.json", 'r', encoding='utf-8')
    #print(type(json.load(ouput_json)[0]))
    st.json(json.dumps(json.load(ouput_json)[0]))