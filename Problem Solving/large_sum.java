import java.util.*;
public class large_sum
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int size=0;
        long sum=0;
        int i=0;
        size=sc.nextInt();
        long a[]=new long [size];
        for(i=0;i<size;i++)
        {
            a[i]=sc.nextLong();
            sum=sum+a[i];
        }
        System.out.println(sum);
    }
}

        
        
        
