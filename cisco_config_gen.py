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
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": descripcion}
            ],
            temperature=0.1,
            max_tokens=1024,
            stream=True
        )

        print(f"\n! --- INICIO CONFIGURACIÓN {escenario} ---")
        full_config = ""

        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="")
                full_config += content

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
    print("A. VLAN | B. OSPF | C. SUBNET | D. ACL")
    op = input("\nElija Escenario: ").upper()

    if op == 'A':
        desc = input("Detalles del escenario (VLANs, puertos, trunk): ")
        generar_configuracion(op, f"Genera configuracion de VLANs y trunking para switch capa 2. {desc}")

    elif op == 'B':
        desc = input("Detalles del escenario (proceso, redes, area): ")
        generar_configuracion(op, f"Genera configuracion OSPF para router Cisco IOS. {desc}")

    elif op == 'C':
        desc = input("Detalles del escenario (red base, prefijo, subredes): ")
        generar_configuracion(op, f"Genera subnetting y asignacion de IPs a interfaces Cisco IOS. {desc}")

    elif op == 'D':
        print("\n--- Escenario D: ACL (Lista de Control de Acceso) ---")
        red_origen  = input("Red de origen a controlar (ej: 192.168.10.0/24): ")
        red_destino = input("Red de destino (ej: 10.0.0.0/8 o 'any'): ")
        accion      = input("Accion (permit/deny): ").lower()
        interfaz    = input("Interfaz donde aplicar la ACL (ej: GigabitEthernet0/1): ")
        direccion   = input("Direccion (in/out): ").lower()
        desc = (
            f"Genera una ACL extendida en Cisco IOS. "
            f"Accion: {accion} trafico desde {red_origen} hacia {red_destino}. "
            f"Permitir el resto del trafico. "
            f"Aplicar la ACL en la interfaz {interfaz} direccion {direccion}."
        )
        generar_configuracion(op, desc)

    else:
        print("! Opcion invalida. Elija A, B, C o D.")

if __name__ == "__main__":
    main()