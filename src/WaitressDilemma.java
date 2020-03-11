import java.util.*;

public class WaitressDilemma {
    public static void main(String[] args) {
        System.out.println(minBridges(6, 1, 3, 1, 5));
    }
    //originally tried to use recursion, but that doesn't work for a cyclic graph (super complicated)
    //use bfs instead (create a acyclic graph from a cyclic one)
    //dont need to deal with visited nodes, but big O blows up super fast
    //exponential time
    public static int minBridges(int n, int xi, int yi, int xj, int yj) {
    	ArrayList<int[]> current = new ArrayList<int[]>();
    	current.add(new int[] {xi, yi});
    	ArrayList<int[]> visited = new ArrayList<int[]>();
    	//we can move in the shape of an L
    	int[][] dirs = {new int[] {2,1}, new int[] {1,2}, new int[] {-2,1}, new int[] {-1,2}, new int[] {-2,-1}, new int [] {-1,-2}, new int[] {1, -2}, new int[] {2, -1}};
    	int steps = 0;
    	boolean found = false;
    	while(!found) {
    		ArrayList<int[]> next = new ArrayList<int[]>();
    		for(int[] coord : current) {
    			for(int[] dir : dirs) {
        			int newx = coord[0]+dir[0];
        			int newy = coord[1]+dir[1];
        			if(newx == xj && newy == yj) {
        				found = true;
        				break;
        			}
        			next.add(new int[] {newx, newy});
        			
        		}
    			
    		}
    		current = next;
    		steps++;
    	}
    	return steps;
    	
    }
    
}