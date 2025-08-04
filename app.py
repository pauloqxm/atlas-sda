import os
import streamlit as st

st.set_page_config(page_title="Atlas SDA", layout="wide")
st.title("✅ Deploy funcionando com porta dinâmica")

st.markdown("Se você está vendo isso, seu Streamlit está rodando corretamente na Railway.")

# Força execução com porta correta (caso necessário)
port = int(os.environ.get("PORT", 8501))
os.system(f"streamlit run app.py --server.port={port} --server.address=0.0.0.0")
exit()
