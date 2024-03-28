#include <iostream>
using namespace std;

int main(){
	int a, b, n, resultado;
	cout<<"ingrese el primer numero: ";
	cin >> a;
	cout<<"ingrese el segundo numero: ";
	cin >> b;
	cout << "Menu de operaciones: ";
	cout << "1. a+b, " << endl;
	cout << "2. a-b, " << endl;
	cout << "3. a*b, " << endl;
	cout << "4. a/b, " << endl;
	cout << "Digita el numero de operación a realizar: ";
	cin >> n;
	switch(n) {
		case 1:
			resultado = a+b;
			cout<< resultado;
			break;
		case 2:
			resultado = a-b;
			cout<< resultado;
			break;
		case 3:
			resultado = a*b;
			cout<< resultado;
			break;
		case 4:
			resultado = a/b;
			cout<< resultado;
			break;		
		default:
			cout << "operacion invalida";
	}
	return 0;
}

/*
Para compilar programa en C++:

gpp nombre.c

a.exe + tab

*/
