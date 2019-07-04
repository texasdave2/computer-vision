# yoda_detector_tensorflow IN PROGRESS

Everything is self-contained with very descriptive comments to help anyone at the most basic level 

All rights reserved for the yoda images as they certainly belong to Lucasfilm / Disney

The vast majority of code in the notebook comes from the ssd_mobilenet_v1 model config

DISCLAIMER:  This git is meant for those just learning object identification through tensorflow and not 
to be used for identifying yoda at the local cantina or anywhere near Mos Eisely.  Don't mess 
with Jedi and they won't mess with you yada yada yada...


This drop in folder assumes A LOT!  But, you can do it!!

You must install tensorflow-gpu (at least I think you do, that's my platform)
I'm running python3 on ubuntu 18.04 without conda, but this shouldn't matter.  I'm using 
an Nvidia GeForce 940MX gpu, the 390 driver.  If this is you, you'll need to install the nvidia driver
as well as ubuntu 17 Cuda 9.0 toolkit, patches as well as Cudnn libraries.  I can't possibly tell you how much 
a pain in the rear that is... Power through it you will.... you willlllllllllll.... 

Prereq's:

1)  

- You must download / clone the tensorflow git clone located here:
https://github.com/tensorflow/models
place the tensorflow models clone anywhere in your home/ folder. 

- have jupyter notebook on your machine
https://askubuntu.com/questions/737094/jupyter-notebook-installation


2)  Clone my git as well and place it in the following folder of your tensorflow file structure:
/models/research/object_detection

you need this yoda detector clone to be located at:
/models/research/object_detection/yoda_detector


3)  Simply run all the cells on the jupyter notebook file:  yoda_object_detection.ipynb
for immediate satisfaction OR

4) It will detect yoda from various images you feed it inside the 'identify_images' folder

5) If you want to get bold, you can mess with the parameters in the config file and change how 
it is trained.  This takes some razzle dazzle with clearning folders and setting things up
but I believe the force is with you and I documented things pretty well.

6) The commands on the CLI are in a folder in text docs, help you they will young padawan
