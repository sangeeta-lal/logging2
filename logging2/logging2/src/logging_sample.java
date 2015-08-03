

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class logging_sample
 {

  public static void main(String[] args) {

    Logger logger = Logger.getLogger("MyLog");
    FileHandler fh;

    try {

      // This block configure the logger with handler and formatter
      fh = new FileHandler("F:\\MyLogFile.log", true);
      logger.addHandler(fh);
      logger.setLevel(Level.SEVERE);
      SimpleFormatter formatter = new SimpleFormatter();
      fh.setFormatter(formatter);

      System.out.println("Helooo");
      // the following statement is used to log any messages   
      logger.log(Level.WARNING,"My first log");
      logger.log(Level.INFO,"hello");
      
    } catch (SecurityException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    }

  }

}