package src;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JsonObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.IOException;

public class Parser {

    private String data;
    private JSONParser parser;

    public Parser() throws IOException {
        this.parser = new JSONParser();
        this.data = Connection.MyGETRequest();
        /*
        try {
            Object obj = parser.parse(this.data);
            JSONArray array = (JSONArray)obj;
            //System.out.println(array.size());
            //JSONObject obj2 = (JSONObject)array.get(1);
            //System.out.println(obj2.get("username"));

        } catch (org.json.simple.parser.ParseException e) {
            e.printStackTrace();
        }*/

    }

    public String username(int pos) throws ParseException {
        Object obj = this.parser.parse(this.data);
        JSONArray array = (JSONArray)obj;
        JSONObject obj2 = (JSONObject)array.get(pos);
        String name = (String) obj2.get("username");
        return name;
    }


    public String email(int pos) throws ParseException{
        Object obj = this.parser.parse(this.data);
        JSONArray array = (JSONArray)obj;
        JSONObject obj2 = (JSONObject)array.get(pos);
        String email = (String) obj2.get("email");
        return email;

    }

    public String image(int pos) throws ParseException{
        Object obj = this.parser.parse(this.data);
        JSONArray array = (JSONArray)obj;
        JSONObject obj2 = (JSONObject)array.get(pos);
        String img = (String) obj2.get("picture");
        return img;

    }

    public int length() throws ParseException {
        Object obj = this.parser.parse(this.data);
        JSONArray array = (JSONArray)obj;
        int length = array.size();
        return length;
    }

}
