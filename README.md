# ButterflyClassifier

This project is a Butterfly Classification application that combines Java and Python technologies. The application utilizes JavaFX for the graphical user interface (GUI), including file selection. Images selected through the Java-based GUI are sent to a Python backend using Flask.

In the Python backend, the image is processed and fed into a fine-tuned VGG model trained with PyTorch to classify butterfly species. The prediction results are then sent back to the Java application for display.

Technologies Used:

Java & JavaFX: For GUI and file selection.
Python & Flask: For handling requests and interfacing with the PyTorch model.
PyTorch: For image classification.
To use this app:

Make sure you have pytorch and javafx installed
Download the .pth file from the provided Dropbox link and insert it into the python folder.
Run app.py in the Python environment.
Launch the Java application to interact with the GUI.
The dataset used to train the model can be found here : https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification/data
