import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TableCell;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.util.Callback;

import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.Registry;

public class Controller {

    @FXML private TableView tableView;
    @FXML private TableColumn username;
    @FXML private TableColumn email;
    @FXML private TableColumn image;
    private Registry scene;
    public Button save;


    public Controller(){

    }

    public void saveUser(){
        System.out.println("Save");
    }

    public void fillUsername() throws RemoteException, NotBoundException {
        this.tableView = (TableView) this.scene.lookup("#user");
        this.username = (TableColumn) this.scene.lookup("#username");
        Callback<TableColumn<S, T>, TableCell<S, T>> tableColumnTableCellCallback = ;
        this.username.setCellFactory(tableColumnTableCellCallback);
    }
}
