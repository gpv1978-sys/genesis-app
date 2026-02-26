import streamlit as st
import time

# 1. CONFIGURACIÓN (LÍNEA 1)
st.set_page_config(page_title="PROMPT GENESIS", page_icon="🧬", layout="wide")

# 2. OCULTAR TODO EL CÓDIGO Y MENÚS (MODO APK)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    #stDecoration {display:none;}
    </style>
    """, unsafe_allow_html=True)

# 3. IMPORTACIÓN SEGURA DEL MOTOR
try:
    from engine import PromptEngine
except ImportError:
    st.error("Error: No se encontró el archivo 'engine.py'. Asegúrate de que esté en la misma carpeta que main.py")
    st.stop()

# 4. LÓGICA DE API KEY
api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input("API Key:", type="password")

# 5. INTERFAZ
st.title("🧬 PROMPT GENESIS V2.0")

col_in, col_out = st.columns([1, 1])

with col_in:
    st.subheader("🛠️ Forja")
    idea = st.text_area("¿Qué quieres lograr?", height=150)
    tipo = st.selectbox("Estrategia:", ["Técnica", "Marketing", "Código"])
    
    if st.button("🚀 FORJAR"):
        if not api_key:
            st.error("Configura tu API Key")
        elif not idea:
            st.warning("Escribe una idea")
        else:
            with st.spinner("Procesando..."):
                try:
                    motor = PromptEngine(api_key)
                    resultado = motor.expand_idea(f"[{tipo}] {idea}")
                    st.session_state['resultado'] = resultado
                    st.rerun()
                except Exception as e:
                    st.error(f"Fallo en la forja: {e}")

with col_out:
    st.subheader("🔥 Resultado")
    if 'resultado' in st.session_state:
        # Mostramos el resultado de forma elegante
        st.info(st.session_state['resultado'])
        
        # BOTÓN DE COPIADO CON RESPALDO (Failsafe)
        try:
            # Intento con el método moderno
            st.copy_to_clipboard(st.session_state['resultado'])
            st.success("✅ ¡Copiado al portapapeles!")
        except Exception:
            # Si falla por versión, mostramos un área de texto fácil de copiar
            st.warning("Pulsa prolongadamente abajo para copiar:")
            st.text_area("Copiado manual:", value=st.session_state['resultado'], height=100)
    else:
        st.write("Esperando forja...")

# Botón de reset
if st.button("♻️ Nueva Forja"):
    st.session_state.clear()
    st.rerun()
