import java.util.*;
import java.io.*;
public class Solution {


	private Solution() {

		
	}


	public static String re_hash(long h,int n) {

		StringBuilder c = new StringBuilder(9);
		String alphas = "acdegilmnoprstuw";
        int index = 0;

        while (h > n) {
        if (h % 37 == 0) {
            c.append(alphas.charAt(index));
		    index = 0;
		    h /= 37;
            
        }
			else {
			    h -= 1;
				index += 1;
			    
			}


		}

		return c.reverse().toString();
	}


	public static void main(String[] args) {

		long test = 930846109532517L;
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
        System.out.println(re_hash(test,n ));

	}



}