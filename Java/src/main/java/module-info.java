module com.example.butterflyscene {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.ikonli.javafx;
    requires jdk.jsobject;
    requires org.json;

    opens com.example.butterflyscene to javafx.fxml;
    exports com.example.butterflyscene;
}