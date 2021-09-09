#include <iostream>
using namespace std;
// Basit Hesap Makinesi
int main(){
	int a,b;
	double add,minus,multiply,division;
	cout<<"birinci sayiyi giriniz";
	cin>>a;
	cout<<"ikinci sayiyi giriniz";
	cin>>b;
	add = a + b;
	minus = a - b;
	multiply = a * b;
	division = a / b;
	cout<<"iki sayinin toplami :"<<add<<endl;
	cout<<"iki sayinin farki :"<<minus<<endl;
	cout<<"iki sayinin carpimi :"<<multiply<<endl;	
	cout<<"iki sayinin bolumu :"<<division;
	
}
