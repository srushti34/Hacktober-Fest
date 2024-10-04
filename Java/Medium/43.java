// Question: Complete the function to perform depth-first search (DFS) on a graph.

class Main {
    public static void dfs(int[][] graph, int start, boolean[] visited) {
        visited[start] = true;
        System.out.print(start + " ");

        for (int i = 0; i < graph[start].length; i++) {
            if (graph[start][i] == 1 && !visited[i]) {
                dfs(graph, i, visited);
            }
        }
    }

    public static void main(String[] args) {
        int[][] graph = {
            {0, 1, 1, 0},
            {1, 0, 1, 1},
            {1, 1, 0, 1},
            {0, 1, 1, 0}
        };
        boolean[] visited = new boolean[graph.length];
        System.out.print("DFS: ");
        dfs(graph, 0, visited);
    }
}
