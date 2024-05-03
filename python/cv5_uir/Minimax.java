class Minimax {
    public static void main(String[] args) {
        int winStateLen = Integer.parseInt(args[0]);
        int myMarker = Integer.parseInt(args[1]);
        String board = args[2];

        System.out.println(winStateLen);
        System.out.println(myMarker);
        System.out.println(board);

//         TODO parse board
        for(String row: board.split("\\], \\["))
            System.out.println(row);



//         TODO decide next move
        int row = 0;
        int col = 1;

        System.out.print(":" + row + ";" + col);    //     DO NOT EDIT - return value is parsed from this format at the end of stdout
    }
}