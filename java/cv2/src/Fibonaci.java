import java.util.Scanner;

import java.util.Scanner;
public class Fibonaci {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Zadejte číslo: ");
        int n;
        try {
            n = input.nextInt();
            if (n < 0) {
                System.out.println("Zadejte kladné číslo");
                return;
            }
            System.out.println("Fibonaciho posloupnost: " + fibonaci(n));
            System.out.println("Rekurzivni fibonaciho posloupnost: " + fibonaciRekurze(n));

        } catch (Exception e) {
            System.out.println("Špatný vstup, zadejte číslo");
        }

    }
    public static int fibonaciRekurze(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fibonaci(n - 1) + fibonaci(n - 2);
        }
    }
    public static int fibonaci(int n) {
        int a = 0;
        int b = 1;
        for (int i = 0; i < n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return a;
    }
}
