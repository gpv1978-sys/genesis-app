import google.generativeai as genai

class PromptEngine:
    def __init__(self, api_key):
        # Configuración del modelo Gemini
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def expand_idea(self, user_input):
        # El Framework RCPE + Chain of Thought (CoT)
        system_prompt = """
        Actúa como un Experto en Ingeniería de Prompts con enfoque en Mantenimiento Industrial.
        Tu misión es transformar ideas vagas en prompts maestros siguiendo el Framework RCPE:
        - R: Rol (Asignar una identidad experta)
        - C: Contexto (Definir el entorno industrial o de negocios)
        - P: Pasos (Instrucciones Chain-of-Thought paso a paso)
        - E: Ejecución (Formato de salida esperado)
        
        Si el usuario da un código de error, analízalo técnicamente.
        """
        
        response = self.model.generate_content(f"{system_prompt}\n\nEntrada del usuario: {user_input}")
        return response.text
