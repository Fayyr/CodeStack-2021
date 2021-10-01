#include <iostream>
using namespace std;
int main() {
    // your code goes here
    int t;
    cin>>t;
    while(t--){
        int X,A,B;
        cin>>X>>A>>B;
        int ans=A + ((100-X)*B);
        //ans*= 10; //1 litre= 1000 ml; / 100 ml
        std::cout << (ans*10) << std::endl;
    }
return 0;
}

