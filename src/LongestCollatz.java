import java.util.*;
public class LongestCollatz {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long startTime = System.currentTimeMillis();
		System.out.println(chain(13));
		long endTime = System.currentTimeMillis();
		System.out.println(( (double)endTime - (double)startTime)/ (double)1000 +" seconds.");

	}
	//Must memoize sub problem solutions to solve
	//avoid recalculating subproblems
	//m must be a long, because int will overflow
	//Hashtable k -> v
	public static int chain(int n) {		
		Hashtable<Long, Integer> map = new Hashtable<Long, Integer>();
		int maxlength = 0;
		int max_n = 0;
		for(int i = 1; i < 1000000; i++) {
			long m = Long.valueOf(i);
			//terms have to be at least 1 in length
			int terms = 1;
			while(m != 1) {
				//if we have already calculated, get from hashtable
				if(map.containsKey(m)) {
					terms += (map.get(m))-1;
					break;
				}
				if(m%2 == 0) {
					m /= 2;
					terms++;	

				}
				else {
					m = 3*m + 1;
					terms++;	

				}
			}
			if(terms > maxlength) {
				maxlength = terms;
				max_n = i;
			}
			//if we havent calculated this before, add it to the hashtable
			if(!map.containsKey(Long.valueOf(i))) {
				map.put(Long.valueOf(i), terms);
			}
			
		}
		return max_n;
		
	}

}
