import streamlit as st
from engine import PromptEngine

# 1. CONFIGURACIÓN DE PÁGINA (Debe ser la primera línea)
st.set_page_config(
    page_title="PROMPT GENESIS",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS PARA OCULTAR INTERFAZ DE STREAMLIT Y LIMPIAR APP
st.markdown("""
    <style>
    /* Ocultar menú de hamburguesa y marca de agua de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Ajustar espacio superior para que parezca App nativa */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    /* Estilo para el botón de copiado (más grande para pulgares) */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        font-weight: bold;
    }
    
    /* Estilo para el área de resultado */
    .result-box {
        background-color: #1e2129;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #3d414b;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. GESTIÓN DE API KEY
api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input("🔑 API Key:", type="password")

# 4. TÍTULO DE LA APP
st.title("🧬 PROMPT GENESIS V2.0")

# 5. ESTRUCTURA DE LA INTERFAZ
# En móviles, las columnas se apilan automáticamente
col_input, col_output = st.columns([1, 1])

with col_input:
    st.subheader("🛠️ Forja de Idea")
    idea = st.text_area("Describe el problema:", placeholder="Ej: Error F0022 en PLC Siemens...", height=150)
    tipo_ia = st.selectbox("Optimizar para:", ["Ingeniería / Técnico", "Marketing", "Código"])
    
    if st.button("🚀 FORJAR ESTRATEGIA"):
        if not api_key:
            st.error("Falta API Key")
        elif not idea:
            st.warning("Escribe una idea")
        else:
            with st.spinner("🧠 Razonando..."):
                try:
                    motor = PromptEngine(api_key)
                    resultado = motor.expand_idea(f"[{tipo_ia}] {idea}")
                    st.session_state['resultado'] = resultado
                except Exception as e:
                    st.error(f"Error: {e}")

# 6. RESULTADO Y BOTÓN DE COPIADO
with col_output:
    st.subheader("🔥 Resultado")
    if 'resultado' in st.session_state:
        # Mostramos el resultado dentro de un contenedor visual
        st.markdown(f'<div class="result-box">{st.session_state["resultado"]}</div>', unsafe_allow_html=True)
        
        # BOTÓN DE COPIADO OFICIAL (Streamlit nativo)
        # Este componente aparece claramente debajo del resultado
        st.copy_to_clipboard(st.session_state['resultado'], before_text="📋 COPIAR PROMPT", after_text="✅ ¡COPIADO!")
        
        st.success("Listo para pegar en tu IA favorita.")
    else:
        st.info("El resultado aparecerá aquí.")
