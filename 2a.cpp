#include <iostream>
#include <cmath>



using namespace std;



void tulis(double &up, double &low, double &rectangle)
{	cout << "upper " ;
	cin >> up;
	cout << "lower" ;
	cin >> low;
	cout << "rectangle " ;
	cin >> rectangle;
}
double hitung(double &up, double &low, double &rectangle, double &f, double &width, double &area,double &bb,double &p,int &i)
{
	width = ((up-low)/rectangle);
	for (i = 0; i < rectangle +1 ;i++)
	{
		f = pow(sin(low),0.5); // jadi f1
		low = low + width; // x1 jadi x2
		bb = pow(sin(low),0.5) ; // f2
		p = p + f + bb;
	
	}
	return p*width*0.5;
}

int main() {
	double up,low,rectangle,f,width,area,bb,p;
	int i;
	tulis(up,low,rectangle);
	cout << hitung( up, low, rectangle, f, width, area,bb,p,i ) << endl;
	return 0;
}

	
