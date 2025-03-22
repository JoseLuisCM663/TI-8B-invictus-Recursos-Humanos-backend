# Cómo levantar un proyecto de Uvicorn con FastAPI

Sigue estos pasos para levantar un proyecto de FastAPI utilizando Uvicorn:

## Requisitos previos
1. **Python instalado**: Asegúrate de tener Python 3.7 o superior instalado.
2. **Instalar FastAPI y Uvicorn**:
    ```bash
    pip install fastapi uvicorn
    ```

## Pasos para levantar el proyecto

1. **Crea un archivo principal** (por ejemplo, `main.py`):
 

2. **Ejecuta el servidor con Uvicorn**:
    En la terminal, ejecuta el siguiente comando:
    ```bash
    uvicorn main:app --reload
    ```

    - `main` es el nombre del archivo (sin la extensión `.py`).
    - `app` es la instancia de FastAPI creada en el archivo.
    - `--reload` habilita la recarga automática en desarrollo.

3. **Accede a la API**:
    - Abre tu navegador y ve a `http://127.0.0.1:8000` para ver la respuesta de la API.
    - La documentación interactiva estará disponible en `http://127.0.0.1:8000/docs`.

## Notas adicionales
- Para entornos de producción, considera usar un servidor como **Gunicorn** junto con Uvicorn.
- Puedes personalizar el puerto con la opción `--port`, por ejemplo:
  ```bash
  uvicorn main:app --reload --port 8080
  ```

¡Listo! Ahora tienes tu proyecto FastAPI corriendo con Uvicorn.