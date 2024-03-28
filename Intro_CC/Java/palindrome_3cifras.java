// JAVA
import java.util.Scanner;

public class palindrome_3cifras {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Por favor ingrese el numero ");
        int n = sc.nextInt();
        
	if(n>=100 && n<= 999){
		int primerdig = n / 100;
		int tercerdig = n % 10;
		if(primerdig == tercerdig){
			System.out.print("El numero es palindrome");
		}else{
			System.out.print("El numero no es palindrome");
		}

	}else{
		System.out.print("El numero ingresado no esta en el rango");
	}
    }
}
