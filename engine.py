import os
from groq import Groq

class PromptEngine:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
        self.messages = [
            {
                "role": "system", 
                "content": """Actúa como un experto en ingeniería de prompts industriales.
                Tu objetivo es crear prompts de alta calidad en ESPAÑOL.
                
                Usa estrictamente el framework RCPE:
                1. **ROL**: Quién debe ser la IA.
                2. **CONTEXTO**: El escenario y objetivo.
                3. **PASOS**: Instrucciones detalladas.
                4. **EJECUCIÓN**: Formato de salida y restricciones.

                IMPORTANTE: Toda tu comunicación, explicaciones y el prompt resultante 
                deben estar en ESPAÑOL, a menos que el usuario pida lo contrario."""
            }
        ]

    def process_request(self, user_input):
        # Añadimos la petición del usuario al historial
        self.messages.append({"role": "user", "content": user_input})
        
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=0.7
            )
            response = completion.choices[0].message.content
            # Guardamos la respuesta de la IA para que tenga contexto en la siguiente iteración
            self.messages.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            return f"Error en el motor: {str(e)}"
