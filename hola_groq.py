import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def test_conexion():
    if not api_key:
        print("! ERROR: Revisa el archivo .env")
        return

    try:
        client = Groq(api_key=api_key)
        
        # System prompt ultra-estricto para CERO explicaciones
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "Eres un motor de texto puro. Tu única función es devolver comandos Cisco IOS. PROHIBIDO: saludar, explicar, usar Markdown (```) o dar cualquier texto que no sea un comando. Si no hay comando, no respondas nada."
                },
                {
                    "role": "user", 
                    "content": "Comando para ver interfaces brief."
                }
            ],
            temperature=0.0 # Temperatura en 0 para que sea un robot total
        )

        # Usamos .strip() para limpiar cualquier espacio extra
        print(completion.choices[0].message.content.strip())

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_conexion()