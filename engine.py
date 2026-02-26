import google.generativeai as genai

class PromptEngine:
    def __init__(self, api_key):
        # Configuración base
        genai.configure(api_key=api_key)
        
        # Usamos 'gemini-pro', que es el modelo con mayor compatibilidad 
        # en todas las versiones de la API.
        self.model = genai.GenerativeModel('gemini-pro')

    def expand_idea(self, user_input):
        system_prompt = (
            "Actúa como un experto en ingeniería de prompts. "
            "Transforma la siguiente idea en una instrucción maestra "
            "usando el framework RCPE (Rol, Contexto, Pasos, Ejecución)."
        )
        
        try:
            # Llamada simplificada
            response = self.model.generate_content(f"{system_prompt}\n\nEntrada: {user_input}")
            
            if response.text:
                return response.text
            else:
                return "El motor no pudo generar una respuesta clara. Revisa tu API Key."
        except Exception as e:
            # Si gemini-pro también falla, intentamos la ruta absoluta
            return f"Error de conexión con el modelo: {str(e)}"
