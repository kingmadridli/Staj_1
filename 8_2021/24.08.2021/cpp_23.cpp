#include <iostream>
using namespace std;

	// Fonksiyonlar

void Toplama()
{
	int a,b;   // Local Deðiþkenler  ==> Sadece bu fonsiyona özgü a ve b deðerleridir.
	
	cout<<"Birinci Sayiyi girin :"<<endl;
	cin>>a;
	
	cout<<"Ikinci sayiyi girin :"<<endl;
	cin>>b;
	
	cout<<"Iki sayinin toplami = "<<a + b<<endl;
}

void Cikar()
{
	int a,b;   // local Deðiþkenler
	
	cout<<"Birinci Sayiyi girin :"<<endl;
	cin>>a;
	
	cout<<"Ikinci sayiyi girin :"<<endl;
	cin>>b;
	
	cout<<"Iki sayinin farki = "<<a - b<<endl;
}

int main(){
	
	Toplama();
	Cikar();
	
	
	
	
	
}








