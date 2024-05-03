import java.util.Scanner;
public class Faktorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Zadejte číslo: ");
        int n;

        try {
            n = input.nextInt();
            System.out.println("Faktoriál " + n + " je: " + faktorialRekuze(n));
            System.out.println("Faktoriál " + n + " je: " + faktorial(n));
        } catch (Exception e) {
            System.out.println("Špatný vstup, zadejte číslo");
        }


    }
    public static int faktorialRekuze(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * faktorialRekuze(n - 1);
        }
    }
    public static int faktorial(int n) {
        int vysledek = 1;
        for (int i = 1; i <= n; i++) {
            vysledek *= i;
        }
        return vysledek;
    }
}