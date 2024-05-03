public class HanoiSolver {

    public static void main(String[] args) {
        char[] initialState = {'A', 'A', 'A'};
        System.out.println("DFS:");
        DFS dfs = new DFS();
        dfs.DFS(initialState);
        System.out.println("BFS:");
        BFS bfs = new BFS();
        bfs.BFS(initialState);
    }
}
