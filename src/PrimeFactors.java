import java.util.*;

public class PrimeFactors {
    public static void main(String[] args){
        long n = 600851475143L;
        System.out.println(greatestPrimeFactor(n));
    }
  
    //linear time
    public static long greatestPrimeFactor(long n){
        long maxFactor = 1;
        long m = n; //why is this needed?
        for(long i = 2; i < n; i++ ){
            while( m % i == 0){
                m /= i;
                if(i > maxFactor){
                    maxFactor = i;
                }
            }
            if (m == 1){
                break;
            }
            
        }
        return maxFactor;
    }
}