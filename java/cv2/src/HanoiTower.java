import java.util.Scanner;
import java.util.Stack;

public class HanoiTower {
    public static void main(String[] args) {
//        Scanner input = new Scanner(System.in);
//        System.out.print("Zadejte číslo kotoučů: ");

        try {
//            int n = input.nextInt();
            System.out.println("Přesuny 3 kotouče pomoci nonRecursiveHanoi");
            nonRecursiveHanoi('A', 'C', 'B');
            System.out.println("Přesuny 3 kotouče pomoci hanoiDFS");
            hanoiDFS(3, 'A', 'C', 'B');
        } catch (Exception e) {
            System.out.println("Špatný vstup, zadejte číslo");
        }

    }
    public static void hanoi(int n, char from, char to, char help) {
        if (n == 1) {
            System.out.println("Přesun disk z " + from + " na " + to);
        } else {
            hanoi(n - 1, from, help, to);
            System.out.println("Přesun disk z " + from + " na " + to);
            hanoi(n - 1, help, to, from);
        }
    }

    public static void nonRecursiveHanoi(char from, char to, char help){
        Stack<Move> stack = new Stack<>();
        stack.push(new Move(3, from, to, help));
        while (!stack.isEmpty()) {
            Move move = stack.pop();
            if (move.n == 1) {
                System.out.println("Přesun disk z " + move.from + " na " + move.to);
            } else {
                stack.push(new Move(move.n - 1, move.help, move.to, move.from));
                stack.push(new Move(1, move.from, move.to, move.help));
                stack.push(new Move(move.n - 1, move.from, move.help, move.to));
            }
        }
    }

    private static class Move {
        int n;
        char from;
        char to;
        char help;
        public Move(int n, char from, char to, char help) {
            this.n = n;
            this.from = from;
            this.to = to;
            this.help = help;
        }
    }
    public static void hanoiDFS(int n, char from, char to, char help) {
        Stack<Move> stack = new Stack<>();
        stack.push(new Move(n, from, to, help));
        while (!stack.isEmpty()) {
            Move move = stack.pop();
            if (move.n == 1) {
                System.out.println("Přesun disk z " + move.from + " na " + move.to);
            } else {
                stack.push(new Move(move.n - 1, move.help, move.to, move.from));
                stack.push(new Move(1, move.from, move.to, move.help));
                stack.push(new Move(move.n - 1, move.from, move.help, move.to));
            }
        }
    }
    public static void hanoiBFS(){}
}

