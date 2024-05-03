public class Node {
    Node parent;
    char[] state;

    Node(Node parent, char[] state) {
        this.parent = parent;
        this.state = state;
    }
}