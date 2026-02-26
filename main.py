import streamlit as st
from engine import PromptEngine

st.set_page_config(page_title="PROMPT GENESIS V2.0", page_icon="🧬", layout="wide")

# Estilo Pro
st.markdown("""
    <style>
    .stTextInput > div > div > input { background-color: #1e1e1e; color: #00ffcc; }
    .stButton > button { width: 100%; background-color: #00ffcc; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 PROMPT GENESIS V2.0")
st.subheader("Arquitecto de Instrucciones de Élite")

with st.sidebar:
    st.header("⚙️ NÚCLEO")
    # Intentar leer desde los secretos, si no, pedirla manualmente
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = st.sidebar.text_input("Gemini API Key", type="password")
    st.write("---")
    st.markdown("**Versión 2.0:**\n- Framework RCPE\n- Lógica CoT\n- Optimización Multimodelo")

# Área de trabajo
col1, col2 = st.columns([1, 1])

with col1:
    idea = st.text_area("🚀 Describe tu intención o necesidad:", 
                        placeholder="Ej: Necesito un plan de marketing para una app de café...",
                        height=150)
    
    tipo_ia = st.selectbox("Optimizar para:", ["ChatGPT/Claude (Texto)", "Midjourney/DALL-E (Imagen)", "Análisis Técnico/Código"])

if st.button("FORJAR ESTRATEGIA"):
    if not api_key:
        st.error("Falta la llave del Oráculo (API Key).")
    elif not idea:
        st.warning("El Arquitecto debe proveer una intención.")
    else:
        with st.spinner("🧠 El motor está razonando la mejor arquitectura..."):
            motor = PromptEngine(api_key)
            resultado = motor.expand_idea(f"[{tipo_ia}] {idea}")
            
            with col2:
                st.info("🔥 PROMPT MAESTRO GENERADO:")

                st.markdown(resultado)
