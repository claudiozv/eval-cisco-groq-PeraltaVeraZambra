import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv() # Carga la API Key de forma segura [cite: 25, 26]
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Prueba rápida
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Genera un comando Cisco para ver las interfaces."}]
)
print(completion.choices[0].message.content)