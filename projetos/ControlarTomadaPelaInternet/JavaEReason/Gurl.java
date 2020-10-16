import java.io.*;
import java.net.*;

public class Gurl {
    /** Faz a requisição GET especificada em urlToRead, recebe a resposta e a retorna como uma String.*/
   public static String getHTML(String urlToRead) throws Exception {
      StringBuilder result = new StringBuilder();
      URL url = new URL(urlToRead);
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setRequestMethod("GET");
      BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
      String line;
      while ((line = rd.readLine()) != null) {
         result.append(line);
      }
      rd.close();
      // System.out.println (conn.getResponseMessage());
      return result.toString();
   }

   public static void main(String[] args) throws Exception
   {
     System.out.println(getHTML(args[0]));
   }
}

