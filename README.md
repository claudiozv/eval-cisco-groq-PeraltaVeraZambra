# eval-cisco-groq-PeraltaVeraZambra

# Generador Inteligente de Configuraciones Cisco IOS

## Descripción del Proyecto
Este proyecto consiste en una aplicación de consola en Python, nombrada `cisco_config_gen.py`. La herramienta recibe descripciones de escenarios de red y utiliza el SDK de Python de Groq para generar bloques de configuración Cisco IOS reales y listos para ser implementados. El sistema utiliza un system prompt especializado para asegurar que el modelo devuelva únicamente comandos válidos, sin texto explicativo adicional fuera de los comentarios de IOS. Además, emplea respuestas en streaming (`stream=True`) para visualizar la salida en tiempo real y guarda automáticamente cada archivo de configuración en un directorio local.

# Integrantes del Grupo
* **Matías Peralta** 
* **Claudio Zambra** 
* **Hernán Vera** 
