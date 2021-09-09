#include <iostream>
using namespace std;

int main(){
	
	int a[] = {1,2,3,4,5};	
	char t[] = "Sel";
	
	cout<<a<<endl;
	cout<<t<<endl;
	
	int *p = a;  // a deðiþkeni bir dizi olduðu için & iþareti konulmaz.
	
	cout<<*p<<endl;		   // {1,2,3,4,5};   ==> 1 deðeri   // aþaðýdaki de aynýsý
	
	cout<<p[0]<<endl;	//1
	cout<<p[3]<<endl;   // 4     
	
	cout<<*(p+1)<<endl; 	// {1,2,3,4,5};   ==> 2 deðeri
	cout<<*(p+3);   // 4      // p + 4bit x 3  ==> p + 12bit
}
