// Question: Complete the function to find all paths from the top-left corner to the bottom-right corner of a maze.

import java.util.ArrayList;
import java.util.List;

class Main {
    public static List<String> findAllPaths(int[][] maze, int x, int y, String path) {
        List<String> result = new ArrayList<>();
        if (x == maze.length - 1 && y == maze[0].length - 1) {
            result.add(path);
            return result;
        }

        // Move down
        if (x + 1 < maze.length && maze[x + 1][y] == 1) {
            result.addAll(findAllPaths(maze, x + 1, y, path + "D"));
        }

        // Move right
        if (y + 1 < maze[0].length && maze[x][y + 1] == 1) {
            result.addAll(findAllPaths(maze, x, y + 1, path + "R"));
        }

        return result;
    }

    public static void main(String[] args) {
        int[][] maze = {
                {1, 0, 0, 0},
                {1, 1, 0, 1},
                {0, 1, 0, 0},
                {1, 1, 1, 1}
        };

        List<String> paths = findAllPaths(maze, 0, 0, "");
        for (String path : paths) {
            System.out.println(path);
        }
    }
}
