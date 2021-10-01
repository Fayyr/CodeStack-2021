#include <stdio.h>
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int maxProfit(vector<int> &prices) {
    int maxPro = 0;
    int minPrice = 100000;
    for(int i = 0; i < prices.size(); i++){
        minPrice = min(minPrice, prices[i]);
        maxPro = max(maxPro, prices[i] - minPrice);
    }
    return maxPro;
}


int main(){
vector<int> prices;
int temp;
int sizeofarray;
cin >> sizeofarray;
for (int i = 0; i < sizeofarray; ++i)
{
    cin>>temp;
    prices.push_back(temp);
}

int output = maxProfit(prices);
cout<<output;

return 0;
}