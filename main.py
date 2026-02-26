import streamlit as st
from engine import PromptEngine

st.set_page_config(page_title="PROMPT GENESIS", page_icon="🧬", layout="wide")

# Inicializar el motor en la sesión de Streamlit para que no se borre la memoria
if 'motor' not in st.session_state:
    st.session_state['motor'] = None

st.title("🧬 PROMPT GENESIS V2.0")

with st.sidebar:
    st.header("⚙️ Configuración")
    api_key = st.text_input("Groq API Key:", type="password")
    if st.button("🔄 Reiniciar Sesión"):
        st.session_state['motor'] = None
        st.session_state.pop('resultado', None)
        st.rerun()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛠️ Forja")
    idea = st.text_area("Describe tu idea inicial:", height=150)
    if st.button("🚀 GENERAR ESTRATEGIA"):
        if api_key and idea:
            with st.spinner("Creando ADN del prompt..."):
                # Creamos el motor solo si no existe
                st.session_state['motor'] = PromptEngine(api_key)
                resultado = st.session_state['motor'].process_request(idea)
                st.session_state['resultado'] = resultado
        else:
            st.warning("Falta API Key o Idea.")

with col2:
    st.subheader("🔥 Resultado y Refinamiento")
    if 'resultado' in st.session_state:
        # Mostramos el prompt actual
        st.markdown(st.session_state['resultado'])
        
        st.divider()
        
        # CAMPO DE REFINAMIENTO
        feedback = st.text_input("¿Quieres ajustar algo? (Ej: 'Hazlo más formal', 'Añade ejemplos')")
        if st.button("🪄 REFINAR"):
            with st.spinner("Ajustando..."):
                nuevo_resultado = st.session_state['motor'].process_request(feedback)
                st.session_state['resultado'] = nuevo_resultado
                st.rerun()
