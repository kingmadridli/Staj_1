#include <iostream>
using namespace std;
	// Pointers Kullaným Amacý:

// Define Func
int Degistir(int *a, int *b) // ( sayi1'in adresi, sayi2'nin adresi)
{
	// a  = &sayi1   , b = &sayi2
	*a = 20;   // adresteki deðeri 20 yap 
	*b = 40;   // adresteki deðeri 40 yap
	cout<<a<<endl<<b;          // sayi1 ve sayi2 nin adres deðerleri
	
	return *a + *b;   // 20 + 40,  ==>  return 60 
}
// Define Main
int main(){
	
	int sayi1,sayi2;
	sayi1 = 3;
	sayi2 = 5;
	int sonuc = Degistir(&sayi1,&sayi2);   // Fonksiyona sayi1 ve sayi2' nin adreslerini yolla
	cout<<""<<endl;
	cout<<sonuc;   // Sonuc, Fonksiyonun return deðeridir.  
}
