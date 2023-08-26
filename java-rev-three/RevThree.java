import java.util.Scanner;

public class RevThree {
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
        int[] distanceBetweenChars = {-14, -23, -10, 10, 9, 46, -64, -3, 21, 10, 37, 35, 1, 22, -61, -11, 9, 4, -9, 26, -16, 14, -27, 66, -27, 7, 10, 38, 48, 5, 2, -51, 1, 13, -83, -37, 20};        
        String encryptString = "qxwfrKpXJeAChMnLCHbERWO2zc701ZPxURtFi";

        for (int i = 0; i < passwordGuess.length()-1; i++) {
            int firstChar = passwordGuess.charAt(i);
            int secondChar = encryptString.charAt(i);

            if (firstChar-secondChar != distanceBetweenChars[i]) {
                return false;
            }
        }

        return true;
    }
}