import streamlit as st
import pandas as pd
import os #import de l'Os
from dotenv import load_dotenv, find_dotenv
import platform
a = platform.system()

if a == 'Windows':
    load_dotenv("./.env",  override=True)
else:
    load_dotenv( dotenv_path="./.env.local", override=True)
cleandata = os.environ.get("EXPORTDIR")



st.write("""
# My first app
Hello *world!*
""")
    
df = pd.read_csv(os.path.join(cleandata, "resultat_brevet_2016_2022.csv"))
st.line_chart(df, y="Taux de réussite")
