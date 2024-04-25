<div align="center">
  
  ![Logo del Proyecto](https://avatars.githubusercontent.com/u/14185940?s=200&v=4.png)

</div>
<!-- Título principal -->
 <h1 align="center"> RAG with LLM API </h1>

<!-- Descripción del proyecto -->
<p align="center">Este proyecto implementa una solución simple de tipo RAG (retrieved augmented generation) utilizando un LLM (large language model) a través de una API desarrollada con FastAPI en Python. La API permite a los usuarios hacer preguntas sobre un documento específico y recibir respuestas generadas por el LLM.</p>

<!-- Separador -->
<hr>

<!-- Subtítulo de Características -->
<h2>Características</h2>

<!-- Lista de características -->
<ul>
  <li>Desarrollado con <strong>FastAPI</strong> en Python.</li>
  <li>Utiliza <strong>Cohere</strong> para la generación de respuestas.</li>
  <li>Almacena fragmentos del documento en <strong>ChromaDB</strong> para la búsqueda de contextos relevantes.</li>
  <li>Incluye manejo de errores para una experiencia robusta.</li>
  <li>Ofrece una estructura organizada y modular.</li>
</ul>

<!-- Subtítulo de Requisitos -->
<h2>⚙️ Requisitos</h2>

<!--  Lista de requisitos -->
<ul>
  <li>Python 3.7 o superior.</li>
  <li>Acceso a internet para comunicación con Cohere API.</li>
</ul>

<!-- Subtítulo de Instalación -->
<h2>🛠️ Instalación</h2>

<!-- Pasos de instalación -->
<ol>
  <li>Clona este repositorio en tu máquina local:</li>
</ol>

git clone https://github.com/tu_usuario/rag-with-llm-api.git

<ol start="2">
  <li>Accede al directorio del proyecto:</li>
</ol>
bash
 
cd rag-with-llm-api
<ol start="3">
  <li>Crea un entorno virtual e instala las dependencias:</li>
</ol>
bash
 
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
<ol start="4">
  <li>Configura las variables de entorno en un archivo <code>.env</code>:</li>
</ol>
plaintext
 
COHERE_API_KEY=tu_clave_de_api_de_cohere
<!-- Subtítulo de Uso -->
<h2>🚀 Uso</h2>
<!-- Pasos de uso -->
<ol>
  <li>Inicia el servidor de desarrollo:</li>
</ol>
bash
 
uvicorn app.main:app --reload
<ol start="2">
  <li>Abre tu navegador y visita <code>http://localhost:8000/docs</code> para acceder a la documentación de la API Swagger.</li>
  <li>Realiza una solicitud POST a <code>/ask/</code> con el siguiente JSON en el cuerpo de la solicitud:</li>
</ol>
json
 
{
    "user_name": "John Doe",
    "question": "How are you today?"
}
<!-- Subtítulo de Contribución -->
<h2>🤝 Contribución</h2>
<!-- Instrucciones de contribución -->
<p>¡Toda contribución es bienvenida! Si deseas contribuir al proyecto, sigue estos pasos:</p>
<ol>
  <li>Haz un fork del repositorio.</li>
  <li>Crea una nueva rama (<code>git checkout -b feature/nueva-funcionalidad</code>).</li>
  <li>Realiza tus cambios y haz commit (<code>git commit -am 'Agrega nueva funcionalidad'</code>).</li>
  <li>Sube tus cambios a tu fork (<code>git push origin feature/nueva-funcionalidad</code>).</li>
  <li>Crea un nuevo Pull Request.</li>
</ol>
<!-- Subtítulo de Licencia -->
<h2>📝 Licencia</h2>
<!-- Licencia -->
<p>Este proyecto está bajo la licencia <a href="LICENSE">MIT</a>.</p>
