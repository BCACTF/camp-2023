import java.util.Scanner;

public class RevTwo {
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
        int[] nums = {7267, 6113, 11757, 7152, 7675, 6345, 9823, 11463, 8821, 12339, 8019, 6739, 5983, 11476, 10344, 11057, 11603, 5087, 8791, 11956, 12115, 11982, 4820, 10719, 8787, 6835, 9059, 6901, 11090, 5605, 7677};

        for (int i = 0; i < passwordGuess.length(); i++) {
            if ((int) passwordGuess.charAt(i) != nums[i] % 128) {
                return false;
            }
        }

        return true;
    }
}