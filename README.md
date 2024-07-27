# ButterflyClassifier

This project is a Butterfly Classification application that combines Java and Python. The application utilizes JavaFX for the graphical user interface (GUI), including file selection. Images selected through the Java-based GUI are sent to a Python backend using Flask.

In the Python backend, the image is processed and fed into a fine-tuned VGG model trained with PyTorch to classify butterfly species. The prediction results are then sent back to the Java application for display.


https://github.com/user-attachments/assets/6d2601c7-4664-4e59-b822-ed584248024b


Technologies Used:

Java & JavaFX: For GUI and file selection.
Python & Flask: For handling requests and interfacing with the PyTorch model.
PyTorch: For image classification.
To use this app:

Make sure you have pytorch installed

Download the .pth file from the provided Dropbox link : https://www.dropbox.com/scl/fi/4fee601p77854l1mgjfp8/butterfly_model.pth?rlkey=ddxsjjkkyzti5ngpwt84jtoba&st=kgndiuk1&dl=0

and insert it into the python folder.

Run app.py in the Python environment.

Launch the Java application to interact with the GUI.

The dataset used to train the model can be found here : https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification/data
