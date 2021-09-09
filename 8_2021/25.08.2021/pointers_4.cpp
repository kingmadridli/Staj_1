#include <iostream>
using namespace std;


void Arttir(int *a)
	{
		(*a)++;
	}

int main(){
	
	int sayi = 120;
	cout<<"Artirdan once ...: "<<sayi<<endl;
	
	Arttir(&sayi);
	
	cout<<"Artirdan sonra ...: "<<sayi<<endl;
	
	
}
