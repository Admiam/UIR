import java.util.*;

public class BFS {

    char[] targetState = {'C', 'C', 'C'};
    final int DISK_COUNT = 3;
    Set<String> visited = new HashSet<>();
    char[][] path = new char[1000][DISK_COUNT];

    public void BFS(char[] state) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(null, state));
        visited.add(Arrays.toString(state));


        int pathIndex = 0;

        while (!queue.isEmpty()) {
            Node currentState = queue.poll();

            if (Arrays.equals(currentState.state, targetState)) {
                printState(currentState.state);
                System.out.println("Solution found.");
                printPath(currentState);
                return;
            }

            List<char[]> possibleMoves = getPossibleMoves(currentState.state);
            for (char[] move : possibleMoves) {
//                System.out.print( Arrays.toString(move));
                if (!visited.contains(Arrays.toString(move))) {
//                    System.out.println("Visited: " + visited);
                    visited.add(Arrays.toString(move));
//                    System.out.println("Adding to queue: " + Arrays.toString(move));
                    queue.add(new Node(currentState, move));
                }
            }
//            System.out.println();
            path[pathIndex++] = currentState.state.clone();
        }
    }
    public void printState(char[] state) {
        System.out.println(Arrays.toString(state));
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

    public void printPath(Node finalNode) {
        List<char[]> pathList = new ArrayList<>();
        while (finalNode != null) {
            pathList.add(finalNode.state);
            finalNode = finalNode.parent;
        }
        for (int i = pathList.size() - 1; i >= 0; i--) {
            System.out.println(Arrays.toString(pathList.get(i)));
        }
        System.out.println("Length: " + pathList.size());
    }
}
