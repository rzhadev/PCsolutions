import java.util.ArrayList;

public class DistinctPowers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(combinations(100,100));
	}
	public static int combinations(int a, int b) {
		ArrayList<Double> terms = new ArrayList<Double>();
		for(int i = 2; i <= a; i++) {
			for(int k = 2; k <= b; k++) {
				double exp = Math.pow(i, k);
				if(!terms.contains(exp)) {
					terms.add(exp);
				}
				
			}
		}
		return terms.size();
	}
}
