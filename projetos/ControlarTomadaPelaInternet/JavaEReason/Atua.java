import java.util.StringTokenizer;
import java.util.NoSuchElementException;
import java.io.IOException;
import java.net.ProtocolException;
import java.net.MalformedURLException;
import java.lang.SecurityException;

class Atua {
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
    /** Informa o estado, armazenado no servidor, do ventilador: true=ligado, false=desligado. */
    public static boolean getVent () {
        double d=getValue ("http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/d12");
        return d>0.5;   // 0.5 é arbitrário, só para converter o tipo.
    }
    /** Informa o estado, armazenado no servidor, do umidificador: true=ligado, false=desligado. */
    public static boolean getUm () {
        double d=getValue ("http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/d13");
        return d>0.5;   // 0.5 é arbitrário, só para converter o tipo.
    }
    /** Informa o estado, armazenado no servidor, da lâmpada: true=ligado, false=desligado. */
    public static boolean getLamp () {
        double d=getValue ("http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/d15");
        return d>0.5;   // 0.5 é arbitrário, só para converter o tipo.
    }

    /** Ajusta o estado, armazenado no servidor, do ventilador: true=ligado, false=desligado. */
    public static void setVent (boolean s) {
        String URL="http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d12?value=";
        if (s) URL+="1";
        else URL+="0";
        getValue (URL);
    }
    /** Ajusta o estado, armazenado no servidor, do umidificador: true=ligado, false=desligado. */
    public static void setUm (boolean s) {
        String URL="http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d13?value=";
        if (s) URL+="1";
        else URL+="0";
        getValue (URL);
    }
    /** Ajusta o estado, armazenado no servidor, da lâmpada: true=ligado, false=desligado. */
    public static void setLamp (boolean s) {
        String URL="http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d15?value=";
        if (s) URL+="1";
        else URL+="0";
        getValue (URL);
    }
    /** Teste */
    public static void main (String args[]) {
        System.out.print ("lamp=" + getLamp());
        System.out.print ("; vent=" + getVent());
        System.out.print ("; um=" + getUm() + ";");

        // setLamp(false);
        // setVent(false);
    }
}

