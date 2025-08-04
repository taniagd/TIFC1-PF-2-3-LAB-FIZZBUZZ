# Guía para Ejecutar los Tests de FizzBuzz en Python

Este documento explica el proceso paso a paso para ejecutar los tests automatizados del programa FizzBuzz.

📌Paso 1: Verificar la instalación de Python

Antes de ejecutar los tests, asegúrate de tener Python instalado en tu sistema. Puedes verificarlo abriendo una terminal o línea de comandos y escribiendo: python --version. En algunos otros sistemas, puede ser: `python3 --version` 

Si Python está instalado, verás la versión que tienes (por ejemplo, Python 3.9.7). Si no, necesitarás instalarlo.

📌Paso 2: Navegar hasta la carpeta del proyecto

Abre una terminal y usa el comando `cd` (change directory) para moverte a la carpeta donde se encuentran los archivos del proyecto.

📌Paso 3: Copia y pega el contenido del archivo test.py en tu propia carpeta donde almacenaste el ejercicio. 

📌Paso 4: Instalar Pytest (si no lo tienes)

Si es la primera vez que lo usas en tu entorno, necesitarás instalarlo. En la terminal, ejecuta el siguiente comando: `pip install pytest` 
Esto descargará e instalará el paquete pytest. Solo necesitas hacer esto una vez por entorno de Python.

📌Paso 5: Ejecutar el script de test

Asegurándote de que estás en la carpeta correcta del proyecto, ejecuta el comando: `python -m pytest test.py`

📌Paso 6: Interpretar el resultado

Después de ejecutar el comando, la terminal te mostrará un resultado. Hay dos escenarios principales:

Si los tests pasan: Verás un mensaje que dice algo como `1 passed` o una línea final con `== 1 passed in ... ==`. Esto significa que tu código de FizzBuzz funciona correctamente.

Si los tests fallan: Verás un mensaje que indica `FAILED`. El reporte será más detallado, te mostrará qué test falló, en qué línea y por qué. Esto es útil para que puedas volver a tu código, corregir el error y volver a ejecutar el test.

Sigue estos pasos y, una vez que el test haya pasado, habrás completado la tarea. 


