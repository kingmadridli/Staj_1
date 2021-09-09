#include <iostream>
using namespace std;
  		
  		// While Döngüsü Örnek_1
  		
int main(){
	
	int i = 1;
	int a,b;
	
	while (i<=5)
	{
		cout<<"Birinci sayiyi girin :";
		cin>>a;
		
		cout<<"Ikinci sayiyi girin :";
		cin>>b;
		
		cout<<"Iki sayinin toplamý = "<<a+b<<endl;
		i++;
	}
}
