#include <iostream>
using namespace std;

int main(){
	
	int a = 12;
	int *p = &a;
	
	cout<<"p : "<<p<<endl;    
	cout<<"&a : "<<&a<<endl;
	cout<<"*p : "<<*p<<endl;
	cout<<"a : "<<a<<endl;
	
	// *p adresini tuttuğu  değişkene değişim uyguluyoruz
	*p = 220;   // adres değişmez, adresini tuttuğu değişken artık 12 değil 220 olur
	
	cout<<"Degisimden Sonra"<<endl;
	
	cout<<"p : "<<p<<endl;    
	cout<<"&a : "<<&a<<endl;
	cout<<"*p : "<<*p<<endl;
	cout<<"a : "<<a<<endl;

}
