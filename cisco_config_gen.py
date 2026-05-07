import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Borrador del System Prompt especializado [cite: 29, 52]
SYSTEM_PROMPT = "Eres un experto en redes Cisco. Devuelve SOLO comandos IOS válidos, sin texto explicativo."

def main():
    print("--- Generador de Configuraciones Cisco (INACAP) ---")
    # Estructura inicial para cumplir el Item 5 
    print("1. Escenario A (VLANs)")
    print("2. Escenario B (OSPF)")
    print("3. Escenario C (Subnetting)")
    opcion = input("Seleccione escenario: ")

if __name__ == "__main__":
    main()