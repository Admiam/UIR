import java.util.*;


public class DFS {

    char[] targetState = {'C', 'C', 'C'};
    final int DISK_COUNT = 3;
    Set<String> visited = new HashSet<>();
    char[][] path = new char[1000][DISK_COUNT];

    public void DFS(char[] state) {
        Stack<Node> stack = new Stack<>();
        stack.push(new Node(null, state.clone()));
        visited.add(Arrays.toString(state));

        int pathIndex = 0;

        while (!stack.isEmpty()) {
            Node currentState = stack.pop();

            if (Arrays.equals(currentState.state, targetState)) {
                path[pathIndex++] = targetState.clone();
                printState(currentState.state);
                System.out.println("Solution found.");
                printPath(pathIndex);
                return;
            }

            List<char[]> possibleMoves = getPossibleMoves(currentState.state);

            for (char[] move : possibleMoves) {
//                System.out.println("Move: " + Arrays.toString(move));
//                System.out.println("Visited: " + visited);
                if (!visited.contains(Arrays.toString(move))) {
                    visited.add(Arrays.toString(move));
//                    System.out.println("Adding to stack: " + Arrays.toString(move));
                    stack.push(new Node(currentState, move));
                }
            }
            path[pathIndex++] = currentState.state.clone();
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

    public int getTop(char stack, char[] state) {
        for (int i = 0; i < DISK_COUNT; i++) {
            if (state[i] == stack) {
                return i;
            }
        }
        return Integer.MAX_VALUE;
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

    public void printState(char[] state) {
        System.out.println(Arrays.toString(state));
    }

        public void printPath(int pathIndex) {
        for (int i = pathIndex - 1; i >= 0; i--) {
            System.out.println(Arrays.toString(path[i]));
        }
        System.out.println("Length: " + pathIndex);
    }

}
