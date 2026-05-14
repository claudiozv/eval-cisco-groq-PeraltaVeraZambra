# eval-cisco-groq-PeraltaVeraZambra
# Asignatura: Redes Avanzadas 1

# Generador Inteligente de Configuraciones Cisco IOS con Groq + Python

## Descripción del Proyecto
Este proyecto consiste en una aplicación de consola en Python, nombrada `cisco_config_gen.py`. La herramienta recibe descripciones de escenarios de red y utiliza Python y Groq para generar bloques de configuración Cisco IOS reales y listos para ser implementados. El sistema utiliza un system prompt especializado para asegurar que el modelo devuelva únicamente comandos válidos, sin texto explicativo adicional fuera de los comentarios de IOS. Además, emplea respuestas en streaming (`stream=True`) para visualizar la salida en tiempo real y guarda automáticamente cada archivo de configuración en un directorio local.

# Integrantes del Grupo
* **Matías Peralta** Desarrollador
* **Hernán Vera** Readme/Validaciones
* **Claudio Zambra** Lider del proyecto/Arquitectura general
## Requisitos
- Python 3.10 o superior
- Cuenta en [Groq] con API Key activa
- Git instalado
## Instrucciones de Instalación
1.- Clonar el repositorio 

2.- Crear y activar el entorno virtual

3.- Instalar dependenicas

4.- Configurar API Key

5.- Ejecutar la aplicación 
## Escenarios y Funciones

* **Escenario A (VLANs y Trunking):** El usuario ingresa una lista de VLANs con sus nombres y los puertos asignados para configurar un switch de capa 2.
* **Escenario B (OSPF):** El usuario proporciona el ID del proceso de enrutamiento, las redes que se desean anunciar y las áreas correspondientes para configurar un router.
* **Escenario C (Subnetting e IP):** El usuario define una red base, un prefijo y la cantidad de subredes necesarias para asignar direcciones IP a las interfaces.

* **Escenario D (ACL):** El usuario define los siguientes parámetros, red de origen, red de destino, si va a permitir o denegar el tráfico, la interfaz donde se aplicara la ACL y por último si el tráfico de paquetes es entrante o saliente (in/out).

Todas las salidas generadas se almacenan automáticamente en la carpeta `/configs/` utilizando la nomenclatura `escenario_{tipo}_{timestamp}.txt`.
## Justificación de Parámetros del Modelo

**Model: llama-3.3-70b-versatile** **¿Por qué?**
Se utilizo este modelo porque genera comandos Cisco IOS más precisos y completos.
**Temperature: 0.1 ¿Por qué?**
La temperatura controla qué tan "creativo" o "aleatorio" es el modelo al generar texto, al estar en 0.1 nos entregara comandos más técnicos.
**Max_tokens: 1024 ¿Por qué?**
Escogimos esta cantidad para dejar el margen suficiente para todos los escenarios del proyecto.
**Stream: True ¿Por qué?** 
Esto hace que la respuesta se vaya viendo paso a paso como se va creando y no aparece un mensaje de golpe con todo el comando.

## Limitaciones Conocidas
- La carpeta `/configs/` se acumula con cada ejecución y debe limpiarse manualmente.
- La entrada del usuario es texto libre, no validamos rangos antes de enviar a la API.

*Evaluación Práctica · Generador Cisco con Groq · INACAP La Serena · 2026*

