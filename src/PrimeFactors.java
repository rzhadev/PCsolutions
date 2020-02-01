import java.util.*;

public class PrimeFactors {
    public static void main(String[] args){
        long n = 600851475143L;
        System.out.println(greatestPrimeFactor(n));
    }
    public static long greatestPrimeFactor(long n){
        long maxFactor = 0;
        long m = Long.valueOf(n); //why is this needed?
        for(long i = 2; i < n-1; i++ ){
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