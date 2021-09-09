#include <iostream>
using namespace std;

    // Karar Yapýlarý Örnek_2

int main(){
	
	int vize,final;
	double ort;
	
	cout<<"Vize notunuzu giriniz :"<<endl;
	cin>>vize;
	
	cout<<"Final notunuzu giriniz : "<<endl;
	cin>>final;
	
	ort = vize*0.4 + final*0.6;
	
	if (ort >= 90 && ort < 100)
	{
		cout<<"Notunuz :"<<ort<<endl<<"Harf Notu A \n";
	}
	else if (ort >= 75 && ort < 90)
	{
		cout<<"Notunuz :"<<ort<<endl<<"Harf Notu B \n";
	}
	else if (ort >= 60 && ort < 75)
	{
		cout<<"Notunuz :"<<ort<<endl<<"Harf Notu C \n";
	}
	else if (ort >= 50 && ort < 60)
	{
		cout<<"Notunuz :"<<ort<<endl<<"Harf Notu D \n";
	}
	else
	{
		cout<<"Notunuz :"<<ort<<endl<<"Kaldiniz \n";
	}
	
	
	
	
	
	
	
	
	
	
}
