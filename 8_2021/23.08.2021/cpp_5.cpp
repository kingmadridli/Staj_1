#include <iostream>
using namespace std;

// Global Deðiþken
int a = 5;

int main(){
	
	// local deðiþken
	int b = 5; 	
	cout<<a<<endl;
	
	// Özel Karakterler
	string str_1 = "Merhaba Dunya\n";   // \n  veya \r  ==> Yeni bir satýr oluþturur.
	string str_2 = "Hello World\t";    // \t ==> bir tab boþluk býrakýr.
	cout<<str_1<<str_2;
	
	// \v  ==> Dikey tab boþluk býrakýr.
	// \f  ==> Sayfa sonu
	// \'  ,  \"  , \?   ==> Özel karakterlerin görünmesi saðlar.
	// \b  ==> Sola doðru bir karakter siler.   
	
	
	/* 
	
	Aritmetik Operatörler
	
	+ Toplama
	- Çýkarma
	* Çaprma
	/ Bölme
	% Mod Alma
	
	Bileþik Atama Operatörleri
	
	a += b     ==> a = a + b
	a -= b     ==> a = a - b
	a *= b     ==> a = a * b
	a /= b     ==> a = a / b
	
	a++  ==> a = a + 1
	a--  ==> a = a - 1
	
		
	a = 3; b = a++;     Ýþlem sonunda a = 4 , b = 3    ==> *** Önce ata sonra artýr.***
	a = 3; b = ++a,     Ýþlem sonunda a = 4 , b = 4    ==Z *** Önce artýr sonra ata.***
	
	
	Ýliþkisel Operatörler
	
	 == Eþittir 
	 != Eþit deðildir
	 > Büyüktür
	 < Küçüktür
	 >= Büyük Eþit
	 <= Küçük Eþit
	


	a      ==> a deðeri
	b      ==> b deðeri
	!a     ==> a nýn deðili
	a && b ==> a ve b 
	a || b ==> a veya b





	*/	

	
}
