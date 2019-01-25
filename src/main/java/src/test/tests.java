package test;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.ArrayList;

public class MyTestRunner {

    @Test
    public void readUser() {
        // Arrange
        final int expected = 4;

        // Act

        // Assert

    }

    @Test
    public void saveUser(){
        ArrayList<Person> data = new ArrayList<>();
        data.add(new Person(username, email, image));
    }

}