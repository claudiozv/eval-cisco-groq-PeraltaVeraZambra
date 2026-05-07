# eval-cisco-groq-PeraltaVeraZambra

# Generador Inteligente de Configuraciones Cisco IOS

## Descripción del Proyecto
Este proyecto consiste en una aplicación de consola en Python, nombrada `cisco_config_gen.py`. La herramienta recibe descripciones de escenarios de red y utiliza Python y Groq para generar bloques de configuración Cisco IOS reales y listos para ser implementados. El sistema utiliza un system prompt especializado para asegurar que el modelo devuelva únicamente comandos válidos, sin texto explicativo adicional fuera de los comentarios de IOS. Además, emplea respuestas en streaming (`stream=True`) para visualizar la salida en tiempo real y guarda automáticamente cada archivo de configuración en un directorio local.

# Integrantes del Grupo
* **Matías Peralta**  
* **Hernán Vera**
* **Claudio Zambra**
## Instrucciones de Instalación
Como primer paso se crea el repositorio de GitHub y lo vinculamos con el Visual Studio Code. Una vez dentro nos aseguramos de instalar los requerimientos necesarios. Tambien se debe configurar el archivo .gitgnore para que excluya __venv/__, __pycache__/ y __.env__ .(falta terminar)
## Escenarios y Funciones
* **Escenario A (VLANs y Trunking):** El usuario ingresa una lista de VLANs con sus nombres y los puertos asignados para configurar un switch de capa 2.
* **Escenario B (OSPF):** El usuario proporciona el ID del proceso de enrutamiento, las redes que se desean anunciar y las áreas correspondientes para configurar un router.
* **Escenario C (Subnetting e IP):** El usuario define una red base, un prefijo y la cantidad de subredes necesarias para asignar direcciones IP a las interfaces.
* Todas las salidas generadas se almacenan automáticamente en la carpeta `/configs/` utilizando la nomenclatura `escenario_{tipo}_{timestamp}.txt`.
* **Escenario D (a definir):**
## Justificación de Parámetros del Modelo
(por completar)
## Limitaciones Conocidas
(por completar)
