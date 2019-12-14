import java.util.ArrayList;

public class MorningBuns {

	public static void main(String[] args) {
		char[][] arr = new char[][] { new char[] {'I', '*', 'l', 'o', 'v'}, new char[] {'o', 'u', '*', 's', 'e'}, new char[] {'y', ' ', ' ', 'm', '*'}, new char[] {'*', 'e', 'l', 'i', 't'}, new char[] {'e', 'e', 's', '*', 'o' }};
		System.out.println(messageReveal(arr));
	}
	public static String messageReveal(char[][] characters) {
		//row, col direction pair to move
		int[] dir = new int[] {-1,1};
		//row, col
		int[] pos = new int[] {0,0};
		//how far to move
		int mag = characters[0].length;
		String s = "";
		//do first row first
		for(int i = 0; i < mag; i++) {
			s += characters[0][i];
		}
		pos[0] = 1;
		pos[1] = characters[0].length-1;
		mag--;
		//continue until move length is 0
		while( mag >= 0) {
			int start;
			//y bottom-up
			if(dir[1] < 0) {
				start = pos[0];
				for(int i = 0; i < mag; i++) {
					s += characters[start+i*dir[1]][pos[1]];
					pos[0] = start+i*dir[1];
				}
				pos[1]++;
			}
			//y top-down
			else if(dir[1] > 0) {
				start = pos[0];
				for(int i = 0; i < mag; i++) {
					s += characters[start+i*dir[1]][pos[1]];
					pos[0] = start+i*dir[1];
				}
				pos[1]--;
			}
			//x right to left
			if(dir[0] < 0) {
				start = pos[1];
				for(int i = 0; i < mag; i++) {
					s += characters[pos[0]][start+i*dir[0]];
					pos[1] = start+i*dir[0];
				}
				pos[0]--;
			}
			//x left to right
			else if(dir[0] > 0) {
				start = pos[1];
				for(int i = 0; i < mag; i++) {
					s += characters[pos[0]][start+i*dir[0]];
					pos[1] = start+i*dir[0];
				}
				
				pos[0]++;
			}
			
			//change the direction to move in following the pattern
			if(dir[0] > 0) {
				dir[0] = -1;
			}
			else if(dir[0] < 0) {
				dir[0] = 1;
			}
			if(dir[1] > 0) {
				dir[1] = -1;
			}
			else if(dir[1] < 0) {
				dir[1] = 1;
			}
			
			mag--;
		}
		//replace * with spaces
		s = s.replace('*', ' ');
	
		return s;
	}

}
