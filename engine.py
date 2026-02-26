import os
from groq import Groq

class PromptEngine:
    def __init__(self, api_key):
        # Inicializamos el cliente de Groq
        self.client = Groq(api_key=api_key)
        # Usamos Llama 3 70B, un modelo de élite para razonamiento
        self.model = "llama3-70b-8192"

    def expand_idea(self, user_input):
        system_prompt = """
        Actúa como un Experto en Ingeniería de Prompts Industriales.
        Tu misión es transformar ideas en prompts maestros siguiendo el Framework RCPE:
        - R: Rol (Asignar una identidad experta)
        - C: Contexto (Definir el entorno industrial)
        - P: Pasos (Instrucciones paso a paso)
        - E: Ejecución (Formato de salida)
        """
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                model=self.model,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error en el motor Groq: {str(e)}"
