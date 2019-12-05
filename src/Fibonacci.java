import java.util.Hashtable;

public class Fibonacci {

	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();
		//execution timing
		long endTime = System.currentTimeMillis();
		System.out.println("Took "+( (double)endTime - (double)startTime)/ (double)1000 +" seconds.");

	}
	/**
	 * 
	 * @param n is the nth index of the fibonacci series
	 * @return the value at n
	 */
	//bottom up using variable swapping
	public static int fibonacci1(int n) {
		int a = 0;
		int b = 1;
		for(int i = 1; i < n-1; i++) {
			int c = a;
			a = b;
			b = b + c;
		}
		return a + b;
	}
	/**
	 * 
	 * @param n is the nth index of the fibonacci series
	 * @return the value at n
	 */
	//bottom up using array
	public static int fibonacci2(int n) {
		int[] arr = new int[n]; 
		arr[0] = 0;
		arr[1] = 1;
		for(int i = 2; i < arr.length; i++) {
			arr[i] = arr[i-1] + arr[i-2];
		}
		return arr[n-1];
	}
	/**
	 * 
	 * @param n is the nth index of the fibonacci series
	 * @return the value at n
	 */
	//top down using recursion
	public static int recursiveFibonacci(int n) {
		if(n == 0) {
			return 0;
		}
		if(n == 1) {
			return 1;
		}
		return recursiveFibonacci(n-1) + recursiveFibonacci(n-2);
	}
	/**
	 * 
	 * @param n is the nth index of the fibonacci series
	 * @param memo is the memoization table to hash values from
	 * @return the value at n
	 */
	//top down using memoized recursive values
	public static int memoFibonacci(int n, Hashtable<Integer, Integer> memo) {
		if(memo.containsKey(n)) {
			return memo.get(n);
		}
		if(n == 0) {
			return 0;
		}
		if(n == 1) {
			return 1;
		}
		int value = recursiveFibonacci(n-1) + recursiveFibonacci(n-2);
		memo.put(n, value);
		return memo.get(n);
	}
	

}
