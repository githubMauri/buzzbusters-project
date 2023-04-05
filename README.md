# PROYECTO BUZZBUSTERS

# Sistema de Detección y Monitoreo de Mosquitos
## Descripción

El Sistema de Detección y Monitoreo de Mosquitos es una solución desarrollada para prevenir y controlar enfermedades transmitidas por mosquitos en la región de Santa Cruz, Bolivia. El sistema utiliza técnicas de procesamiento de imágenes y algoritmos de aprendizaje automático para detectar la densidad y distribución de mosquitos en tiempo real, lo que permite la detección temprana y los esfuerzos de prevención.

El sistema incluye una red de trampas para mosquitos equipadas con Raspberry Pi 3 para la captura y el procesamiento de imágenes. Las imágenes se envían a Google Cloud Storage, donde son procesadas por modelos de aprendizaje automático entrenados en Google AutoML. Los resultados se envían luego a Firebase, donde se muestran en un panel accesible para profesionales de la salud y autoridades locales.

Este proyecto utiliza técnicas de aprendizaje profundo (Deep Learning) para la detección de mosquitos. La solución utiliza una cámara y un algoritmo de detección para identificar y contar mosquitos en tiempo real. La detección se realiza mediante el uso de un modelo entrenado en Google AutoML Vision. La aplicación se ejecuta en una Raspberry Pi 3 y utiliza servicios en la nube de Google, como Cloud Storage y Firebase, para el almacenamiento y la visualización de los resultados. La solución se puede escalar fácilmente mediante el uso de contenedores Docker y servicios en la nube escalables como Vertex AI.

La solución también incluye una aplicación móvil para que el público informe avistamientos de mosquitos y haga un seguimiento del progreso de los esfuerzos de control de mosquitos en su área.

## Instalación y configuración del proyecto

Este proyecto utiliza Python y Docker para crear un sistema de detección y monitoreo de mosquitos en tiempo real. Para instalar y configurar el proyecto, siga los siguientes pasos:

Requisitos previos
Este proyecto fue desarrollado en Ubuntu 20.4
Asegúrese de tener instalado Python 3 y Docker en su sistema antes de continuar.

### Preparar ambiente de trabajo

Instalar pip: 
<pre>
<code class="copyable">
sudo apt install -y python3-pip
</code>
</pre>

Instalar otras dependencias: 
<pre>
<code class="copyable">
sudo apt install build-essential libssl-dev libffi-dev python3-dev
</code>
</pre>

Instalar ambiente virtual: 
<pre>
<code class="copyable">
sudo apt install -y python3-venv
</code>
</pre>

Crear ambiente virtual: 
<pre>
<code class="copyable">
python3.8 -m venv mosquitoes
</code>
</pre>

Activar el ambiente virtual: 
<pre>
<code class="copyable">
source mosquitoes/bin/activate
</code>
</pre>

### Paso 1: Clonar el repositorio

Clone el repositorio del proyecto desde GitHub en su directorio local:
<pre>
<code class="copyable">
git clone https://github.com/username/repository.git
</code>
</pre>

Ir al directorio del proyecto: 
<pre>
cd repository
</pre>

### Paso 2: Instalar las dependencias
Este proyecto utiliza las siguientes bibliotecas de Python, que están especificadas en el archivo "requirements.txt":

* certifi==2022.12.7
* charset-normalizer==3.1.0
* idna==3.4
* numpy==1.24.2
* opencv-python==4.7.0.72
* requests==2.28.2
* urllib3==1.26.15

Para instalar las dependencias, ejecute el siguiente comando: 
<pre>
<code class="copyable">
pip install -r requirements.txt
</code>
</pre>

### Paso 3: Configurar el modelo
Para ejecutar el modelo, necesita configurar la ubicación del modelo local.

El archivo saved_model.pb está en la carpeta "mounted_model".

esta es la ruta donde se encuentra el archivo saved_model.pb en mi computadora
YOUR_LOCAL_MODEL_PATH=/home/iruam/Documentos/deploy-mosquitoes-cpu/mounted_model

Establece la variable YOUR_LOCAL_MODEL_PATH con la ruta donde se encuentra el archivo saved_model.pb en tu computadora: 
<pre>
<code class="copyable">
YOUR_LOCAL_MODEL_PATH=/path/to/mounted_model
</code>
</pre>

### Paso 4: Ejecutar el modelo
Para ejecutar el modelo en un contenedor de Docker, primero debe descargar la imagen de Docker del contenedor:

Establecer la variable CPU_DOCKER_GCR_PATH: 
<pre>
<code class="copyable">
export CPU_DOCKER_GCR_PATH=gcr.io/cloud-devrel-public-resources/gcloud-container-1.14.0:latest
</code>
</pre>

Descargar la imagen Docker: 
<pre>
<code class="copyable">
sudo docker pull ${CPU_DOCKER_GCR_PATH}
</code>
</pre>

Luego, ejecute el siguiente comando para iniciar el contenedor de Docker y ejecutar el modelo

Establecer el nombre del contenedor: 
<pre>
<code class="copyable">
CONTAINER_NAME=automl_high_accuracy_model_cpu
</code>
</pre>

Establecer el número del puerto: 
<pre>
<code class="copyable">
PORT=8501
</code>
</pre>

Ejecutar el contenedor de Docker: 
<pre>
<code class="copyable">
sudo docker run --rm --name ${CONTAINER_NAME} -p ${PORT}:8501 -v ${YOUR_LOCAL_MODEL_PATH}:/tmp/mounted_model/0001 -t ${CPU_DOCKER_GCR_PATH}
</code>
</pre>

### Paso 5: Configurar la cámara (opcional)
Si está trabajando en Ubuntu y su cámara no es reconocida automáticamente, puede usar el siguiente comando para listar las cámaras disponibles:
<pre>
<code class="copyable">
v4l2-ctl --list-devices
</code>
</pre>

identifique el indice de la camara y cambie el valor en la siguiente linea de codigo
<pre>
<code class="copyable">
cap = cv2.VideoCapture(1)
</code>
</pre>

### Paso 6: Ejecutar proyecto
Una vez configurado todo ejecutamos el siguiente comando para probar el modelo con una webcam:
<pre>
<code class="copyable">
python webcam_testing.py
</code>
</pre>

Para probar el modelo con un video:
<pre>
<code class="copyable">
python video_testing.py
</code>
</pre>


<img src="https://github.com/githubMauri/buzzbusters-project/blob/master/images/image1.jpg" alt="model-training" width="500" height="500">
