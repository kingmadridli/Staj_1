#include <iostream>
using namespace std;

int main(){
	
	int i;
	// Break Ýfadesi  == > Döngüyü Orada Kapatýr.
	// Continue Ýfadesi ==> Düngü O ifadeye gelince atlar
	for (i=1;i<=10;i++)
	
	{
		if (i == 5)
			//break;      // Döngü biter, en son 5 görünür.
			continue;    // 5 yazdýrýlmaz , 6 dan devam eder.
		cout<<i<<endl;
		
	}
	
	
}
