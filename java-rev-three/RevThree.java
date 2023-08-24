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
        double[] avgs = {112.0, 65.0, 71.0, 103.5, 104.5, 95.0, 65.0, 90.0, 96.0, 98.5, 83.5, 104.0, 100.0, 107.5, 50.5, 83.0, 71.0, 85.5, 89.0, 85.5, 71.0, 83.0, 50.5, 107.5, 100.0, 104.0, 83.5, 98.5, 96.0, 90.0, 65.0, 95.0, 104.5, 103.5, 71.0, 65.0, 112.0};

        for (int i = 0; i < passwordGuess.length()-1; i++) {
            int firstChar = passwordGuess.charAt(i)+128;
            int secondChar = passwordGuess.charAt(passwordGuess.length()-i-1);

            double avg = ((double) firstChar-128+secondChar)/2; 

            if (firstChar-secondChar != offsets[i] || Math.abs(avg-avgs[i]) > .003) {
                return false;
            }
        }

        return true;
    }
}