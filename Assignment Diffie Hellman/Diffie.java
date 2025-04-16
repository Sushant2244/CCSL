import java.util.*;

class Diffie {
    static int findPrimitive(int prime_no) {
        int phi = prime_no - 1;
        for (int i = 2; i < prime_no; i++) {
            boolean flag = true;
            for (int j = 1; j < phi; j++) {
                if (Math.pow(i, j) % prime_no == 1 ) {
                    flag = false;
                    break;
                }
            }
            if (flag==true) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       
        System.out.println("Enter Prime Number:");
        int prime_no = sc.nextInt();

        int primitive_root = findPrimitive(prime_no);


        System.out.println("Enter private key of A:");
        int private_key_A = sc.nextInt();

        System.out.println("Enter private key of B:");
        int private_key_B = sc.nextInt();

        System.out.println("Primitive root of " + prime_no + " is " + primitive_root);
        
        if(private_key_A<prime_no && private_key_B<prime_no){

        int public_key_A = (int) (Math.pow(primitive_root, private_key_A) % prime_no);
        System.out.println("\nPublic Key of A is: " + public_key_A);

        int public_key_B = (int) (Math.pow(primitive_root, private_key_B) % prime_no);
        System.out.println("\nPublic Key of B is: " + public_key_B);

        int sec_key_A = (int) (Math.pow(public_key_B, private_key_A) % prime_no);
        System.out.println("\nSecret Key of A is: " + sec_key_A);

        int sec_key_B = (int) (Math.pow(public_key_A, private_key_B) % prime_no);
        System.out.println("\nSecret Key of B is: " + sec_key_B);
        }
        else{
            System.out.println("Enter valid private keys");
        }
    }
}
