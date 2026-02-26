import google.generativeai as genai

class PromptEngine:
    def __init__(self, api_key):
        # Configuración del modelo Gemini
        genai.configure(api_key=api_key)
        # Cambiamos a la versión estable para evitar el error 404
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

    def expand_idea(self, user_input):
        # Framework RCPE + Chain of Thought (CoT)
        system_prompt = """
        Eres un Experto en Ingeniería de Prompts Industriales. 
        Tu objetivo es aplicar el Framework RCPE (Rol, Contexto, Pasos, Ejecución) 
        y razonamiento Chain-of-Thought para generar prompts maestros.
        """
        
        try:
            # Forzamos la generación de contenido
            response = self.model.generate_content(f"{system_prompt}\n\nEntrada: {user_input}")
            return response.text
        except Exception as e:
            return f"Error interno del motor: {str(e)}"
