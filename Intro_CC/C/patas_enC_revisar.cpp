# include<stdio.h>

int main(){
	int x;
	int y;
	printf("ingrese el numero de animales ");
	scanf("%d", &x);
	printf("ingrese el numero de patas ");
	scanf("%d", &y);
	While(x<0 || y<=2*x || y%2!=0){
		printf("No se puede realizar tu cálculo, por favor vuelve a ingresar un numero de animales: ");
		scanf("%d", &x);
		printf("por favor vuelve a ingresar un numero de patas: ");
		scanf("%d", &y);
		}

	int c = (y-2*x)/2;
		int g = x - c;
		printf("El numero de conejos es: %d y el numero de gansos es %d", c, g);
	return 0
}

/*
Para compilar programa en C:

gcc nombre.c

a.exe + tab

*/
