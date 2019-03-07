# Face-Recognition

Project on Face Recognition using OpenCV

We will implement a classical face recognition system using OpenCV library. The process will be carried out in two phases.

  - **Face Detection**
  - **Face Recognition**
  
Before we get started, you need to install some libraries. 

1. First of all you will need **Python 3.5** or more in your computer. You can easily check if it is installed by typing "python" in your terminal/command prompt. If not, [install python](https://www.python.org/downloads/) .

2. Now you need **OpenCV**. For this, you can run the command *pip install opencv-python* and *pip install opencv-contrib-python*. Here is a detailed information of how you can [install OpenCV](https://pypi.org/project/opencv-python/).

That's it! You can now start writing your own programs and access OpenCV's power to do various Computer Vision projects. So let's get started with face detection.

## Face detection 

*Don't feel like reading the information below and want to directly get started with the implemenation??? Run this command and your face will be detected*

> python face_detection.py

Face detection is used nowadays in many kinds of applications like smartphone cameras, human computer interaction, social media and surveillance. It can be done using various pre-trained models which can do the heavy lifting for us to detect faces. OpenCV has various cascade classifiers which can detect faces with their different aspects like eye, nose and lips location. They are saved in a  XML file which we can access easily. There are line features, edge features and rectangle features in these models.

A Haar Cascade is basically a classifier which is used to detect particular objects from the source. The haarcascade_frontalface_default.xml is a haar cascade designed by OpenCV to detect the frontal face. A Haar Cascade works by training the cascade on thousands of negative images with the positive image superimposed on it. The haar cascade is capable of detecting features from the source. You can [explore more](
https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html) about Haar Cascade for face detection.

The program *face_detection.py* is able to locate the face in the given image using the same Cascade Classifier. Just make sure to specify the path where the haarcascade_frontalface_default.xml file is stored. I have uploaded the xml file in the repo. **It is recommended that you store this haarcascade_frontalface_default.xml file in the same folder where the face_detection.py is present.** You can [download](https://github.com/opencv/opencv/tree/master/data/haarcascades) various xml files and try diffrent things other than only face detection.

## Create Dataset

> python create_dataset.py

This script is used to store the facial images in the database which will be used to train the recognizer. Storing whole image will make it difficult to recognize the faces. Hence we will crop only the face from the captured image and store it to the folder. The rectangle that we drew over the face in the face_detection.py script, same concept will be applied to store the facial image. We have the co-ordinates of the rectangle which we can use to crop the image from the video. The script will create a folder named dataset where it will store all the images. If the folder is not present, it will do that for you!
One thing to notice is that we store the images in grayscale format. This is because the algorithm we use needs black and white images. It will further be explained when we talk about LBPH recognizer.  

 
This was all about face detection. I will keep updating the repo as soon as I finish the further modules. Till then, **Happy Coding**
