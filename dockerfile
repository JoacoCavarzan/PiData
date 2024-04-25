# Usa la imagen base de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la carpeta actual al contenedor en /app
COPY . .

# Expone el puerto predeterminado por fastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]