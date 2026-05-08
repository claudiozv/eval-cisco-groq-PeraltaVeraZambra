import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("! ERROR: No hay API KEY.")
    exit()

client = Groq(api_key=api_key)

# SYSTEM PROMPT DEFINITIVO (Cumple Ítem 6 y 2.1 de la pauta) [cite: 17, 52]
SYSTEM_PROMPT = (
    "ACT AS A CISCO IOS CONFIGURATION ENGINE. "
    "OUTPUT ONLY VALID COMMANDS. "
    "STRICT RULES: "
    "1. NO GREETINGS, NO EXPLANATIONS, NO INTRODUCTIONS. "
    "2. NO MARKDOWN CODE BLOCKS (DO NOT USE BACKTICKS OR ```). "
    "3. EVERY COMMENT MUST START WITH '!'. "
    "4. IF YOU CANNOT GENERATE THE COMMAND, RESPOND ONLY WITH '!'. "
    "5. OUTPUT MUST BE PURE TEXT READY TO COPY-PASTE INTO CLI."
)

def generar_configuracion(escenario, descripcion):
    """Generación con los valores exactos de la pauta """
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": descripcion}
            ],
            temperature=0.1,  # Exigencia pauta: <= 0.2 [cite: 34]
            max_tokens=1024, # Exigencia pauta: >= 800 [cite: 34]
            stream=True      # Exigencia pauta: Streaming [cite: 27]
        )

        print(f"\n! --- INICIO CONFIGURACIÓN {escenario} ---")
        full_config = ""
        
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="")
                full_config += content
        
        # Guardado automático en /configs/ [cite: 30]
        if not os.path.exists('configs'):
            os.makedirs('configs')
        
        timestamp = int(time.time())
        filename = f"configs/escenario_{escenario}_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write(full_config)
            
        print(f"\n! --- FIN (Archivo: {filename}) ---")

    except Exception as e:
        print(f"\n! Error: {e}")

def main():
    print("CISCO GENERATOR V1.0 - INACAP LA SERENA")
    print("A. VLAN | B. OSPF | C. SUBNET")
    op = input("\nElija Escenario: ").upper()
    if op in ['A', 'B', 'C']:
        desc = input("Detalles del escenario: ")
        generar_configuracion(op, desc)

if __name__ == "__main__":
    main()