import javafx.beans.property.SimpleStringProperty;

public class Person {

    private SimpleStringProperty username;
    private SimpleStringProperty email;
    private SimpleStringProperty image;


    public Person(String username, String email, String image) {
        this.username = new SimpleStringProperty(username);
        this.email = new SimpleStringProperty(email);
        this.image = new SimpleStringProperty(image);
    }

    public String getUsername() {
        return this.username.get();
    }

    public String getEmail() {
        return this.email.get();
    }

    public String getImage(){
        return this.image.get();
    }

    public void setUsername(String username) {
        this.username = new SimpleStringProperty(username);
    }

    public void setEmail(String email) {
        this.email = new SimpleStringProperty(email);
    }

    public void setImage(String image){
        this.image = new SimpleStringProperty(image);
    }
}