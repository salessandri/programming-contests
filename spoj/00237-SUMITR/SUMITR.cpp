#include <iostream>
using namespace std;
int main(){
int tc;cin>>tc;while(tc--){int i,j,r,t[101][101];cin>>r;for(i=0;i<r;i++){for(j=0;j<=i;j++)cin>>t[i][j];}for(i=r-2;i>=0;i--){for(j=0;j<=i;j++)t[i][j]+=max(t[i+1][j],t[i+1][j+1]);}cout<<t[0][0]<<endl;}
}
