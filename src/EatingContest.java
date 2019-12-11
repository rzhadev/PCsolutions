
public class EatingContest {

	public static void main(String[] args) {
		int[] arr = new int[] {232,10,1,484};
		System.out.println(winner(arr));

	}
	public static String winner(int[] scores) {
		int matt = 0;
		int joey = 0;
		for(int i = 0; i < scores.length; i++) {
			if(i%2 == 0) {
				matt += scores[i];
			}
			else {
				joey += scores[i];
			}
		}
		if (matt == joey) {
			return "tie";
		}
		else if (matt > joey) {
			return "matt";
		}
		return "joey";
	}
	

}
