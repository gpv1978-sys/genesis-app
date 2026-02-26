import streamlit as st
from engine import PromptEngine

# 1. CONFIGURACIÓN INICIAL (Obligatorio en la línea 1 o 2)
st.set_page_config(
    page_title="PROMPT GENESIS",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. LIMPIEZA DE INTERFAZ (Ocultar menús de Streamlit para modo APK)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem;}
    /* Estilo para que el resultado resalte */
    .stMarkdown div {line-height: 1.6;}
    </style>
    """, unsafe_allow_html=True)

# 3. CONEXIÓN CON EL MOTOR
api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input("API Key:", type="password")

# 4. CUERPO DE LA APP
st.title("🧬 PROMPT GENESIS V2.0")

col_in, col_out = st.columns([1, 1])

with col_in:
    st.subheader("🛠️ Forja")
    idea = st.text_area("¿Qué quieres lograr?", placeholder="Ej: Reporte de falla motor eje 2...", height=150)
    tipo = st.selectbox("Estrategia:", ["Técnica", "Marketing", "Código"])
    
    if st.button("🚀 FORJAR"):
        if not api_key:
            st.error("Falta API Key")
        elif not idea:
            st.warning("Escribe tu idea")
        else:
            with st.spinner("Procesando..."):
                try:
                    motor = PromptEngine(api_key)
                    resultado = motor.expand_idea(f"[{tipo}] {idea}")
                    st.session_state['resultado'] = resultado
                except Exception as e:
                    st.error(f"Error: {e}")

with col_out:
    st.subheader("🔥 Resultado")
    if 'resultado' in st.session_state:
        # Contenedor de texto
        st.info(st.session_state['resultado'])
        
        # BOTÓN DE COPIADO (Requiere Streamlit 1.32+)
        try:
            st.copy_to_clipboard(st.session_state['resultado'], before_text="📋 COPIAR PROMPT", after_text="✅ ¡COPIADO!")
        except AttributeError:
            st.warning("Actualiza requirements.txt a streamlit>=1.32.0 para usar el botón de copiado.")
    else:
        st.write("El resultado aparecerá aquí.")

# Botón para limpiar sesión y empezar de nuevo
if st.button("♻️ Nueva Forja"):
    if 'resultado' in st.session_state:
        del st.session_state['resultado']
        st.rerun()


