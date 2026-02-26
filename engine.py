import streamlit as st
from engine import PromptEngine

# 1. CONFIGURACIÓN DE PÁGINA (Debe ser la primera instrucción de Streamlit)
st.set_page_config(
    page_title="PROMPT GENESIS V2.0",
    page_icon="🧬",
    initial_sidebar_state="collapsed",
    layout="wide"
)

# 2. ESTILOS PERSONALIZADOS (Para un look más industrial y elegante)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .copy-button {
        background-color: #262730;
        border: 1px solid #464646;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. GESTIÓN DE API KEY
api_key = None
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = st.sidebar.text_input("🔑 Gemini API Key:", type="password")
    st.sidebar.info("Para uso permanente, añade la clave en los Secrets de Streamlit Cloud.")

# 4. INTERFAZ PRINCIPAL
st.title("🧬 PROMPT GENESIS V2.0")
st.caption("Arquitectura de Instrucciones para Entornos Industriales de Alta Precisión")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("🛠️ Forja de Idea")
    idea = st.text_area(
        "Describe el problema o intención:", 
        placeholder="Ej: Falla en servomotor KUKA eje 2, error E-204...",
        height=200
    )
    
    tipo_ia = st.selectbox(
        "Optimizar estrategia para:", 
        ["Análisis Técnico / Ingeniería", "Marketing / Ventas", "Código / Programación", "Relato Creativo"]
    )
    
    btn_generar = st.button("🚀 FORJAR ESTRATEGIA MAESTRA")

# 5. LÓGICA DE PROCESAMIENTO
if btn_generar:
    if not api_key:
        st.error("Falta la API Key de Gemini.")
    elif not idea:
        st.warning("Por favor, introduce una idea para procesar.")
    else:
        with st.spinner("🧠 El Oráculo está razonando..."):
            try:
                # Inicialización del motor
                motor = PromptEngine(api_key)
                # Construcción del prompt refinado
                prompt_input = f"Modo: {tipo_ia}. Idea: {idea}"
                resultado = motor.expand_idea(prompt_input)
                
                # Guardar en sesión para que persista al interactuar con otros botones
                st.session_state['prompt_final'] = resultado
            except Exception as e:
                st.error(f"Error en la forja: {str(e)}")

# 6. COLUMNA DE RESULTADOS Y HERRAMIENTAS
with col2:
    st.subheader("🔥 Resultado de la Forja")
    if 'prompt_final' in st.session_state:
        # Mostrar el resultado
        st.markdown("---")
        st.markdown(st.session_state['prompt_final'])
        st.markdown("---")
        
        # BOTÓN DE COPIADO AL PORTAPAPELES
        # Usamos la función nativa de Streamlit para máxima compatibilidad
        if st.button("📋 COPIAR PROMPT MAESTRO"):
            try:
                # Esta función es compatible con versiones recientes de Streamlit
                # y funciona perfectamente en dispositivos móviles
                st.write(f'<textarea id="input_copy" style="opacity:0;height:0;">{st.session_state["prompt_final"]}</textarea>', unsafe_allow_html=True)
                st.write("""
                    <script>
                    var copyText = document.getElementById("input_copy");
                    copyText.select();
                    document.execCommand("copy");
                    </script>
                    """, unsafe_allow_html=True)
                st.success("¡Copiado con éxito! Pégalo en tu IA favorita.")
            except:
                st.error("Tu navegador bloqueó el copiado automático. Por favor, selecciona el texto manualmente.")
    else:
        st.info("El Prompt Maestro aparecerá aquí una vez forjada la estrategia.")

# Pie de página técnico
st.divider()
st.caption("PROMPT GENESIS V2.0 | Impulsado por Google Gemini | Arquitectura RCPE-CoT")
