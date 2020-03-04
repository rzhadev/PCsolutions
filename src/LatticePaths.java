import java.util.Hashtable;

public class LatticePaths {

	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();
		System.out.println(routes(19, new int[] {0,0}, new Hashtable<String, Long>()));
		long endTime = System.currentTimeMillis();

	}
	public static long routes(int gridsize, int[] coords, Hashtable<String, Long> map) {
		//number of ways from any point = number of ways from point to the right + number of ways from point down
		//if i am at the bottom
		String coordkey = Integer.toString(coords[0])+Integer.toString(coords[1]);
		//System.out.println(coordkey);
		if(map.containsKey(coordkey)) {
			return map.get(coordkey);
		}
		if(coords[0] == gridsize || coords[1] == gridsize) {
			return 1;
		}
		else {
			long total = 0L;
			if(coords[0] < gridsize) {
				total += routes(gridsize, new int[] {coords[0]+1, coords[1]}, map);
			}
			if(coords[1] < gridsize) {
				total += routes(gridsize, new int[] {coords[0], coords[1]+1}, map);
			}
			if(!map.containsKey(coordkey)) {
				System.out.println("coordkey "+coordkey+" total "+total);
				map.put(coordkey, total);
			}
			return total;
		}
	}

}
