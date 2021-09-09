#include <iostream>
using namespace std;

    // Karar Yapýlarý örnek_5
    // Ýç içe if kullanýmý

int main(){
	
	string a;
	int sifre;
	
	cout<<"Kullanici adi giriniz : ";
	cin>>a;
	
	if (a=="Ozgur")
	{
		cout<<"Kullanici Adi Dogru "<<endl;
		cout<<"Sifre giriniz :"<<endl;
		cin>>sifre;
		if (sifre == 0000)
		{
			cout<<"Sifre dogru ";
		}
		else
		{
			cout<<"Sifre Yanlis";
		}
		
	}
	else
	    cout<<"Bulunamadi";
}






