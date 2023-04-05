# BUZZBUSTERS PROJECT

# Mosquito Detection and Monitoring System
## Description
The Mosquito Detection and Monitoring System is a solution developed to prevent and control mosquito-borne diseases in the Santa Cruz region of Bolivia. The system uses image processing techniques and machine learning algorithms to detect the density and distribution of mosquitoes in real-time, allowing for early detection and prevention efforts.

The system includes a network of mosquito traps equipped with Raspberry Pi 3 for image capture and processing. The images are sent to Google Cloud Storage, where they are processed by machine learning models trained on Google AutoML. The results are then sent to Firebase, where they are displayed on an accessible dashboard for healthcare professionals and local authorities.

This project utilizes deep learning techniques for mosquito detection. The solution employs a camera and detection algorithm to identify and count mosquitoes in real-time. Detection is performed using a model trained on Google AutoML Vision. The application runs on a Raspberry Pi 3 and utilizes Google cloud services such as Cloud Storage and Firebase for storage and visualization of the results. The solution can be easily scaled using Docker containers and scalable cloud services like Vertex AI.

The solution also includes a mobile application for the public to report mosquito sightings and track the progress of mosquito control efforts in their area.

## Installation and configuration of the project
This project uses Python and Docker to create a real-time mosquito detection and monitoring system. To install and configure the project, follow the steps below:

### Prerequisites
This project was developed on Ubuntu 20.4.
Make sure you have Python 3 and Docker installed on your system before continuing.

### Prepare workspace
Install pip:
<pre>
<code class="copyable">
sudo apt install -y python3-pip
</code>
</pre>

Install other dependencies:
<pre>
<code class="copyable">
sudo apt install build-essential libssl-dev libffi-dev python3-dev
</code>
</pre>

Install virtual environment:
<pre>
<code class="copyable">
sudo apt install -y python3-venv
</code>
</pre>

Create virtual environment:
<pre>
<code class="copyable">
python3.8 -m venv mosquitoes
</code>
</pre>

Activate the virtual environment:
<pre>
<code class="copyable">
source mosquitoes/bin/activate
</code>
</pre>

### Step 1: Clone the repository

Clone the project repository from GitHub to your local directory:
<pre>
<code class="copyable">
git clone https://github.com/githubMauri/buzzbusters-project.git
</code>
</pre>

Navigate to the project directory:
<pre>
cd repository
</pre>

### Step 2: Install dependencies
This project uses the following Python libraries, which are specified in the "requirements.txt" file:

* certifi==2022.12.7
* charset-normalizer==3.1.0
* idna==3.4
* numpy==1.24.2
* opencv-python==4.7.0.72
* requests==2.28.2
* urllib3==1.26.15

To install the dependencies, run the following command:
<pre>
<code class="copyable">
pip install -r requirements.txt
</code>
</pre>

### Step 3: Configure the model
To run the model, you need to configure the location of the local model.

The saved_model.pb file is in the "mounted_model" folder.

This is the path where the saved_model.pb file is located on my computer: 

YOUR_LOCAL_MODEL_PATH=/home/iruam/Documentos/deploy-mosquitoes-cpu/mounted_model

Set the YOUR_LOCAL_MODEL_PATH variable to the path where the saved_model.pb file is located on your computer:
<pre>
<code class="copyable">
YOUR_LOCAL_MODEL_PATH=/path/to/mounted_model
</code>
</pre>

### Step 4: Run the model
To run the model in a Docker container, you first need to download the Docker image of the container:

Set the CPU_DOCKER_GCR_PATH variable:
<pre>
<code class="copyable">
export CPU_DOCKER_GCR_PATH=gcr.io/cloud-devrel-public-resources/gcloud-container-1.14.0:latest
</code>
</pre>

Download the Docker image:
<pre>
<code class="copyable">
sudo docker pull ${CPU_DOCKER_GCR_PATH}
</code>
</pre>

Then, run the following command to start the Docker container and run the model:

Set the container name:
<pre>
<code class="copyable">
CONTAINER_NAME=automl_high_accuracy_model_cpu
</code>
</pre>

Set the port number:
<pre>
<code class="copyable">
PORT=8501
</code>
</pre>

Run the Docker container:
<pre>
<code class="copyable">
sudo docker run --rm --name ${CONTAINER_NAME} -p ${PORT}:8501 -v ${YOUR_LOCAL_MODEL_PATH}:/tmp/mounted_model/0001 -t ${CPU_DOCKER_GCR_PATH}
</code>
</pre>

### Step 5: Configure the camera (optional)
If you are working on Ubuntu and your camera is not automatically recognized, you can use the following command to list the available cameras:
<pre>
<code class="copyable">
v4l2-ctl --list-devices
</code>
</pre>

Identify the index of the camera and change the value in the following line of code:
<pre>
<code class="copyable">
cap = cv2.VideoCapture(1)
</code>
</pre>

### Step 6: Run the project
Once everything is configured, execute the following command to test the model with a webcam:
<pre>
<code class="copyable">
python webcam_testing.py
</code>
</pre>

To test the model with a video:
<pre>
<code class="copyable">
python video_testing.py
</code>
</pre>


<img src="https://github.com/githubMauri/buzzbusters-project/blob/master/images/image1.jpg" alt="model-training" width="500" height="500">
