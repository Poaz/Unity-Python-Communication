Welcome to the AIP project template page

There is three different projects located in this repository.

1. A plain Unity-Python communication with a clean Unity scene.
2. A Unity scene with a robot setup for computer vision/navigation and Unity-Python communication.
3. A Unity scene with a humanoid rig and Unity-Python communication.


The Python code is made with Python 3.6 and needs one library called zmq, which you can use pip to install (pip install zmq).

The communication for each project is using the same base, which is 3 C# scripts to make an independent runable thread to handle communication in Unity, and 1 script in python as a server. 


