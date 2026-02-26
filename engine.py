import google.generativeai as genai

class PromptEngine:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        
        # --- BLOQUE DE DETECCIÓN AUTOMÁTICA ---
        model_to_use = 'gemini-1.5-flash' # Valor por defecto
        try:
            # Listamos los modelos disponibles para tu llave
            available_models = [m.name for m in genai.list_models() 
                               if 'generateContent' in m.supported_generation_methods]
            
            # Prioridad: 1.5-flash > 1.5-pro > gemini-pro
            if any('gemini-1.5-flash' in m for m in available_models):
                model_to_use = [m for m in available_models if 'gemini-1.5-flash' in m][0]
            elif any('gemini-1.5-pro' in m for m in available_models):
                model_to_use = [m for m in available_models if 'gemini-1.5-pro' in m][0]
            else:
                model_to_use = available_models[0] # El primero que funcione
                
        except Exception:
            # Si falla la lista, intentamos la ruta estándar de 2026
            model_to_use = 'models/gemini-1.5-flash'

        self.model = genai.GenerativeModel(model_to_use)
        # ---------------------------------------
        
        self.system_instruction = """
        Eres el motor PROMPT GENESIS V2.0. Tu función es transformar ideas vagas en PROMPTS MAESTROS.
        Usa el framework RCPE: Rol, Contexto, Pasos atómicos y Estilo.
        """

    def expand_idea(self, user_idea):
        try:
            # Limpiamos el nombre del modelo para el log (opcional)
            response = self.model.generate_content(
                f"{self.system_instruction}\n\nIDEA DEL USUARIO: {user_idea}"
            )
            return response.text
        except Exception as e:
            return f"Error crítico en la Cámara de Expansión: {str(e)}"