import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.util.Callback;
import org.json.simple.parser.ParseException;

import java.io.IOException;
import java.rmi.registry.Registry;
import java.util.ArrayList;

public class Controller {

    @FXML private TableView<Person> user;
    @FXML private TableColumn<Person, String> username;
    @FXML private TableColumn<Person, String> email;
    @FXML private TableColumn<Person, String> image;

    @FXML private TextField nuser;
    @FXML private TextField nmail;
    @FXML private TextField nimage;

    private Registry scene;
    public Button save;
    private Parser parser;

    ArrayList<Person> data;

    public Controller() throws IOException {
        this.parser = new Parser();
        this.data = new ArrayList<>();
    }



    @FXML
    public void initialize() throws ParseException {
        fillUsers();
    }


    public void fillUsers() throws ParseException {
        username.setCellValueFactory(new PropertyValueFactory<>("username"));
        email.setCellValueFactory(new PropertyValueFactory<>("email"));
        image.setCellValueFactory(new PropertyValueFactory<>("image"));

        for(int i = 0; i < parser.length(); i++){
            String username = parser.username(i);
            String email = parser.email(i);
            String image = parser.image(i);
            this.data.add(new Person(username,email,image));
        }

        ObservableList<Person>  tabledata = FXCollections.observableArrayList(this.data);
        this.user.setItems(tabledata);
    }

    @FXML
    public void saveUser() throws ParseException, IOException {
        if(!this.nuser.getText().isEmpty() && !this.nmail.getText().isEmpty() && !this.nimage.getText().isEmpty()) {
            String username = this.nuser.getText();
            String email = this.nmail.getText();
            String image = this.nimage.getText();

            this.data.add(new Person(username, email, image));
            ObservableList<Person> tabledata = FXCollections.observableArrayList(this.data);
            this.user.setItems(tabledata);

            Connection.MySENDReq(username,email,image);

            this.nuser.clear();
            this.nmail.clear();
            this.nimage.clear();
        }else {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("LAN!!");
            alert.setHeaderText(null);
            alert.setContentText("BITTE ALLE FELDER AUSFÜLLEN!");

            alert.showAndWait();
        }
        //this.fillUsername();
    }

    public void deleteUser(ActionEvent actionEvent) {
        Person selectedItem = user.getSelectionModel().getSelectedItem();
        user.getItems().remove(selectedItem);

    }
}
