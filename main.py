import streamlit as st
from engine import PromptEngine  # Asegúrate de que engine.py esté en la misma carpeta

# 1. CONFIGURACIÓN DE PÁGINA (DEBE SER EL PRIMER COMANDO ST)
st.set_page_config(
    page_title="PROMPT-GENESIS",
    page_icon="🧬",
    initial_sidebar_state="collapsed",
    layout="wide"
)

# 2. GESTIÓN DE LA LLAVE (API KEY) - Prevenimos el NameError
api_key = None

if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    # Si no está en secretos, la pedimos en la barra lateral
    api_key = st.sidebar.text_input("Introduce tu Gemini API Key:", type="password")

# 3. INTERFAZ DE USUARIO
st.title("🧬 PROMPT GENESIS V2.0")
st.subheader("Arquitecto de Instrucciones de Élite")

col1, col2 = st.columns([1, 1])

with col1:
    idea = st.text_area("🚀 Describe tu intención:", 
                        placeholder="Ej: Análisis de falla en motor KUKA...",
                        height=150)
    tipo_ia = st.selectbox("Optimizar para:", ["Texto", "Imagen", "Análisis Técnico"])

# 4. LÓGICA DE EJECUCIÓN
if st.button("FORJAR ESTRATEGIA"):
    if not api_key:
        st.error("Error: No se encontró la API Key. Configúrala en los Secrets de Streamlit o en la barra lateral.")
    elif not idea:
        st.warning("Por favor, describe una idea o intención.")
    else:
        with st.spinner("🧠 El motor está razonando..."):
            try:
                # Inicializamos el motor solo cuando tenemos la llave
                motor = PromptEngine(api_key)
                resultado = motor.expand_idea(f"[{tipo_ia}] {idea}")
                
                with col2:
                    st.info("🔥 PROMPT MAESTRO GENERADO:")
                    st.markdown(resultado)
            except Exception as e:
                st.error(f"Hubo un fallo en la forja: {str(e)}")

