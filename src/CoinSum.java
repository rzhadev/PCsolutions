import java.util.ArrayList;
import java.util.Arrays;
import java.util.Hashtable;

public class CoinSum {

	public static void main(String[] args) {
		int[] coins = {1,2,3};
		int m = coins.length;
		//time the execution speed
		long startTime = System.currentTimeMillis();
		int solutions = getPermutations(coins, 4);
		//int solutions = getMemoizedPermutations(coins, m, 200, new Hashtable<int[], Integer>());
		long endTime = System.currentTimeMillis();
		System.out.println("Found " + solutions + " in " + ( (double)endTime - (double)startTime)/ (double)1000 +" seconds.");
	}
	// Why does this not work?
	// because it counts duplicate solutions
	public static int getPermutations(int[] coins, int n) {
		if( n == 0) {
			return 1;
		}
		if ( n < 0) {
			return 0;
		}
		int ways = 0;
		for (int i = 0; i < coins.length; i++) {
			ways += getPermutations(coins, n-coins[i]);
			
		}
		
		return ways;
		
	}
	/**
	 * 
	 * @param coins are the given coin values
	 * @param index is the current length of the coin array we are looking at 
	 * @param n is the current sum we are looking for
	 * @return number of permutations for value n using coins
	 */
	
	public static int getRecursivePermutations(int[] coins, int len, int n) {
		//if we used too many coins, this is not a solution
		if(n < 0) {
			return 0;
		}
		//if the current total is 0, we found a solution
		if(n == 0) {
			return 1;
		}
		//if we used all the coins in the sub array and the current total is still not 0, there are no more solutions
		if (len <= 0 && n >= 0) {
			return 0;
		}
		//include the current coin and include in the recursion with total-this coin
		//exclude the current coin in the recursion and continue with len-1
		int total = getRecursivePermutations(coins, len-1, n) + getRecursivePermutations(coins, len, n-coins[len-1]);
		return total;
	}
	/**
	 * 
	 * @param coins are the given coins
	 * @param index is the current index
	 * @param n is the sub sum total
	 * @param memo is the memoization table
	 * @return number of permutations for value n using coins 
	 */
	public static int getMemoizedPermutations(int[] coins, int index, int n, Hashtable<int[], Integer> memo) {
		//look through each saved key to see if we have already calculated this solution total
		for(int[] key : memo.keySet()) {
			//if it exists then return that solution total
			if ((key[0] == n) && (key[1] == index)) {
				return memo.get(key);
			}
		}
		//if we used too many coins, this is not a solution
		if(n < 0) {
			return 0;
		}
		//if the current total is 0, we found a solution
		if(n == 0) {
			return 1;
		}
		//if we used all the coins in the sub array and the current total is still not 0, there are no more solutions
		if (index <= 0 && n >= 0) {
			return 0;
		}
		int total = getMemoizedPermutations(coins, index-1, n, memo) + getMemoizedPermutations(coins, index, n-coins[index-1], memo);
		int[] key = new int[] {n, index};
		memo.put(key, total);
		return memo.get(key);
	}

}
