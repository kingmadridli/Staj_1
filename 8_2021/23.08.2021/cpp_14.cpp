#include <iostream>
using namespace std;


	// For Döngüsü

int main(){
	/*
	int a = 50;
	int b = 30;
	
	cout<<a++<<endl;   // Önce yazdýr sonra artýr.
	cout<<++b<<endl;   // Önce artýr sonra yazdýr.
	cout<<a;    // artýrýlmýþ hali
	*/
	
	
	/*
	int i;
	for (i=1;i<=10;i++)    // i, 1 den 10 kadar 1'er 'er artaracak þekilde döngüyü saðla
	{
		cout<<"Merhaba Dunya"<<endl;
	}
	*/
	
	int a;
	int i;
	//cout<<"Bir sayi giriniz :"<<endl;
	//cin>>a;
	
	for (i=1;i<=10;i++)
	{
		cout<<"Bir sayi giriniz :"<<endl;
		
		cin>>a;
		
		if (a % 2 == 0)
		{
			cout<<"Cifttir "<<endl;
		}
		else
		{
			cout<<"Tektir. "<<endl;
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
