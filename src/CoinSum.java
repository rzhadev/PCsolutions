import java.util.ArrayList;
import java.util.Hashtable;

public class CoinSum {

	public static void main(String[] args) {
		int[] coins = {1, 2, 5, 10, 20, 50, 100, 200};
		int m = coins.length;
		//time the execution speed
		long startTime = System.currentTimeMillis();
		int solutions = getPermutations(coins, 200);
		//int solutions = getMemoizedPermutations(coins, m, 200, new Hashtable<int[], Integer>());
		long endTime = System.currentTimeMillis();
		System.out.println("Found " + solutions + " in " + ( (double)endTime - (double)startTime)/ (double)1000 +" seconds.");
	}
	/**
	 * 
	 * @param coins is the given values of each coin
	 * @param n is the value which is being looked for
	 * @return the number of permutations for that coin value
	 */
	//BOTTOM UP APPROACH 
	//looks for all ways to get a total starting at a total of 0 up to totals of n-1
	public static int getPermutations(int[] coins, int n) {
		int[] ways = new int[n+1];
		ways[0] = 1;
		for(int i = 0; i < coins.length; i++) {
			for(int j = 0; j < ways.length; j++) {
				if(coins[i] <= j) {
					ways[j] = ways[j-coins[i]]+ways[j];
				}
			}
		}
		return ways[n];
	}
	/**
	 * 
	 * @param coins are the given coin values
	 * @param index is the current length of the coin array we are looking at 
	 * @param n is the current sum we are looking for
	 * @return number of permutations for value n using coins
	 */
	//TOP DOWN APPROACH
	//this solutions works by looking for all the sums of n by breaking the problem down into sub problems of coins[m-1] and sums of n-coins[m-1]
	//you can memoize this by understanding that for a certain sum there must be a certain length to the coins array
	public static int getRecursivePermutations(int[] coins, int index, int n) {
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
		//getRecursivePermutations(coins, m-1, n) looks for coins in the coins array top down (starting at end of array and going backwards)
		//getRecursivePermutations(coins, m, n-coins[m-1]) looks for sub sum solutions (looks for coins to add up to a new sub total)
		int total = getRecursivePermutations(coins, index-1, n) + getRecursivePermutations(coins, index, n-coins[index-1]);
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
