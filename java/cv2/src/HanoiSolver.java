import java.util.*;

public class HanoiSolver {

    char[] targetState = {'C', 'C', 'C'};
    final int DISK_COUNT = 3;
    Stack<String> visited = new Stack<>();
    List<char[]> path = new ArrayList<>();

    public void solveHanoiDFS(char[] state) {
        Stack<Node> stack = new Stack<>();
        stack.push(new Node(null, new State(state)));
        visited.push(new String(state));

        while (!stack.isEmpty()) {
            Node currentState = stack.pop();

            if (currentState.isGoal(targetState)) {
                printState(currentState.state.state);
                System.out.println("Solution found.");
                printPath(currentState);
                return;
            }

            List<char[]> possibleMoves = getPossibleMoves(currentState.state.state);

            for (char[] move : possibleMoves) {
                char[] newState = move.clone();
                if (!visited.contains(new String(newState))) {
                    visited.push(new String(newState));
                    State nextState = new State(newState);
                    Node nextNode = new Node(currentState, nextState);
                    stack.push(nextNode);
                }
            }
        }
    }

    public List<char[]> getPossibleMoves(char[] state) {
        List<char[]> moves = new ArrayList<>();

        for (int i = 0; i < DISK_COUNT; i++) {
            char disk = state[i];
            int currentTop = getTop(disk, state);

            for (int j = 0; j < 3; j++) {
                char nextDisk = (char) ('A' + j);
                int nextTop = getTop(nextDisk, state);
                if (currentTop < nextTop && !isAnyDiskAbove(i, state)) {
                    char[] newState = state.clone();
                    newState[i] = (char) ('A' + j);
                    moves.add(newState);
                }
            }
        }
        return moves;
    }

    public boolean isAnyDiskAbove(int disk, char[] state) {
        char currentDisk = state[disk];
        if (disk == 0) {
            return false;
        } else if (disk == 1) {
            return currentDisk == state[0];
        } else {
            return currentDisk == state[0] || currentDisk == state[1];
        }
    }

    public int getTop(char stack, char[] state) {
        for (int i = 0; i < DISK_COUNT; i++) {
            if (state[i] == stack) {
                return i;
            }
        }
        return Integer.MAX_VALUE;
    }

    public void printState(char[] state) {
        System.out.println(new String(state));
    }

    public void printPath(Node node) {
        Node currentNode = node;
        List<String> list = new ArrayList<>();
        while (currentNode.parent != null) {
            list.add(new String(currentNode.state.state));
            currentNode = currentNode.parent;
        }

        for (int i = list.size() - 1; i >= 0; i--) {
            System.out.println(list.get(i));
        }
    }

    class Node {
        Node parent;
        State state;

        Node(Node parent, State state) {
            this.parent = parent;
            this.state = state;
        }

        boolean isGoal(char[] target) {
            return Arrays.equals(state.state, target);
        }
    }

    class State {
        char[] state;

        State(char[] state) {
            this.state = state;
        }
    }

    public static void main(String[] args) {
        HanoiSolver solver = new HanoiSolver();
        char[] initialState = {'A', 'A', 'A'};
        solver.solveHanoiDFS(initialState);
    }
}
