#include <iostream>

using namespace std;

int i, j, k;

int main(){

    i = 2;
    cout << "Hello" << endl;
    cin >> j ;
    k = i + j ;
    cout << k << " is the result" << endl;
    
    for(i=0; i<=k; i++){
        cout << "*"<< endl;
    }


    return 0;
}