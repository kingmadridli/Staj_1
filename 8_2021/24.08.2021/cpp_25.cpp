#include <iostream>  
using namespace std;

	// String Fonksiyonlarý    lenght() - append() - assign()

int main(){
	
	string a = "Ozgur Cetin";
	cout<<a<<endl;
	cout<<a.length()<<endl;     //   lenght  ==>  string ifadenin karakter uzunluðunu geriye döndürür.
	
	string b = "Marmara Universitesi ";
	cout<<b<<endl;
	cout<<b.append("Eklendi")<<endl;    //  append  ==>  Sadece eklendi olarak çýktý vermez, ekleyerek hafýzaya atar.
	cout<<b.append("Eklendi",2)<<endl;
	
	string c = "Mekatronik";          
	cout<<c<<endl;						// assign  ==>  deðiþkenin içeriðini deðiþtirir.
	cout<<c.assign("Yeni String")<<endl;
	cout<<c<<endl;	
}

