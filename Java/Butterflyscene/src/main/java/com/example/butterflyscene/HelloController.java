package com.example.butterflyscene;
import javafx.fxml.FXML;
import javafx.geometry.Rectangle2D;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import netscape.javascript.JSObject;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;
import java.util.Base64;
import java.util.Scanner;
import java.io.File;
import org.json.JSONObject;
public class HelloController {
    @FXML
    private Button select;
    @FXML
    private Label Prediction;
    @FXML
    private ImageView Imview;
    private File selectedFile;
    private Image resizeImage(Image image, double targetWidth, double targetHeight) {
        ImageView imageView = new ImageView(image);
        imageView.setPreserveRatio(true);
        imageView.setFitWidth(targetWidth);
        imageView.setFitHeight(targetHeight);
        return imageView.snapshot(null, null);
    }
    @FXML
    private void OpenFileChooser(){
        Imview.setImage(null);
        Prediction.setText(null);
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Select File");
        FileChooser.ExtensionFilter extensionFilter = new FileChooser.ExtensionFilter("Image Files", "*.jpg", "*.png");
        fileChooser.getExtensionFilters().add(extensionFilter);
        fileChooser.setInitialDirectory(new File(System.getProperty("user.home")+File.separator+"Downloads"));

        Stage stage = (Stage) select.getScene().getWindow();
        selectedFile = fileChooser.showOpenDialog(stage);

        if (selectedFile != null){
            Image image = new Image(selectedFile.toURI().toString());
            Image resizedImage = resizeImage(image, 400, 300);
            Imview.setImage(resizedImage);

            double width = resizedImage.getWidth();
            double height = resizedImage.getHeight();
            double offsetX = (width - Imview.getFitWidth()) / 2;
            double offsetY = (height - Imview.getFitHeight()) / 2;

            // Create a viewport to center the image
            Imview.setViewport(new Rectangle2D(offsetX, offsetY, Imview.getFitWidth(), Imview.getFitHeight()));
        }
    }
    private String encodeFile_B64(File file) throws Exception{
        try {
            FileInputStream fileInputStream = new FileInputStream(file);
            byte[] bytes = new byte[(int)file.length()];
            fileInputStream.read(bytes);
            fileInputStream.close();
            return Base64.getEncoder().encodeToString(bytes);
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
            return "error";
        }
    }
    @FXML
    private void Predict() throws IOException {
        if(selectedFile !=null) {
            try {
                URL url = new URL("http://localhost:5000/predict");
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("POST");
                connection.setRequestProperty("Content-Type", "application/json");
                connection.setDoOutput(true);
                String ImageData = encodeFile_B64(selectedFile);
                String inputJson = "{\"image\": \"" + ImageData + "\"}";

                connection.getOutputStream().write(inputJson.getBytes());
                connection.getOutputStream().flush();

                if (connection.getResponseCode() != HttpURLConnection.HTTP_OK) {
                    throw new RuntimeException(("Failed : HTPP error code : " + connection.getResponseCode()));
                }

                Scanner scanner = new Scanner(connection.getInputStream());
                StringBuilder response = new StringBuilder();

                while (scanner.hasNextLine()) {
                    response.append(scanner.nextLine());
                }
                scanner.close();
                System.out.println(response.toString());
                JSONObject jsonresponse = new JSONObject(response.toString());
                String confidence = String.format("%.2f", jsonresponse.getDouble("confidence") * 100);
                String label = jsonresponse.getString("label");

                Prediction.setText(label + ": " + confidence + "%");
                connection.disconnect();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        else{
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("Please select an image");
            alert.showAndWait();
        }
    }

}