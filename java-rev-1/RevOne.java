import java.util.Scanner;

public class RevOne {
   public static void main(String[] args) {
      System.out.println("Enter the password: ");
      Scanner scanner = new Scanner(System.in);

      String line = scanner.nextLine();

      if (checkPassword(line)) {
         System.out.println("That's the right password!");
      } else {
         System.out.println("That's the incorrect password!");
      }

      scanner.close();
   }

   public static boolean checkPassword(String passwordGuess) {
      String[] flagSegments = {"C0nGr4TulAt1OnS", "Y0u", "4Re", "J4v4", "Pr0"};

      String flag = "camp{"+String.join("_", flagSegments)+"}";

      return flag.equals(passwordGuess);
   }
}