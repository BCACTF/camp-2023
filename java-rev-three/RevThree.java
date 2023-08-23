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
        int[] offsets = {102, 192, 204, 145, 165, 180, 94, 118, 126, 153, 165, 124, 138, 111, 125, 92, 138, 109, 128, 147, 118, 164, 131, 145, 118, 132, 91, 103, 130, 138, 162, 76, 91, 111, 52, 64, 154};

        for (int i = 0; i < passwordGuess.length()-1; i++) {
            int firstChar = passwordGuess.charAt(i)+128;
            int secondChar = passwordGuess.charAt(passwordGuess.length()-i-1);

            if (firstChar-secondChar != offsets[i]) {
                return false;
            }
        }

        return true;
    }
}