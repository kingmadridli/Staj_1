#include <iostream>
using namespace std;

	// Switch-Case  Karar Yapýsý

int main(){
	
	int i;
	cout<<"1-4 arasinda bir sayi giriniz :\t";
	cin>>i;
	
	switch(i){
		case 1:      // case i'nin deðeri :     þeklinde tanýmlanýr
			cout<<"1 Girdiniz";
			break;              // Switch-case karar yapýsýndan çýkar.
		case 2:
			cout<<"2 Girdiniz";
			break;
		case 3:
			cout<<"3 Girdiniz";
			break;
		case 4:
			cout<<"4 Girdiniz";
			break;
		default:           // default yazýlmadýðý takdirde de program çalýþýr.
			cout<<"Yanlis deger girdiniz.";
	}
}
