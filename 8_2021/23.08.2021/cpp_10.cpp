#include <iostream>
using namespace std;

		// Karar Yapýlarý Örnek_4
		// Üçgenin Ýç Açýlarý
		
int main(){
	
	int aci_1,aci_2,aci_3;
	
	cout<<"Birinici Aciyi Giriniz :";
	cin>>aci_1;
	
	cout<<"Ikinici Aciyi Giriniz :";
	cin>>aci_2;
	
	aci_3 = 180 - (aci_1 + aci_2);
	
	cout<<"Ucgenin diger acisi = "<<aci_3;
}
