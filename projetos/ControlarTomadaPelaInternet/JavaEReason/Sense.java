import java.util.StringTokenizer;
import java.util.NoSuchElementException;
import java.io.IOException;
import java.net.ProtocolException;
import java.net.MalformedURLException;
import java.lang.SecurityException;

class Sense {
/** Faz a requisição GET definida em getURL, converte o resultado recebido que, espera-se, seja um String contendo uma lista em JSON contendo um número em um double e retorna esse double.
*/
    private static double getValue (String getURL) {
        double d=-1.0;
        StringTokenizer result=null;
        try {
            result = new StringTokenizer(Gurl.getHTML(getURL), "\""); 
        } catch (ProtocolException e) {
            System.out.println ("erro de comunicação - é possível que a requisição não tenha sido atendida.");
            e.printStackTrace();
        } catch (MalformedURLException e) {
            System.out.println ("Erro de sintaxe na URL");
            e.printStackTrace();        
        } catch (SecurityException e) {
            System.out.println ("Faltam permissões de segurança?");
            e.printStackTrace();
        } catch (Exception e) {
            System.out.println ("Catcher genérico - não achei qual é a exceção específica.");
            e.printStackTrace();
        }
        
        while (result.hasMoreTokens()) {
            String buf= result.nextToken();
            try {
                d=Double.parseDouble(buf);
            } catch (NumberFormatException e) {
                // System.out.println ("não é double");
                // continua
            } catch (NoSuchElementException e) {
                System.out.println ("lista de tokens vazia!");
                e.printStackTrace();
            }
            // System.out.println (buf);
        }
        return d;
    }
    /** Informa o valor, armazenado no servidor, da leitura mais recente de temperatura do sensor DHT22. */
    public static double getTemp () {
        return getValue ("http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/v6");
    }
    /** Informa o valor, armazenado no servidor, da leitura mais recente de umidade do sensor DHT-22. */
    public static double getUm () {
        return getValue ("http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/v5");
    }
    /** Informa o valor, armazenado no servidor, da leitura mais recente do sensor de Luz - Um LDR conectado à entrada analógica do ESP8266, que tem resolução de 10bits (valores inteiros de 0 a 1023).(https://randomnerdtutorials.com/esp8266-adc-reading-analog-values-with-nodemcu/) */
    public static double getLuz () {
        return getValue ("http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/v1");
    }
    
    public static void main (String args[]) {
        System.out.print ("luz=" + getLuz());
        System.out.print ("; temperatura=" + getTemp());
        System.out.print ("; umidade=" + getUm() + ";");
    }
}

