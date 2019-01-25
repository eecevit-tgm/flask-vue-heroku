import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class WindowStarter extends Application {

    public static void main(String[] args) {
        Application.launch(WindowStarter.class, args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("crud.fxml"));

        stage.setTitle("CRUD Simple User Database");
        stage.setScene(new Scene(root, 900, 800));



        stage.show();
    }
}