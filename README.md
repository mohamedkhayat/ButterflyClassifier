## ButterflyClassifier

**ButterflyClassifier** is an application that integrates Java and Python to classify butterfly species. The application leverages JavaFX for the graphical user interface (GUI) and uses Flask to communicate with a Python backend. The backend processes images with a fine-tuned VGG model trained in PyTorch and sends classification results back to the Java application.

![Butterfly Classification](https://github.com/user-attachments/assets/6d2601c7-4664-4e59-b822-ed584248024b)

### Technologies Used

- **Java & JavaFX:** For the GUI and file selection.
- **Python & Flask:** For handling requests and interfacing with the PyTorch model.
- **PyTorch:** For image classification.

### To Use This App

1. **Install PyTorch:** Ensure you have PyTorch installed in your Python environment.

2. **Download the Model:**
   - Download the `.pth` file from the Dropbox link: [butterfly_model.pth](https://www.dropbox.com/scl/fi/4fee601p77854l1mgjfp8/butterfly_model.pth?rlkey=ddxsjjkkyzti5ngpwt84jtoba&st=kgndiuk1&dl=0)
   - Place the downloaded file into the `python` folder.

3. **Run the Backend:**
   - Execute `app.py` in your Python environment to start the Flask server.

4. **Launch the Java Application:**
   - Open the Java application to interact with the GUI, select images, and view classification results.

### Dataset

The model is trained using the [Butterfly Image Classification dataset](https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification/data) available on Kaggle.
