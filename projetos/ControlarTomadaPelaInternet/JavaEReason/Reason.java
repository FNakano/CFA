// http://www.dsc.ufcg.edu.br/~jacques/cursos/map/html/threads/timer.html
import java.util.Timer;
import java.util.TimerTask;
import java.awt.Toolkit;

public class Reason {
    Toolkit toolkit;
    Timer timer;

    public Reason() {
        toolkit = Toolkit.getDefaultToolkit();
        timer = new Timer();
        timer.schedule(new ReasonTask(),
                       0,        //initial delay
                       30*1000);  //subsequent rate: 30 segundos
    }

    class ReasonTask extends TimerTask {
        /* task é percorrido do fim para o começo */
        boolean tasks[][]= {
          // lamp, vent, um
            {false, false, false},
            {false, false, false}, // quinto minuto tudo desligado.
            {true, true, false},
            {true, true, false}, // quarto minuto lâmpada e ventilador
            {true, false, false},
            {true, false, false},  // terceiro minuto só lâmpada
            {false, false, true},
            {false, false, true},  // segundo minuto só umidificador
            {false, false, false},   
            {false, false, false}  // primeiro minuto tudo desligado
        };
        int currentTask = tasks.length-1;
        /** Age sobre a lâmpada, ventilador e umidificador */
        private void act () {
            Atua.setLamp(tasks[currentTask][0]);
            Atua.setVent(tasks[currentTask][1]);
            Atua.setUm(tasks[currentTask][2]);
        }
        
        public void run() {
            if (currentTask > 0) {
                System.out.print (currentTask + ";");
                act();       
                Sense.main (new String[0]);
                Atua.main (new String[0]);
                System.out.println ();
                toolkit.beep();
                //System.out.println("Beep!");
                currentTask--;
            } else {
                toolkit.beep(); 
                System.out.println("Time's up!");
                //timer.cancel(); // Not necessary because
                                  // we call System.exit
                System.exit(0);   // Stops the AWT thread 
                                  // (and everything else)
            }
        }
    }
    public static void main(String args[]) {
        new Reason();
        System.out.println("Task scheduled.");
    }
}
